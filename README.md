[![AlgoData](https://github.com/josuebrunel/algodata/actions/workflows/algodata.yml/badge.svg)](https://github.com/josuebrunel/algodata/actions/workflows/algodata.yml)

## Important patterns to know

From [14 patterns to ace your coding interviews](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)

### 1. Sliding window

The Sliding Window pattern is used to perform a required operation on a specific window size of a given array or linked list, such as finding the longest subarray containing all 1s. Sliding Windows start from the 1st element and keep shifting right by one element and adjust the length of the window according to the problem that you are solving. In some cases, the window size remains constant and in other cases the sizes grows or shrinks.

* The problem input is a linear data structure such as a linked list, array, or string
* You’re asked to find the longest/shortest substring, subarray, or a desired value

```python

    from collections import Counter

    def max_sum_subarray(array, k):
        if not array of k > len(array):
            return 0
        max_sum = 0
        for i in range(k): # defining max sum base line
            max_sum += array[i]
        cur_sum = max_sum
        left, right = 0, k

        while k < len(array):
            # no need to recompute the slice
            # if we want array[i:j] we just remove
            # the starting value (i) then add the ending value (j)
            cur_sum = cur_sum - array[left] + array[right]
            max_sum = max(max_sum, cur_sun)
            left += 1
            right += 1
        return max_sum


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

    def reverse_only_letters(s):
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalpha():
                i += 1
                continue
            if not s[j].isalpha():
                j -= 1
                continue

            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
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

    # O(n) time | O(1) space
    def reorder_list(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break linked list
        half = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while half:
            next_node = half.next
            half.next = prev
            prev = half
            half = next_node
        # reorder the linked list
        fhead, shead = head, prev
        while fhead and shead:
            # save the next of the 2 heads
            fnext = fhead.next
            snext = shead.next
            # fix next values of both heads
            fhead.next = shead
            shead.next = fnext
            # advance
            fhead = fnext
            shead = snext
        return head
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

    def interval_list_intersections(l1, l2):
        res = []
        i = j = 0

        while i < len(l1) and j < len(l2):
            start = max(l1[i][0], l2[j][0])
            end = min(l1[i][1], l2[j][1])
            if start <= end:
                res.append([start, end])
            if l1[i][1] == end:
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

```python

    def cyclic_sort(array):
        """The goal is to put every element in the array
        at its right position according to the relation
        correct_index = array[index] - 1.
        For each element (i) that doesn't meet this relation
        swap with the element at the "correct" index (j = array[i]-1)
        """
        i = 0
        while i < len(array):
            j = array[i] - 1 # correct index
            if array[i] != array[j]:
                array[i], array[j] = array[j], array[i] # swap
            else:
                i += 1
        return array

    def find_missing_number(nums):
        i, length = 0, len(nums)
        # sort the array
        while i < length:
            j = nums[i]
            if nums[i] < length and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # search for value different from its own index
        for i in range(length):
            if i != nums[i]:
                return i
        return length

    def find_duplicate_number(nums):
        i, length = 0, len(nums)
        while i < length:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        # search for the misplaced number
        for i in range(length):
            if nums[i] != i+1:
                return nums[i]
        return -1

    def set_mismatch(nums):
        i, length = 0, len(nums)
        while i < length:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]

        for i in range(length):
            if nums[i] != i+1:
                return [nums[i], i+1]
        return [-1, -1]

    def first_missing_positive(nums):
        i, length = 0, len(nums)
        while i < length:
            j = nums[i] - 1
            if (0 <= j < length) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(length):
            if nums[i] != i+1:
                return i+1
        return length + 1
```

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

```python

    from collections import deque

    def level_order_traversal(root):
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(node)
                queue.append(node.left)
                queue.append(node.right)
            if level:
                res.append(level)
        return res

    def zigzag_order_traversal(root):
        res = []
        queue = deque()
        queue.append(root)
        switch = False
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                level.append(value)
                queue.append(node.left)
                queue.append(node.right)
            if not level:
                continue
            if switch:
                level.reverse()
            res.append(level)
            switch = not switch
        return res
```

### 8. Tree DFS (Depth First Search)

Tree DFS is based on the Depth First Search (DFS) technique to traverse a tree.
You can use recursion (or a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.
The Tree DFS pattern works by starting at the root of the tree, if the node is not a leaf you need to do three things:
1. Decide whether to process the current node now (pre-order), or between processing two children (in-order) or after processing both children (post-order).
2. Make two recursive calls for both the children of the current node to process them.

How to identify the Tree DFS pattern:
* If you’re asked to traverse a tree with in-order, preorder, or postorder DFS
* If the problem requires searching for something where the node is closer to a leaf


```python

    # O(n) time because we have to through all path
    # O(h) space where h is the height of the tree
    # O(n) in worst case
    # O(log(n)) for a balanced tree
    def has_path_sum(root, target):
        if not root:
            return False

        def dfs(node, current_sum):
            if not node:
                return False
            current_sum += node.val
            if node.left and not node.right:
                return current_sum == target
            return dfs(node.left, current_sum, target) or dfs(node.right, current_sum, target)

    return dfs(root, 0, target)

    def path_sum_2(node, target)
        if not root:
            return []
        res = []

        def dfs(node, csum, path):
            if not node:
                return False
            csum += node.val
            if not node.left and not node.right and csum == targetSum:
                path.append(node.val)
                res.append(path.copy())
                path.pop()
                return
            path.append(node.val)
            dfs(node.left, csum, path)
            path.pop()
            path.append(node.val)
            dfs(node.right, csum, path)
            path.pop()

        dfs(root, 0, [])
        return res

    def path_sum_3(node, target):
        if not root:
            return 0

        prefix_sum = {0: 1}

        def dfs(node, cur_sum):
            if not node:
                return 0
            res = 0
            cur_sum += node.val
            if cur_sum - target in prefix_sum:
                res += prefix_sum[cur_sum - target]
            prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
            res = dfs(node.left, cur_sum) + dfs(node.right, cur_sum)
            prefix_sum[cur_sum] -= 1
            return res

        return dfs(root, 0)

    def max_path_sum(root):
        if not root:
            return 0
        res = [float("-inf")]

        def dfs(node):
            if not node:
                return 0
        left_path_sum = max(0, dfs(node.left))
        right_path_sum = max(0, dfs(node.right))
        # compute node sum with a split
        # and update if greater than current max sum
        res[0] = max(res[0], node.val + left_path_sum + right_path_sum)
        # return max sum without a split
        return node.val + max(left_path_sum, right_path_sum)

    dfs(root)
    return res[0]
```

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
    # backtracking template
    def backtrack(Path, Seletion List, Result  ):
        if meet the End Conditon:
            Result.add(Path)
            return

        for seletion in Seletion List:
            select
            backtrack(Path, Seletion List)
            deselect

    # O(n*n^2) time because we have 2 choices at every level: include the current value or not
    # O(2^n) space
    def subsets_ii(nums):
        res = []
        # sort nums to have duplicates in row
        def backtrack(subset, pos):
            if pos == len(nums):
                res.append(subset.copy())
                return

            # all subset with nums[pos]
            subset.append(nums[pos])
            backtrack(subset, pos + 1)
            subset.pop()
            # all without subset with nums[pos]
            backtrack(subset, pos + 1)
            # we remove duplicate
            while pos+1 < len(nums) and nums[pos] == nums[pos+1]:
                pos += 1
            backtrack(subset, pos + 1)

        backtrack([], 0)
        return res

    def unique_permutation(nums):
        res = []
        visited = set()

        def backtrack(subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            for i in nums:
                if i in visited:
                    continue

                visited.add(i)
                subset.append(i)
                backtrack(subset)
                subset.pop()
                visited.remove(i)

        backtrack([])
        return res


    # O(4^n) time where 4 is the max number of letter for 1 digit
    # O(n) space where n is the length of digits
    def letter_combination_phone_number(digits):
        if not digits:
            return []
        keypad = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        # backtrack function
        def backtrack(comb, pos):
            if len(comb) == len(digits):
                res.append("".join(comb.copy()))
            for i in keypad[digits[pos]]:
                comb.append(i)
                backtrack(comb, pos+1)
                comb.pop()

        # initial call
        backtrack([], 0)
        return res

    def combination_sum(elements, target):
        res = []

        def backtrack(pos, comb):
            if sum(comb) > target:
                return
            if pos > len(elements):
                return
            if sum(comb) == target:
                res.append(comb.copy())

            comb.append(elements[pos])
            backtrack(pos, comb)
            comb.pop()
            backtrack(pos+1, comb)

        # initial call
        backtrack(0, [])
        return res
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

    def find_min_in_rotated_array(nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

    def sqrt(x):
        if not x:
            return x
        left , right = 0, x+1
        while left < right:
            mid = left + (right - left) // 2
            val = mid*mid
            if val == x:
                return mid
            elif val < x:
                left = mid+1
            else:
                right = mid
        return left-1
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
    # there is better solution than the one below
    # that solution consists on merging the set of
    # linked list by group of 2. Repeat that process
    # until there's one linked list left
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

```python

    def course_schedule(num, prerequisites): # can finish
        # we build an adjacent list to map each course
        # to its prerequisites
        pre_map = {i: [] for i in range(num)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # we define a list to track the state of the vertex
        # -1 visiting
        # 0 not visited
        # 1 visited
        visit = [0 for _ in range(num)]

        def dfs(crs):
            # if course is in visiting state
            # we have a cycle
            if visit[crs] == -1:
                return False
            # if course already visited
            # no need to go further
            if visit[crs] == 1:
                return True
            # set course in visiting state
            visit[crs] = -1
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            # set course state to visited
            # after exploring its adjacent nodes
            visit[crs] = 1
            return True

        for i in range(num):
            if not dfs(i):
                return False
        return True
```

### 15. Union-Find (DSU - Disjoint Set Union)

Union-Find Data structure can be used to check whether an undirected graph contains cycle or not
So we can use DSU to check if 2 components ( nodes ) are connected to each other directly or
indirectly or determine if tow components are disconnected.
This data structure has 2 operations:
* Union: connects 2 elements
* Find: finds if there is a path between 2 elements

```python

    class DSU:
        def __init__(self, array):
            self.array = array

        def root(self, n):
            while i != self.array[i]:
                # path compression
                self.array[i] = self.array[self.array[i]]
                i = self.array[i]
            return i

        def union(self, a, b):
            root_a = self.root(a)
            root_b = self.root(b)
            self.array[root_a] = root_b

        def find(self, a, b):
            return self.root(a) == self.root(b)
```

### 16. Djikstra

### 17. Prefix Sum

### 18. Monotonic Stack
