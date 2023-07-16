'''
SuperAgents
'''
totalLength = 9
booleanList = [0]*totalLength
k = 0
for i in range(0,totalLength):
    char = input()
    if char == 'X':
        booleanList[i] = 1
isSymmetric = True
for i in range(0,totalLength):
    if booleanList[i] != booleanList[totalLength-i-1]:
        isSymmetric = False
        break;
if isSymmetric:
    print(isSymmetric)
else:
    print(isSymmetric)
