# UVa 272 - TEX Quotes

Write a complete, standalone program in [INSERT LANGUAGE HERE] to solve the "TEX Quotes" problem. Do not use any external libraries or frameworks; rely only on the standard library.

**Objective:**
Read a raw text input and replace all standard double-quote characters (`"`) with LaTeX-style directional quotes. 

**Algorithm:**
* Replace the first `"` in each pair with two left-single-quotes (backticks): ` `` `
* Replace the second `"` in each pair with two right-single-quotes (apostrophes): ` '' `
* This replacement alternates continuously throughout the entire input text. You can assume that the text will contain an even number of double-quote characters. Nested quotations do not occur.

**Critical Edge Cases (Must Handle):**
1. **Global State Across Lines:** A quotation might begin on one line and end on a completely different line. Your state tracking whether a quote is currently "open" or "closed" MUST persist across line breaks. Do not reset your open/close flag at the end of a line.
2. **Whitespace and Formatting Preservation:** Every single character that is not a double-quote (including spaces, tabs, empty lines, and other punctuation) must be output exactly as it was input. 
3. **Continuous Input:** The input may contain any number of lines. Your program must continue reading and processing text until the End-of-File (EOF) signal is reached.

**I/O Constraints:**
* Read dynamically from standard input (stdin) until EOF.
* Do not use hardcoded file paths. 
* Output exactly to standard output (stdout).

**Output Format:**
Output the exact same text as the input, with the only modification being the replaced double-quotes as described above.

Return only the raw, runnable code. Do not include markdown explanations, tutorials, or setup instructions.