from pathlib import Path
import sys


def remove_duplicate_lines(input_path_str: str) -> None:
    input_path = Path(input_path_str)

    if not input_path.is_file():
        print(f"Error: File not found at '{input_path}'")
        sys.exit(1)

    # Construct the output file path in the same directory
    output_path = input_path.with_name(
        f"{input_path.stem}_clean{input_path.suffix}"
    )

    seen_lines = set()

    with open(input_path, "r", encoding="utf-8") as infile, open(
        output_path, "w", encoding="utf-8"
    ) as outfile:
        for line in infile:
            if line not in seen_lines:
                seen_lines.add(line)
                outfile.write(line)

    print(f"Deduplicated file saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_txt_file>")
        sys.exit(1)

    file_argument = sys.argv[1]
    remove_duplicate_lines(file_argument)