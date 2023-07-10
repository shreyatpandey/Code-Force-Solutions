line = input()
content = line.split(' ')
noOfLines = content[0]
P1,P2,P3 = content[1], content[2],content[3]
P1,P2,P3 = int(P1), int(P2), int(P3)
T1,T2 = content[4], content[5]
T1,T2 = int(T1), int(T2)
total, previousTime = 0,-1

for i in range(0,int(noOfLines)):
    startTime,endTime = input().split(' ')
    startTime = int(startTime)
    endTime = int(endTime)
    if previousTime < 0: 
        previousTime = startTime
    total += P1*(endTime - startTime)
    
    timeIdle = startTime - previousTime
    print(timeIdle)
    if timeIdle > T1 + T2:
        total += (timeIdle - T1 - T2)*P3
        timeIdle = T1 + T2
    
    if timeIdle > T1:
        total += (timeIdle-T1)*P2
        timeIdle = T1
    
    total += timeIdle * P1
    previousTime = endTime

    print(total)
