def sum(x):
    return x * (x + 1)

def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


if __name__ == '__main__':
    print(sum(76))
    print(recur_fibo(19))
