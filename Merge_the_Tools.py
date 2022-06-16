def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        line = string[i:i+k]
        new = ""
        for j in line:
            if j not in new:
                new+=j
        print(new)
