import sys
import subprocess
import difflib
import time
import ast
import io
import tokenize
import os

def analyze_script(file_path):
    """
    Analyzes a Python script to count non-blank lines and comment lines
    (including single-line and multi-line comments/docstrings).
    """
    lines_count = 0
    comment_lines = set()

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Count non-blank lines
    for line in content.splitlines():
        if line.strip():
            lines_count += 1

    # 2. Extract comment lines using tokenization (# comments)
    tokens = tokenize.generate_tokens(io.StringIO(content).readline)
    for toktype, tokstring, start, end, line in tokens:
        if toktype == tokenize.COMMENT:
            for l in range(start[0], end[0] + 1):
                comment_lines.add(l)

    # 3. Extract docstrings / multi-line string comments using AST parsing
    try:
        parsed = ast.parse(content)
        for node in ast.walk(parsed):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef, ast.Module)):
                docstring = ast.get_docstring(node, clean=False)
                if docstring:
                    for stmt in node.body if hasattr(node, 'body') else []:
                        if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, str):
                            for l in range(stmt.lineno, stmt.end_lineno + 1):
                                comment_lines.add(l)
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                for l in range(node.lineno, node.end_lineno + 1):
                    comment_lines.add(l)
    except SyntaxError:
        pass

    return lines_count, len(comment_lines)


def run_benchmark(target_script, test_cases, runs=5, delay=3):
    """
    Runs a target script against test cases multiple times and returns the gathered metrics.
    """
    lines_count, comment_lines_count = analyze_script(target_script)

    print("=" * 60)
    print(f"Running tests for: {target_script}")
    print("=" * 60)

    target_executable = [sys.executable, target_script]
    test_results = []

    for tc_idx, test_case in enumerate(test_cases, 1):
        input_file = test_case['input']
        expected_file = test_case['expected']

        with open(input_file, 'r', encoding='utf-8') as f:
            input_data = f.read()

        with open(expected_file, 'r', encoding='utf-8') as f:
            expected_lines = [line.rstrip() for line in f.readlines()]

        print(f"\n--- Test Case {tc_idx} [Input: {input_file} | Expected: {expected_file}] ---")

        run_times = []
        overall_status = "Pass"

        for run in range(1, runs + 1):
            if run > 1:
                time.sleep(delay)

            start_time = time.perf_counter()
            try:
                process = subprocess.run(
                    target_executable,
                    input=input_data,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
            except subprocess.TimeoutExpired:
                print(f"  Run {run}: FAILED (Time Limit Exceeded)")
                overall_status = "Fail"
                continue

            end_time = time.perf_counter()
            execution_time_ms = (end_time - start_time) * 1000
            run_times.append(execution_time_ms)

            actual_lines = [line.rstrip() for line in process.stdout.splitlines()]
            status = "PASSED" if actual_lines == expected_lines else "FAILED"
            
            if status == "FAILED":
                overall_status = "Fail"

            print(f"  Run {run}: {status} | Time: {execution_time_ms:.2f} ms")

            if status == "FAILED" and run == 1:
                print("\n  --- Differences ---")
                diff = difflib.unified_diff(
                    expected_lines, actual_lines,
                    fromfile='Expected', tofile='Actual',
                    lineterm=''
                )
                for line in diff:
                    print(f"  {line}")
                if process.stderr:
                    print("\n  --- Runtime Errors (stderr) ---")
                    print(f"  {process.stderr}")

        test_results.append({
            'input_name': os.path.basename(input_file),
            'status': overall_status,
            'times': run_times
        })

    return {
        'program_name': os.path.basename(target_script),
        'lines_code': lines_count,
        'lines_comment': comment_lines_count,
        'results': test_results
    }


def print_summary(summary_data):
    """
    Prints the final structured summary for all executed programs.
    """
    print("\n" + "=" * 60)
    print("                    FINAL SUMMARY")
    print("=" * 60)

    for prog in summary_data:
        print(f"{prog['program_name']}")
        print(f"Lines of code: {prog['lines_code']}")
        print(f"Comment Lines: {prog['lines_comment']}")

        for test in prog['results']:
            print(f"{test['input_name']}")
            print(f"    |- Status: {test['status']}")

            if test['times']:
                times_str = " ".join([f"{t:.0f} ms" if t.is_integer() else f"{t:.2f} ms" for t in test['times']])
                avg_time = sum(test['times']) / len(test['times'])
                print(f"    |- Execution: {times_str} | AVG: {avg_time:.1f} ms")
            else:
                print(f"    |- Execution: N/A | AVG: N/A")
        print()


def main():
    programs = [
            '../Problems/272-TEX_Quotes/code/claude_haiku4_5.py',
            '../Problems/272-TEX_Quotes/code/claude_opus5_5_medium.py',
            '../Problems/272-TEX_Quotes/code/claude_opus5_medium.py',
            '../Problems/272-TEX_Quotes/code/claude_opus_5_5_max.py',
            '../Problems/272-TEX_Quotes/code/claude_sonnet5_medium.py',
            '../Problems/272-TEX_Quotes/code/gemini3_1_pro.py',
            '../Problems/272-TEX_Quotes/code/gemini3_6_flash.py',
            '../Problems/272-TEX_Quotes/code/gemini3_7_flash.py',
            '../Problems/272-TEX_Quotes/code/gemini3_8_flash.py',
            '../Problems/272-TEX_Quotes/code/gpt_luna_5_6.py',
            '../Problems/272-TEX_Quotes/code/zai_glm_5_3_low.py',
            '../Problems/272-TEX_Quotes/code/zai_glm_5_3_max.py'
        ]

    test_cases = [
        {
            'input': '../Problems/272-TEX_Quotes/inputs_and_outputs/sample_input.txt',
            'expected': '../Problems/272-TEX_Quotes/inputs_and_outputs/sample_output.txt'
        },
        {
            'input': '../Problems/272-TEX_Quotes/inputs_and_outputs/input1.txt',
            'expected': '../Problems/272-TEX_Quotes/inputs_and_outputs/output1.txt'
        },
        {
            'input': '../Problems/272-TEX_Quotes/inputs_and_outputs/input2.txt',
            'expected': '../Problems/272-TEX_Quotes/inputs_and_outputs/output2.txt'
        },
        {
            'input': '../Problems/272-TEX_Quotes/inputs_and_outputs/input3.txt',
            'expected': '../Problems/272-TEX_Quotes/inputs_and_outputs/output3.txt'
        }
    ]

    summary_data = []

    for program in programs:
        prog_summary = run_benchmark(program, test_cases, runs=5, delay=1)
        summary_data.append(prog_summary)

    print_summary(summary_data)


if __name__ == '__main__':
    main()