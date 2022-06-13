# Алгоритм 4. Обработка статической последовательности данных изветсной длины

n = 0
while n<=0:
    print("Введите целое число:")
    n = int(input())
    if n > 0:
        s=0
        i=1
        for i in range(1, n+1):
            d=int(input("Введите число:"))
            s=s+d 
            i=i+1
        mid=s/(i-1)
        print(mid)
    else:
        continue

        




    
         


    