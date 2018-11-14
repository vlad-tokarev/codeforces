from heapq import heappush, heappop, heapify

n = int(input())

W_I = [(int(w), i) for i, w in enumerate(input().split(' '))]
heapify(W_I)

W_E = []

passengers = input()
answer = []

if __name__ == '__main__':

    for passenger in passengers:

        if passenger == '0':
            w, i = heappop(W_I)
            heappush(W_E, (-w, i))
            answer.append(i+1)
        else:
            w, i = heappop(W_E)
            answer.append(i+1)

    print(' '.join([str(el) for el in answer]))
