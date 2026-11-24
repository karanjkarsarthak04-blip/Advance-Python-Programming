"""Question 8: Count lines and write the first two lines to a new file."""


def process_file(input_name, output_name):
    with open(input_name, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    with open(output_name, "w", encoding="utf-8") as output_file:
        output_file.writelines(lines[:2])

    return len(lines)


if __name__ == "__main__":
    input_file_name = input("Enter input file name: ").strip()
    output_file_name = input("Enter output file name: ").strip()
    try:
        line_count = process_file(input_file_name, output_file_name)
        print("Total number of lines:", line_count)
        print(f"First two lines written to '{output_file_name}'.")
    except FileNotFoundError:
        print("Input file not found.")
