import sympy
def func(n,k):
    if k == 1:
        if sympy.isprime(n):
            return 'YES'
        return 'NO' 
    elif n<2*k:
        return 'NO'
    elif k == 2:
        ar = list(sympy.primerange(1,n))
        print(ar)
        for i in ar:
            if n-i in ar:
                return 'YES'
        return "NO"
    else:
        return "YES"

n,k = map(int,input().split())
print(func(n,k))

