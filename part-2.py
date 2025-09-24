n = [13, 11, 12]

n.sort()

S = 'Ciao mondo!'

print(S)

print(n)


M = [[1, 2, 3], # A 3 × 3 matrix, as nested lists
[4, 5, 6], # Code can span lines if bracketed
[7, 8, 9]]

print(M)

s_col = [0 for i in range(len(M))]

for row in M:
    for i in range(len(row)):
        s_col[i] += row[i]

print(s_col)

D = {'a': 1, 'b': 2, 'c': 3}

ksd = [key for key in D]

T = (1,3,4)

f = open('README.MD', 'r')

lines = [line.strip() for line in f]

lines_map = list(map(str.strip, open('README.MD').readlines()))

f.close()


def test(arg = 10):
    print('hello world!', arg)
    global X
    X = 10
    return

test(11)

test.attr= 'c'
test.attr2 = 'd'

print(test.attr)


