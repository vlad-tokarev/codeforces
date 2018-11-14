from collections import defaultdict

# computation complexity = n

elements = defaultdict(int)

if __name__ == '__main__':

    n = int(input())
    for i in range(n):  # bigO = n

        # if x3 - input
        a, x = [int(num) for num in input().split(' ')]

        if elements[a] < x:
            elements[a] = x

    # this loop the same as above =>  # bigO = n
    m = int(input())  #
    for i in range(m):

        b, y = [int(num) for num in input().split(' ')]
        if elements[b] < y:
            elements[b] = y

    # big(O) = n
    print(sum(elements.values()))

    # => big(O) = n => 3n => n

