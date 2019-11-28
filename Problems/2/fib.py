def fib(n):
    x = 0
    y = 1
    current = x + y
    count = 2
    sum = 0
    while current < n:
        print(current)
        if count == 3:
            print('even: ', current)
            count = 0
            sum += current
        x = y
        y = current
        current = x + y
        count += 1
    print('total sum', sum)

fib(4000000)
