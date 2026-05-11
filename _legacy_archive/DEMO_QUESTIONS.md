# Demo Questions for Database Retrieval

## Questions That Will Trigger Database Techniques

The database contains 30+ DSA techniques. To see database retrieval in action, use questions that match these technique keywords:

### 1. **Binary Search Questions** ✅
```
Find the target element in a sorted array using binary search
Implement binary search to find the first occurrence of a number
Use binary search to find the peak element in an array
```

### 2. **Two Pointers Questions** ✅
```
Find two numbers in a sorted array that sum to a target
Remove duplicates from a sorted array using two pointers
Merge two sorted arrays using two pointers
```

### 3. **Sliding Window Questions** ✅
```
Implement a rate limiter using sliding window
Find the maximum sum of a subarray of size k
Find the longest substring without repeating characters
```

### 4. **Hash/Dictionary Questions** ✅
```
Find two numbers that sum to target using hash map
Group anagrams using hash map
Find the first non-repeating character using hash map
```

### 5. **Dynamic Programming Questions** ✅
```
Find the longest common subsequence using dynamic programming
Calculate fibonacci numbers using memoization
Find the minimum path sum in a grid using DP
```

### 6. **Graph Questions** ✅
```
Find shortest path in an unweighted graph using BFS
Detect cycle in a directed graph using DFS
Find all connected components in a graph
```

### 7. **Tree Questions** ✅
```
Traverse a binary tree in-order
Find the lowest common ancestor in a binary tree
Validate if a binary tree is a BST
```

## Best Demo Question (Recommended)

**For maximum database retrieval, use:**

```
Implement a rate limiter using sliding window algorithm
```

**Why this works:**
- Matches "Sliding Window" technique
- Matches "Rate limiting" use case
- Will retrieve multiple relevant techniques
- Shows database integration clearly

## Alternative Good Questions

1. **"Find two numbers in a sorted array that sum to target using two pointers"**
   - Will retrieve: Two Pointers technique

2. **"Implement binary search to find target in sorted array"**
   - Will retrieve: Binary Search technique

3. **"Find longest common subsequence using dynamic programming"**
   - Will retrieve: Dynamic Programming techniques

## Simple Questions (May Not Retrieve)

These simple questions might NOT retrieve techniques:
- "Write a program to check if a number is prime" (too simple, no specific technique)
- "Print hello world" (no algorithm)
- "Calculate factorial" (basic recursion, may not match)

## How to Verify Database Retrieval

When you run a question that matches database techniques, you should see:
```
[PLANNER] Retrieved X techniques from database
```

In the output, you'll see:
- **DSA Techniques Retrieved from Database** section with technique details
- Techniques will be shown in the plan

## Database Status

To ensure database is working:
1. Run: `python3 -m memory.seed_techniques`
2. Check: `memory/techniques_db/` directory exists
3. Verify: Database has 30+ techniques loaded
