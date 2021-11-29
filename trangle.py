import random
a=[]
menu=int(input('''Введите 1 для автоматического заполнения списка числами от A до B
Введите 2 для ручного ввода
'''))
N=int(input('''Введите количество чисел
'''))
if menu==1:
    c=int(input())
    d=int(input())
    for i in range(N):
        a.append(random.randint(c,d))
if menu==2:
    for i in range(N):
        a.append(int(input()))

print("Исходный список")
print(a)

a.sort(reverse=True)
smax=0
for x in range(0,len(a)-2):
     if a[x]+a[x+1] > a[x+2] and a[x]< a[x+1]+a[x+2] and -a[x]+a[x+1] < a[x+2]:
        q=(a[x]+a[x+1]+a[x+2])/2
        s=(q*(q-a[x])*(q-a[x+1])*(q-a[x+2]))**0.5
        if s > smax:
            smax=s
            b1=a[x]
            b2=a[x+1]
            b3=a[x+2]
            break
if smax==0:
    print("Из данных элиментов нельзя создать треугольник")
else:
    print(smax)
    print(b1,b2,b3)




