aliceNo = input()
bobReply = input()
checkTrailZero = 'A'
digitFreq = [0]*10
output = ''
for i in range(0,len(aliceNo)):
    digitFreq[ord(aliceNo[i])-ord('0')] += 1
    if aliceNo[i]>'0'and aliceNo[i]<checkTrailZero:
        checkTrailZero = aliceNo[i]

if checkTrailZero =='A':
    output = '0'
else:
    digitFreq[ord(checkTrailZero)-ord('0')] -= 1
    output += checkTrailZero
    for digit in range(0,10):
        while digitFreq[digit] != 0:
            digitFreq[digit] -= 1
            output += str(digit)

print(output)
if output == bobReply:
    print("OK")
else:
    print("Wrong_Answer")
