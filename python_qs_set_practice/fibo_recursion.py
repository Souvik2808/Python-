def fibo_recur(n):
    if(n==0 or n==1):
        return 1

    return n * fibo_recur(n-1)

print(fibo_recur(5))
