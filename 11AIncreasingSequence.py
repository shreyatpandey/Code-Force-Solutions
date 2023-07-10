line = input()
numsLen, difference = line.split(' ')
numsLen = int(numsLen)
difference = int(difference)
current,total = -1,0
for i in range(0,numsLen):
    number = int(input())
    if current < number:
        current = number
    else:
        times = 1 + (current-number)//difference
        current = number + (times*difference)
        total += times
print(total)
