def merge_the_tools(string, k):
    for i in range(k):
        u = string[i*k:(i+1)*k]
        list_of_chars = list(u)
        output_string = "".join(list(dict.fromkeys(list_of_chars)))
        print(output_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
