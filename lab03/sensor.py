por=float(input())
kol=int(input())
vse=0
osh=0
pre=0
mak=-float('inf')
sum=0.0
sht=0

for _ in range(kol):
    zap=input()
    vse+=1

    if zap=='error':
        osh+=1
        continue

    tem = float(zap)
    sht += 1
    sum += tem

    if  tem > mak:
        mak = tem

    if tem > por:
        pre += 1


sre=sum/sht if sht >0 else 0.0
print(vse)
print(osh)
print(pre)
print(f"{mak:.1f}")
print(f"{sre:.1f}")

