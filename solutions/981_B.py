from collections import defaultdict

elements = defaultdict(int)

if __name__ == '__main__':

    n = int(input())
    for i in range(n):

        a, x = [int(num) for num in input().split(' ')]
        if elements[a] < x:
            elements[a] = x

    m = int(input())
    for i in range(m):

        b, y = [int(num) for num in input().split(' ')]
        if elements[b] < y:
            elements[b] = y

    print(sum(elements.values()))

