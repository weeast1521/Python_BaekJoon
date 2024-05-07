#실패! 뒤에 단어들은 맞는다면 ?가 아니라 뒷 단어들은 나오게 해야하지만 이렇게 하면 특정 번호부터는 뒤가 다 ?로 나옴
N = int(input())

directory = input()
length1 = len(directory)
length2 = len(directory)
for i in range(N-1):
    tmp = input()

    for j in range(length2):
        if tmp[j] != directory[j]:
            length2 = j
            directory = directory[0:j]
            break

print(directory, end ="")
print("?"*(length1-len(directory)))
