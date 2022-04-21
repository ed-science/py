def count_num_in_file(file_path, num):
    count = 0
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            count += count_num_in_tokens(tokens, num)

    return count

def count_num_in_tokens(tokens, num):
    return sum(num == int(token) for token in tokens)


def sum_numbers(file_path):
    output_lines = []
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append(f"sum: {str(total)} | {line}")
    with open(file_path,"w") as f:
        f.writelines(output_lines)

def sum_tokens(tokens):
    return sum(int(token) for token in tokens)

sum_numbers("C:\\Code\\Py\\Basics\\input.txt")