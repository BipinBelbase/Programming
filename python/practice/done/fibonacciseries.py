def fib(n):
    if n < 0 or n > 100 :
        print("please select only from 1 to 100")
        return
    
    fib = [0,1,1]
    if n == 1 or n == 2 or n == 0:
        print(f"the value of {n}th possition is--->", fib[:n+1])
        return
    
    summ = 2
    
    for i in range(n+1):
        if i > 2:
            
            currentfib = fib[i-1] + fib[i-2]
            summ = summ + currentfib
            fib.append(currentfib)
        
        
    print(f"the value of {n}th possition is : {fib} and the sum of fib is :{summ} ")
        



for i in range(10):
    fib(i)