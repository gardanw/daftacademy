import sys


def max_path(rows):
    paths = [[[] for _ in w] for w in rows]
    for i in range(len(rows[-1])):
        paths[-1][i].append(str(rows[-1][i]))

    for w in range(len(rows) - 2, -1, -1):
        for c in range(len(rows[w])):
            if rows[w + 1][c] > rows[w + 1][c + 1]:
                next_to_add = c

                for p in paths[w + 1][next_to_add]:
                    paths[w][c].append(str(rows[w][c]) + p)

                rows[w][c] += rows[w + 1][next_to_add]
            elif rows[w + 1][c] < rows[w + 1][c + 1]:
                next_to_add = c + 1

                for p in paths[w + 1][next_to_add]:
                    paths[w][c].append(str(rows[w][c]) + p)

                rows[w][c] += rows[w + 1][next_to_add]
            elif rows[w + 1][c] == rows[w + 1][c + 1]:

                for p in paths[w + 1][c]:
                    paths[w][c].append(str(rows[w][c]) + p)
                for p in paths[w + 1][c + 1]:
                    paths[w][c].append(str(rows[w][c]) + p)

                rows[w][c] += rows[w + 1][c]
    return rows[0][0], paths[0][0]

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    wiersze = []
    for line in file:
        wiersze.append(list(map(int, line.strip().split(' '))))

n, m = max_path(wiersze)
print(n)

for i in m:
    print(i)
