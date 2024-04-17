def is_prime(n): #пытаюсь тут написать без циклов фор
    List_divisors = []
    def korn(x):
        if n == 2:
            return True
        if n == 1:
            return False
        if x == 1:
            if len(List_divisors) >= 1:
                return False
            else:
                return True
        if n / x == n // x:
            return False
        return korn(x - 1)

    return korn


n = int(input())
f = is_prime(n)
print(f(int(n ** 0.5) + 1))

