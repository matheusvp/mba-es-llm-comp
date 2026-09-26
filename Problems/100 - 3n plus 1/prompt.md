# UVa 100 - The 3n + 1 Problem

Write a complete, standalone program in [INSERT LANGUAGE HERE] to solve "The 3n + 1 Problem". Do not use any external libraries or frameworks; rely only on the standard library.

**Objective:**
Given a series of pairs of integers `i` and `j`, determine the maximum cycle length over all integers between and including `i` and `j` using the Collatz algorithm, and print the results.

**Algorithm:**
Consider the following sequence generation for an integer `n`:
1. `n` is the first number in the sequence.
2. If `n = 1` then STOP.
3. If `n` is odd then `n = 3n + 1`.
4. Else (if `n` is even) `n = n / 2`.
5. Repeat from step 2.

The "cycle length" of `n` is the total count of numbers generated in this sequence up to and including the final 1. (For example, the sequence for 22 has 16 numbers in it, so its cycle length is 16).

**Critical Edge Cases (Must Handle):**
1. **Unordered Inputs:** The input pairs `i` and `j` are NOT guaranteed to be in ascending order. `i` may be greater than `j`. You must evaluate all numbers between the two (inclusive), but you must correctly identify the lower and upper bounds before looping.
2. **Output Order Preservation:** The output must print the original `i` and `j` in the *exact same order they were given in the input*, followed by the maximum cycle length found. (e.g., if the input is `10 1`, the output must be `10 1 20`).
3. **Continuous Input:** The input may contain any number of lines. Your program must continue reading and processing pairs until the End-of-File (EOF) is reached.

**I/O Constraints:**
* Read dynamically from standard input (stdin) until EOF.
* Do not use hardcoded file paths. 
* Output exactly to standard output (stdout).
* You can assume all input integers will be greater than 0 and less than 1,000,000. 
* You can assume that no intermediate operation overflows a standard 32-bit integer.

**Output Format:**
For each pair of input integers `i` and `j`, output `i`, `j`, and the maximum cycle length. These three numbers must be separated by exactly one space, with one line of output for each line of input.

Return only the raw, runnable code. Do not include markdown explanations, tutorials, or setup instructions.