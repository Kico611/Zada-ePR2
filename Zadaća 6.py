def generator(n):
    for i in range(1,n+1):
        yield i

my_gen = generator(20)
for i in my_gen:
    if i%2 == 0:
        print("Broj je paran",i)
    else:
        print("Broj je neparan",i)
