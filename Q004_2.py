N, L = map(int, input().split())
tranScripts = [list(map(int,input().split(" "))) for _ in range(L)]
tempScript = []
orderedScripts = []
studentScripts = [0] * L

for subject in range(N):
    tempScript = []
    for person in range(L):
        tempScript.append(tranScripts[person][subject])
    else:
        orderedScripts.append(tempScript)
else:
    for apexStudent in orderedScripts:
        studentScripts[apexStudent.index(max(apexStudent))] += 1
    else:
        print(studentScripts.index(max(studentScripts)) + 1, max(studentScripts))
