por=float(input())
kol=int(input())
vse=0
osh=0
pre=0
mak=None
sum=0.0
sht=0

for _ in range(kol):
    zap=input()
    vse+=1

    if zap=='error':
        osh+=1
        continue

