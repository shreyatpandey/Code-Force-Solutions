line = input()
x = int(line)
if x<0: x = (-1)*x
total,result = 0,0
while total<x or (result-x)%2 :
    total += 1
    result += total
print(total)
