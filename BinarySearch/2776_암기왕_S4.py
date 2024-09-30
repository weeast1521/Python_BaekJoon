import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input()) # N < 1,000,000
    note1 = list(map(int,input().split())) # O(N)
    note1.sort() # O(NlogN)

    M = int(input()) # N < 1,000,000
    note2 = list(map(int,input().split())) # O(N)

    # for number in note2: # O(N*N)
    #     if number in note1: # O(N)
    #         print(1)
    #     else:
    #         print(0)
    # ==> 단순한 list in 함수 이용시 시간 초과 발생

    # O(NlogN)
    for number in note2: # O(N)
        start = 0
        end = N - 1
        check = False

        while(start <= end): # O(logN)
            mid = (start + end) // 2
            
            if note1[mid] == number:
                check = True
                break
            elif note1[mid] > number:
                end = mid - 1
            else:
                start = mid + 1
        
        if check:
            print(1)
        else:
            print(0)

# Cf) in() 함수 시간복잡도 -> set( O(1) ), dict( O(1) ), list( O(N) )