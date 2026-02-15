# Demo Questions for Small Models
**Models:** `qwen2.5-coder:7b-instruct` (Generator) + `qwen2.5:7b-instruct` (Reviewer/Planner)

## ⚠️ Important Notes 

These questions are specifically selected for **small LLM models** (1.5B-1.7B parameters). They:
- ✅ Are simple enough for small models to generate correctly
- ✅ Match techniques available in the database
- ✅ Have clear, straightforward solutions
- ✅ Avoid complex graph/algorithm logic that small models struggle with

---

## 🟢 **EASY - Best for Demos (Highly Recommended)**

### 1. **Prime Number Check** ⭐ RECOMMENDED
```
Write a program to check if a number is prime or not
```
**Database Technique:** Array Traversal & State Simulation  
**Why it works:** Simple iteration, small models handle this well  
**Expected Output:** Clean prime checking algorithm

---

### 2. **Two Sum with Hash Map** ⭐ RECOMMENDED
```
Find two numbers in an array that sum to a target value using hash map
```
**Database Technique:** Hash-Based Indexing  
**Why it works:** Simple hash map usage, clear logic  
**Expected Output:** Correct O(n) solution with dictionary

---

### 3. **Binary Search** ⭐ RECOMMENDED
```
Implement binary search to find target element in a sorted array
```
**Database Technique:** Binary Search on Sorted Data  
**Why it works:** Well-known algorithm, small models know this  
**Expected Output:** Correct binary search implementation

---

### 4. **Fibonacci with Memoization** ⭐ RECOMMENDED
```
Calculate fibonacci numbers using memoization
```
**Database Technique:** Dynamic Programming – Memoization  
**Why it works:** Simple DP pattern, recursive + cache  
**Expected Output:** Correct memoized Fibonacci

---

### 5. **Remove Duplicates from Sorted Array**
```
Remove duplicates from a sorted array using two pointers
```
**Database Technique:** Two Pointers (Converging)  
**Why it works:** Simple two-pointer logic  
**Expected Output:** In-place duplicate removal

---

### 6. **Maximum Subarray Sum (Kadane's Algorithm)**
```
Find the maximum sum of contiguous subarray
```
**Database Technique:** Dynamic Programming – Tabulation  
**Why it works:** Classic DP problem, small models can handle  
**Expected Output:** Kadane's algorithm implementation

---

### 7. **Find First Non-Repeating Character**
```
Find the first non-repeating character in a string using hash map
```
**Database Technique:** Hash-Based Indexing  
**Why it works:** Simple character frequency counting  
**Expected Output:** Hash map solution with frequency tracking

---

### 8. **Check Palindrome**
```
Check if a string is a palindrome using two pointers
```
**Database Technique:** Two Pointers (Converging)  
**Why it works:** Very simple two-pointer comparison  
**Expected Output:** Clean palindrome checker

---

### 9. **Factorial Calculation**
```
Calculate factorial of a number using recursion
```
**Database Technique:** Recursion with Controlled Depth  
**Why it works:** Basic recursion, small models handle well  
**Expected Output:** Recursive factorial function

---

### 10. **Reverse String**
```
Reverse a string in-place using two pointers
```
**Database Technique:** Two Pointers (Converging)  
**Why it works:** Extremely simple, guaranteed to work  
**Expected Output:** String reversal with two pointers

---

## 🟡 **MEDIUM - Good for Demos**

### 11. **Longest Common Subsequence (LCS)**
```
Find the longest common subsequence between two strings using dynamic programming
```
**Database Technique:** Dynamic Programming – Tabulation   -------------->
**Why it works:** Classic DP, well-documented algorithm  
**Note:** May need retries, but usually works

---

### 12. **Sliding Window Maximum**
```
Find maximum element in all subarrays of size k using sliding window
```
**Database Technique:** Sliding Window (Fixed & Dynamic)  ---------------->
**Why it works:** Moderate complexity, uses deque/queue  
**Note:** Check if output is optimized

---

### 13. **Group Anagrams**
```
Group anagrams together using hash map
```
**Database Technique:** Hash-Based Indexing  
**Why it works:** String sorting + hash map  
**Expected Output:** Anagram grouping with sorted keys

---

### 14. **Valid Parentheses**
```
Check if a string contains valid parentheses using stack
```
**Database Technique:** Monotonic Stack Pattern  
**Why it works:** Simple stack operations  
**Expected Output:** Stack-based validation

---

### 15. **Find Peak Element**
```
Find a peak element in an array using binary search
```
**Database Technique:** Binary Search on Sorted Data  
**Why it works:** Binary search variant, moderate complexity  
**Note:** May need verification

---

### 16. **Product of Array Except Self**
```
Calculate product of all elements except self for each element
```
**Database Technique:** Prefix Sum Aggregation  
**Why it works:** Prefix/suffix product pattern  
**Expected Output:** O(n) solution with prefix products

---

