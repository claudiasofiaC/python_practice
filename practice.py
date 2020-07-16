# given a string and a non-neg int n, return a larger sting that is n copies of the original string

def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str
    return result

print(string_times(3))
