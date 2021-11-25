package main

import "fmt"

func fizzBuzz(n int) []string {
	ans := []string{}
	for i := 1; i <= n; i++ {
		if i%5 == 0 && i%3 == 0 {
			ans = append(ans, "FizzBuzz")
		} else if i%5 == 0 {
			ans = append(ans, "Buzz")
		} else if i%3 == 0 {
			ans = append(ans, "Fizz")
		} else {
			ans = string(i)
		}
	}
	return ans
}

func main() {
	r := []string{
		"1",
		"2",
		"Fizz",
		"4",
		"Buzz",
		"Fizz",
		"7",
		"8",
		"Fizz",
		"Buzz",
		"11",
		"Fizz",
		"13",
		"14",
		"FizzBuzz",
	}

}
