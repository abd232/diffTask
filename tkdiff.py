from difflib import Differ
def tkdiffMethod(first_file, second_file):
    with open(first_file) as f:
        file1_lines = f.readlines()
    with open(second_file) as f:
        file2_lines = f.readlines()
    d = Differ()
    return d.compare(file1_lines, file2_lines)

