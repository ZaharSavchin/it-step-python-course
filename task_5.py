def split_by_index(s, indexes):
    result = []
    words = []
    counter = 0
    for i in s:
        if counter < len(indexes):
            if i != s[indexes[counter]]:
                words.append(i)
            else:
                result.append("".join(words))
                words.clear()
                words.append(i)
                counter = counter + 1
        else:
            words.append(i)
    result.append("".join(words))
    return result

s = 'pythoniscool,isn`tit?'
indexes = [6, 8, 12, 13, 18]
print(split_by_index(s, indexes))
