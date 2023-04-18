N = int(input())
d = dict()

for _ in range(N):
    word1, word2 = map(str, input().split())
    d[word1] = word2
    d[word2] = word1

word = input()
print(d[word])