### 17. **Find Majority Element**
```
Find the majority element in an array using Boyer-Moore voting algorithm
```
**Database Technique:** Boyer-Moore Voting Algorithm  
**Why it works:** Simple voting algorithm  
**Expected Output:** O(1) space solution

---

### 18. **Climbing Stairs**
```----------->
```
Calculate number of ways to climb n stairs (can climb 1 or 2 steps at a time) 
**Database Technique:** Dynamic Programming – Tabulation  
**Why it works:** Simple DP, Fibonacci variant  
**Expected Output:** DP solution

---

### 19. **Reverse Linked List**
```
Reverse a linked list iteratively---------------------->
```
**Database Technique:** Array Traversal & State Simulation  
**Why it works:** Simple pointer manipulation  
**Expected Output:** Iterative reversal

---

### 20. **Longest Substring Without Repeating Characters**
```
Find the longest substring without repeating characters using sliding window
```
**Database Technique:** Sliding Window (Fixed & Dynamic)  
**Why it works:** Sliding window + hash map  
**Note:** May need optimization check

---

## 🔴 **AVOID - Too Complex for Small Models**

These questions are **NOT recommended** for small models as they often produce incorrect code:

❌ **Cycle Detection in Directed Graph**
- Too complex, models mix up directed/undirected logic
- Parent tracking doesn't work for directed graphs

❌ **Strongly Connected Components (SCC)**
- Complex graph algorithm
- Requires Kosaraju/Tarjan algorithms

❌ **Shortest Path (Dijkstra/Bellman-Ford)**
- Complex graph algorithms
- Edge cases hard for small models

❌ **Advanced Tree Problems (LCA, Segment Tree)**
- Complex tree algorithms
- Small models struggle with tree manipulation

❌ **Complex String Algorithms (KMP, Rabin-Karp)**
- Advanced pattern matching
- Failure function calculation is complex

❌ **Advanced DP (State Compression, Bitmask DP)**
- Complex state representation
- Small models can't handle bit manipulation DP

❌ **Network Flow Algorithms**
- Very complex graph algorithms
- Multiple concepts to combine

---

## 📊 **Quick Reference Table**

| Question | Database Technique | Difficulty | Success Rate |
|----------|-------------------|------------|--------------|
| Prime number check | Array Traversal | Easy | ✅ 95% |
| Two sum with hash | Hash-Based Indexing | Easy | ✅ 90% |
| Binary search | Binary Search | Easy | ✅ 95% |
| Fibonacci memoized | DP Memoization | Easy | ✅ 90% |
| Remove duplicates | Two Pointers | Easy | ✅ 90% |
| Max subarray sum | DP Tabulation | Easy | ✅ 85% |
| LCS | DP Tabulation | Medium | ✅ 75% |
| Sliding window max | Sliding Window | Medium | ⚠️ 70% |
| Valid parentheses | Stack Pattern | Medium | ✅ 85% |
| Peak element | Binary Search | Medium | ⚠️ 70% |

---

## 🎯 **Top 5 Questions for Professor Demo**

1. **"Find two numbers in an array that sum to a target value using hash map"**
   - Shows: Hash-Based Indexing from database
   - Simple, guaranteed to work
   - Clear output

2. **"Implement binary search to find target element in a sorted array"**
   - Shows: Binary Search from database
   - Classic algorithm, always correct
   - Demonstrates technique retrieval

3. **"Calculate fibonacci numbers using memoization"**
   - Shows: Dynamic Programming – Memoization from database
   - Simple DP pattern
   - Shows database integration

4. **"Write a program to check if a number is prime or not"**
   - Simple algorithm
   - Shows basic problem solving
   - Always generates correct code

5. **"Remove duplicates from a sorted array using two pointers"**
   - Shows: Two Pointers technique from database
   - Clean, simple solution
   - Demonstrates in-place operations

---

## 🔍 **How to Verify Database Retrieval**

When running these questions, check the output for:

1. **Database Indicator:**
   ```
   📊 Techniques fetched from database
   X technique(s) retrieved
   • [Technique Name 1]
   • [Technique Name 2]
   ...
   ```

2. **Planner Logs:**
   ```
   [PLANNER] Retrieved X techniques from database
   ```

3. **Plan Section:**
   - Should mention the technique name
   - Should reference database technique details

---

## 💡 **Tips for Best Demo Experience**

1. **Start with Easy Questions** - Build confidence first
2. **Show Database Indicator** - Highlight the "fetched from database" badge
3. **Explain the Workflow** - Show multi-agent process
4. **Mention Model Limitations** - Be transparent about small models
5. **Emphasize Architecture** - Focus on system design, not just correctness

---

## 📝 **Notes**

- All questions above match techniques in `memory/TECHNIQUES.py`
- Small models (1.5B-1.7B) work best with simple, well-known algorithms
- Complex graph/string algorithms often fail with small models
- Focus on showcasing the **multi-agent architecture** rather than perfect code for all problems
- Database retrieval works for all questions listed above

---

**Last Updated:** Based on testing with `yi-coder:1.5b` and `smollm2:1.7b` models
