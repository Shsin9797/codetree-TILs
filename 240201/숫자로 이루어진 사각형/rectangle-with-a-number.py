def make_square(n):
    cnt=1
    for _ in range(n):
        for _ in range(n):
            if cnt >9:
                cnt=1
            print(cnt,end=" ")
            cnt +=1
        print()


N = int(input())
make_square(N)