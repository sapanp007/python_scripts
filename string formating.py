import re


def replace_number_with_letter(data):
    match = data.group(0)
    letters = re.search(r"[a-zA-Z]+", match).group()
    number = int(re.search(r"\d+", match).group())
    return letters * number


def format_string(string_data):
    pattern = re.compile(r"(\d+\[[a-zA-Z]+\])")
    string_data = re.sub(pattern, replace_number_with_letter, string_data)
    if string_data.find("[") > 0:
        return format_string(string_data)
    else:
        return string_data


if __name__ == "__main__":
    str1 = "10[abc]3[cd]ef"
    print(format_string(str1))
