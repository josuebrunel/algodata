[![AlgoData](https://github.com/josuebrunel/algodata/actions/workflows/algodata.yml/badge.svg)](https://github.com/josuebrunel/algodata/actions/workflows/algodata.yml)

## Important patterns to know

From [14 patterns to ace your coding interviews](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

### 1. Sliding window

The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.

* The problem input is a linear data structure such as a linked list, array, or string
* You’re asked to find the longest/shortest substring, subarray, or a desired value

```python

    from collections import Counter

    def length_longest_substring(s):
        if not s:
            return 0
        length = len(s)
        ans = 0
        for i in range(length):
            cword = set()
            j = i
            while j < length and s[j] not in set():
                cword.add(s[j])
                j += 1
            ans = max(ans, j-i)
        return ans

    def find_all_anagrams(s):
        def is_anagram(a, b):
            return Counter(a) == Counter(b)
        ans = []
        i, j = 0, len(j)
        while i+l <= len(s):
            if is_anagram(s[i:i+j]):
                ans.append(i)
            i += 1
        return res
```

### 2. Two pointers (iterator)

Two Pointers is a pattern where two pointers iterate through the data structure in tandem until one or both of the pointers hit a certain condition.Two Pointers is often useful when searching pairs in a sorted array or linked list; for example, when you have to compare each element of an array to its other elements.

Ways to identify when to use the Two Pointer method:

* It will feature problems where you deal with sorted arrays (or Linked Lists) and need to find a set of elements that fulfill certain constraints
* The set of elements in the array is a pair, a triplet, or even a subarray

```python

    def three_sum(nums, target):
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # 2 pointers l and r
            l, r = i+1, len(nums) - 1
            while l < r:
                csum = nums[i] + nums[l] + nums[r]
                if csum > 0:
                    r -= 1
                elif csum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] < nums[l-1] and l < r:
                        l += 1
        return res
```

### 3. Fast and slow pointers

The Fast and Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/linked list) at different speeds. This approach is quite useful when dealing with cyclic linked lists or arrays.
By moving at different speeds (say, in a cyclic linked list), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

How do you identify when to use the Fast and Slow pattern?
* The problem will deal with a loop in a linked list or array
* When you need to know the position of a certain element or the overall length of the linked list.

```python

    def has_cycle(head):
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    # O(n) time | O(1) space
    def is_palindromic(head):
        slow = fast = head
        # finding the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reversing half of the linked list
        middle = None
        while slow:
            next_node = slow.next
            slow.next = middle
            midle = slow
            slow = next_node
        # comparing both half of the linked list
        print(middle, fast)
        while middle:
            if middle.val != fast.val:
                return False
            middle = middle.next
            fast = fast.next
        return True
```

### 4. Merge Intervals

The Merge Intervals pattern is an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, you either need to find overlapping intervals or merge intervals if they overlap. The pattern works like this:
Given two intervals (‘a’ and ‘b’), there will be six different ways the two intervals can relate to each other:
1. *a* and *b* do not overlap e.g \[[1, 3], [5, 7]]
2. *a* and *b* overlap and *b* ends after *a* e.g \[[1,3], [2,5]]
3. *a* completely overlap *b* e.g \[[1, 4], [2,3]]
4. *a* and *b* overlap and *a* ends after *b* e.g \[[3,5], [1, 4]]
5. *b* completely overlap *a* e.g \[[3, 6], [4,5]]
6. *a* and *b* do not overlap \[[1, 3], [4,5]]

How do you identify when to use the Merge Intervals pattern?
* If you’re asked to produce a list with only mutually exclusive intervals
* If you hear the term “overlapping intervals”.

```python

    def interval_intersections(l1, l2):
        res = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start, end])
            if firstList[i][1] == end:
                i += 1
            else:
                j += 1
        return res
```

### 5. Cyclic sort

This pattern describes an interesting approach to deal with problems involving arrays containing numbers in a given range. The Cyclic Sort pattern iterates over the array one number at a time, and if the current number you are iterating is not at the correct index, you swap it with the number at its correct index.

How do I identify this pattern?
* They will be problems involving a sorted array with numbers in a given range
* If the problem asks you to find the missing/duplicate/smallest number in an sorted/rotated array

### 6. In-place reversal linked list

In a lot of problems, you may be asked to reverse the links between a set of nodes of a linked list. Often, the constraint is that you need to do this in-place, i.e., using the existing node objects and without using extra memory. This is where the above mentioned pattern is useful.
This pattern reverses one node at a time starting with one variable (current) pointing to the head of the linked list, and one variable (previous) will point to the previous node that you have processed. In a lock-step manner, you will reverse the current node by pointing it to the previous before moving on to the next node. Also, you will update the variable “previous” to always point to the previous node that you have processed.

How do I identify when to use this pattern:
* If you’re asked to reverse a linked list without using extra memory

```python
    def reverse(head):
        node = head
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev

    def reverse_sub_linked_list(head, left, right):
        dummy = ListNode(0, head)
        left_prev, cur = dummy, head
        for _ in range(left-1):
            left_prev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        left_prev.next.next = cur
        left_prev.next = prev
        return dummy.next
```

### 7. Tree BFS (Breadth First Search)

This pattern is based on the Breadth First Search (BFS) technique to traverse a tree and uses a queue to keep track of all the nodes of a level before jumping onto the next level. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach.
The Tree BFS pattern works by pushing the root node to the queue and then continually iterating until the queue is empty. For each iteration, we remove the node at the head of the queue and “visit” that node. After removing each node from the queue, we also insert all of its children into the queue.

How to identify the Tree BFS pattern:
* If you’re asked to traverse a tree in a level-by-level fashion (or level order traversal)

### 8. Tree DFS (Depth First Search)

Tree DFS is based on the Depth First Search (DFS) technique to traverse a tree.
You can use recursion (or a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.
The Tree DFS pattern works by starting at the root of the tree, if the node is not a leaf you need to do three things:
1. Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order).
2. Make two recursive calls for both the children of the current node to process them.

How to identify the Tree DFS pattern:
* If you’re asked to traverse a tree with in-order, preorder, or postorder DFS
* If the problem requires searching for something where the node is closer to a leaf

### 9. Two Heaps

In many problems, we are given a set of elements such that we can divide them into two parts. To solve the problem, we are interested in knowing the smallest element in one part and the biggest element in the other part. This pattern is an efficient approach to solve such problems.
This pattern uses two heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element. The pattern works by storing the first half of numbers in a Max Heap, this is because you want to find the largest number in the first half. You then store the second half of numbers in a Min Heap, as you want to find the smallest number in the second half. At any time, the median of the current list of numbers can be calculated from the top element of the two heaps.

Ways to identify the Two Heaps pattern:
* Useful in situations like Priority Queue, Scheduling
* If the problem states that you need to find the smallest/largest/median elements of a set
* Sometimes, useful in problems featuring a binary tree data structure

### 10. Subset

A huge number of coding interview problems involve dealing with Permutations and Combinations of a given set of elements. The pattern Subsets describes an efficient Breadth First Search (BFS) approach to handle all these problems.
Mainly problems you can solve with backtracking. Think about **decision tree** to find the different conditions and constraints

How to identify the Subsets pattern:
* Problems where you need to find the combinations or permutations of a given set

```python
    def problem(subset):
        res = []
        backtrack(subset, 0, step, res)
        return res

    def backtrack(subset, start, step, res):
        if condition == ok:
            res.append(step.copy())

        for set in subset:
            step.append(set)
            backtrack(subset, start + 1)
            step.pop()
```

### 11. Modified binary search

Whenever you are given a sorted array, linked list, or matrix, and are asked to find a certain element, the best algorithm you can use is the Binary Search. This pattern describes an efficient way to handle all problems involving Binary Search.
The patterns looks like this for an ascending order set:
1. First, find the middle of start and end. An easy way to find the middle would be: middle = (start + end) / 2. But this has a good chance of producing an integer overflow so it’s recommended that you represent the middle as: middle = start + (end — start) / 2
2. If the key is equal to the number at index middle then return middle
3. If ‘key’ isn’t equal to the index middle:
4. Check if key < arr[middle]. If it is reduce your search to end = middle — 1
5. Check if key > arr[middle]. If it is reduce your search to end = middle + 1

```python
    def binary_search(array, target):
        left, right = 0, len(array) - 1
        while left < right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            elif target > array[right]:
                left = mid + 1
            else:
                right = mid
        return -1
```

### 12. Top K elements

Any problem that asks us to find the top/smallest/frequent ‘K’ elements among a given set falls under this pattern.
The best data structure to keep track of ‘K’ elements is Heap. This pattern will make use of the Heap to solve multiple problems dealing with ‘K’ elements at a time from a set of given elements. The pattern looks like this:
1. Insert ‘K’ elements into the min-heap or max-heap based on the problem.
2. Iterate through the remaining numbers and if you find one that is larger than what you have in the heap, then remove that number and insert the larger one.
There is no need for a sorting algorithm because the heap will keep track of the elements for you.

How to identify the Top ‘K’ Elements pattern:
* If you’re asked to find the top/smallest/frequent ‘K’ elements of a given set
* If you’re asked to sort an array to find an exact element

```python
    import heapq

    def kth_largest(nums, k):
        if len(nums) == 1:
            return nums[0]

        minheap = []
        for i in nums[:k]:
            heapq.heappush(minheap, i)

        for i in nums[k:]:
            if i > minheap[0]:
                heapq.heappop(minheap)
                heapq.heappush(minheap, i)
        return minheap[0]
```

### 13. K-way Merge

K-way Merge helps you solve problems that involve a set of sorted arrays.
Whenever you’re given ‘K’ sorted arrays, you can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays. You can push the smallest element of each array in a Min Heap to get the overall minimum. After getting the overall minimum, push the next element from the same array to the heap. Then, repeat this process to make a sorted traversal of all elements.
The pattern looks like this:
1. Insert the first element of each array in a Min Heap.
2. After this, take out the smallest (top) element from the heap and add it to the merged list.
3. After removing the smallest element from the heap, insert the next element of the same list into the heap.
4. Repeat steps 2 and 3 to populate the merged list in sorted order.

How to identify the K-way Merge pattern:
* The problem will feature sorted arrays, lists, or a matrix
* If the problem asks you to merge sorted lists, find the smallest element in a sorted list.

```python
    # there are better though
    def merge_k_sorted_list(lists):
        merged = []
        min_heap = []
        for i in lists:
            for j in i:
                heapq.heappush(min_heap, j)

        while min_heap:
            merged.append(heapq.heappop(min_heap))
        return merged
```

### 14. Topological sort

Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if event ‘B’ is dependent on event ‘A’, ‘A’ comes before ‘B’ in topological ordering.
This pattern defines an easy way to understand the technique for performing topological sorting of a set of elements.
The pattern works like this:
1. Store the graph in adjacency lists by using a HashMap then find all sources by using a HashMap to keep the count of in-degreesBuild the graph and find in-degrees of all vertices
2. Build the graph from the input and populate the in-degrees HashMap.
3. Find all sources. All vertices with ‘0’ in-degrees will be sources and are stored in a Queue.
4. Sort: For each source, do the following things:
    a. Add it to the sorted list.
    b. Get all of its children from the graph
    c. Decrement the in-degree of each child by 1
    d. If a child’s in-degree becomes ‘0’, add it to the sources Queue
    e. Repeat until the source Queue is empty.

How to identify the Topological Sort pattern:
* The problem will deal with graphs that have no directed cycles
* If you’re asked to update all objects in a sorted order
* If you have a class of objects that follow a particular order

