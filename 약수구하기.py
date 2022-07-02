"""
n	return
12	28
5	6

"""

def solution(n):
    answer = 0
    return answer


def solution(n):
    divisorsList = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if (n % i == 0):
            divisorsList.append(i)
            if ((i ** 2) != n):
                divisorsList.append(n // i)

    divisorsList.sort()

    answer = sum(divisorsList)

    return answer


