num_iterations = int(input())
l_in = ['#', '.', '.', '.', '.', '#']
l_in.insert(0, '.')
l_in.append('.')
res = []
for n in range(num_iterations):
    for i in range(1, len(l_in) - 1):
        if l_in[i] == '#' and (l_in[i - 1] == '#' and l_in[i + 1] == '#') or (l_in[i - 1] == '.' and l_in[i + 1] == '.'):
            res.append('.')
            continue
        if l_in[i] == '.' and (l_in[i - 1] == '#' or l_in[i + 1] == '#'):
            res.append('#')
            continue
        if l_in[i - 1] == '.' and l_in[i + 1] == '#':
            res.append('#')
            continue
        if l_in[i - 1] == '#' and l_in[i + 1] == '.':
            res.append('#')
            continue
        else:
            res.append(l_in[i])
print(res)






s_ = ".##..#..#.#."

# print(dead_alive(s_))

