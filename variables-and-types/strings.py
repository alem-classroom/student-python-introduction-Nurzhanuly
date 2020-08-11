def size_of_str(str):
    return len(str)

def concat_strings(first, second):
    return first + second

def duplicate_string(str, copy):
    return str * copy

def reverse(str):
    return str [::-1]

def is_substring(str, substr):
    if str in substr:
        return True
    else:
        return False
