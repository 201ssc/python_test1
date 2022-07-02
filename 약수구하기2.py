"""
다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
수	약수	약수의 개수
13	1, 13	2
14	1, 2, 7, 14	4
15	1, 3, 5, 15	4
16	1, 2, 4, 8, 16	5
17	1, 17	2
따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.

"""
def count(n):
    divisorsList = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    rl =len(divisorsList)
    return rl

def check(num):
    if num % 2 == 0:
        ad ="even"
    else:
        ad = "odd"
    return ad


def solution(left, right):
    lrlist = []
    for i in (range(left,right+1)):
        lrlist.append(i)
    lrlist
    sum = 0
    for i in lrlist:

        nn = count(i)  # 약수수 10> 1 2 5 10> 4
        ad = check(nn) # even
        if ad == "even":
            sum = sum + i
        else:
            sum = sum - i
    print(sum)
    return sum

c = solution(1,10)



