import sys
import subprocess
import difflib

def run_benchmark(target_executable, input_file, expected_file):
    # 1. Read the input data
    with open(input_file, 'r', encoding='utf-8') as f:
        input_data = f.read()

    # 2. Read the expected output and strip trailing whitespaces
    # (Crucial for UVa problems to avoid \r\n vs \n OS mismatch failures)
    with open(expected_file, 'r', encoding='utf-8') as f:
        expected_lines = [line.rstrip() for line in f.readlines()]

    print(f"Running {' '.join(target_executable)}...")

    # 3. Execute the LLM's code and pass the input data via stdin
    try:
        process = subprocess.run(
            target_executable,
            input=input_data,
            capture_output=True,
            text=True,
            timeout=10 # Prevents infinite loops (Time Limit Exceeded)
        )
    except subprocess.TimeoutExpired:
        print("FAILED: Time Limit Exceeded (Infinite Loop)")
        return

    # 4. Process the LLM's actual output
    actual_lines = [line.rstrip() for line in process.stdout.splitlines()]

    # 5. Compare the results
    if actual_lines == expected_lines:
        print("PASSED: The LLM's output matches the uDebug data exactly.")
    else:
        print("FAILED: Output differs.")
        print("\n--- Differences ---")
        # Generate a visual diff showing exactly where the LLM failed
        diff = difflib.unified_diff(
            expected_lines, actual_lines, 
            fromfile='Expected (uDebug)', tofile='Actual (LLM)', 
            lineterm=''
        )
        for line in diff:
            print(line)

        # Print any runtime errors (e.g., Python tracebacks)
        if process.stderr:
            print("\n--- Runtime Errors (stderr) ---")
            print(process.stderr)

if __name__ == '__main__':
    # Command line argument order:
    # Usage: python tester.py [llm_script.py] [input.txt] [output.txt]
    llm_script = sys.argv[1] if len(sys.argv) > 1 else 'llm_code.py'
    input_txt = sys.argv[2] if len(sys.argv) > 2 else 'input.txt'
    expected_txt = sys.argv[3] if len(sys.argv) > 3 else 'output.txt'

    # Command to run the target script using Python
    command = ['python', llm_script]

    run_benchmark(command, input_txt, expected_txt)