count = int(input())
for i in range(2,count+1):
    prime = 1
    for q in range (2,i):
        if i%q == 0:
            prime = 0
            break
    if prime == 1:
        print (i ,' is prime')
        