package main

import (
	"encoding/json"
	"fmt"
	"io/fs"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"regexp"
	"text/template"
)

// Config holds the readme generator configuration
type Config struct {
	Repo      string            `json:"repo"`
	Languages map[string]string `json:"languages"`
	Scopes    []string          `json:"scopes"`
	Template  string            `json:"template"`
}

// NewConfig read the config file and return a Config structs
func NewConfig(cfpath string) (Config, error) {
	data, err := ioutil.ReadFile(cfpath)
	if err != nil {
		log.Fatalf("Couldn't read %s", cfpath)
	}
	var cf Config
	if err := json.Unmarshal(data, &cf); err != nil {
		log.Fatalf("Couldn't decode json file %s", cfpath)
	}
	return cf, nil
}

// CodeSnippet ....
type CodeSnippet struct {
	Filename string
	Language string
	// Lines    []string
	Content string
}

// NewReadmeGenerator returns a new readme generator
func NewReadmeGenerator(cf Config) ReadmeGenerator {
	return ReadmeGenerator{cf}
}

// ReadmeGenerator holds all the necessary operations to generate readmes
type ReadmeGenerator struct {
	cf Config
}

func (rg ReadmeGenerator) isValid(fname string, info fs.FileInfo) bool {
	if info.IsDir() {
		fname = fmt.Sprintf("%s/", fname)
	}
	for _, exp := range rg.cf.Scopes {
		if match, _ := regexp.MatchString(exp, fname); match {
			return true
		}
	}
	return false
}

// Generate generates all readmes
func (rg ReadmeGenerator) Generate(root string) error {
	files, err := ioutil.ReadDir(root)
	if err != nil {
		return err
	}
	var fpath string
	var snippets []CodeSnippet

	for _, file := range files {
		fpath = filepath.Join(root, file.Name())
		if !rg.isValid(fpath, file) {
			continue
		}
		if file.IsDir() {
			log.Printf("[DIR] - Subdir %s found", fpath)
			if err = rg.Generate(fpath); err != nil {
				log.Printf("Failed to explore %s folder (%v)", fpath, err)
			}
		} else {
			log.Printf("[File] - Processing %s", fpath)
			ext := filepath.Ext(fpath)
			content, err := ioutil.ReadFile(fpath)
			if err != nil {
				log.Printf("Failed to read file %s : err %v", fpath, err)
				continue
			}
			snippet := CodeSnippet{
				file.Name(),
				rg.cf.Languages[ext],
				string(content),
			}
			snippets = append(snippets, snippet)
		}
	}
	if len(snippets) < 1 {
		return nil
	}
	rdmpath := filepath.Join(root, "README.md")
	fd, err := os.Create(rdmpath)
	if err != nil {
		log.Printf("Failed to create readme file for %s", fpath)
		return err
	}
	defer fd.Close()
	for _, snippet := range snippets {
		tpl, err := template.ParseFiles(rg.cf.Template)
		if err != nil {
			log.Printf("Failed to parse template %s: err (%v)", rg.cf.Template, err)
			os.Remove(rdmpath)
			return err
		}
		if err := tpl.Execute(fd, snippet); err != nil {
			log.Printf("Failed to render template %s: err (%v)", rdmpath, err)
			os.Remove(rdmpath)
			return err
		}
		if _, err := fd.WriteString("\n\n"); err != nil {
			log.Printf("Failed to add sections newlines : err %s", err)
			continue
		}
	}
	return nil
}

func main() {
	cf, err := NewConfig("config.json")
	if err != nil {
		log.Fatalf("Couldn't load config file")
	}
	rg := NewReadmeGenerator(cf)
	err = rg.Generate(".")
	if err != nil {
		log.Printf("%v", err)
		log.Fatal("Execution failed")
	}
}
