# UVa 101 - The Blocks Problem

Write a complete, standalone program in Python to solve the "Blocks Problem". Do not use any external libraries or frameworks; rely only on the standard library.

**Objective:**
Parse standard input (stdin) commands to simulate a robotic arm manipulating blocks on a table, and output the final state of the table to standard output (stdout). 

**State Setup:**
Read an integer `n` (where 0 < n < 25) from the first line of input. This represents `n` blocks numbered `0` to `n-1`, and `n` initial positions numbered `0` to `n-1`. Initially, block `i` rests at position `i`.

**Commands to Implement:**
Parse the subsequent lines until the command `quit` is reached. The commands will follow these four patterns (where `a` and `b` are block numbers):

1. `move a onto b`: Returns any blocks stacked on top of block `a` and block `b` to their initial positions. Then puts block `a` directly on top of block `b`.
2. `move a over b`: Returns any blocks stacked on top of block `a` to their initial positions. Then puts block `a` on top of the stack containing block `b`.
3. `pile a onto b`: Returns any blocks stacked on top of block `b` to their initial positions. Then puts block `a` and all blocks stacked above it directly onto block `b` (maintaining their original vertical order).
4. `pile a over b`: Puts block `a` and all blocks stacked above it onto the top of the stack containing block `b` (maintaining their original vertical order).

**Critical Edge Cases (Must Handle):**
Any command where `a == b` OR where block `a` and block `b` are already in the same stack is an **illegal command**. Your program must silently ignore illegal commands and proceed to the next line without modifying the state.

**I/O Constraints:**
* Read dynamically from standard input (stdin) until EOF or `quit`.
* Do not use hardcoded file paths. 
* Output exactly to standard output (stdout).

**Output Format:**
Upon receiving the `quit` command, print the final state of the blocks. Print one line for each position `i` from `0` to `n-1`, formatted exactly as:
`i: block1 block2 ...`

Note: There must be a single space after the colon if there are blocks at that position, and single spaces separating each block number. If a position is empty, print just `i:` with no trailing spaces.

Return only the raw, runnable code. Do not include markdown explanations, tutorials, or setup instructions.