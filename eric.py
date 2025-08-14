import numpy
import math

def sop(data, plan):
    total = 0.0
    for i in range(len(data)):
        for j in range(len(data[i])):
            total += int(data[i][j]) * plan[i,j]
    return total
    
plan = 0.
best = 1

while 1 :
    data = numpy.random.randint(2, size=(4,3))
    print(data)
    ans = int(input("ans"))
    planA = plan + numpy.random.rand(4,3)*best
    planB = plan - numpy.random.rand(4,3)*best
    thr = numpy.random.rand(2)*best
    expA = 1/(1+math.exp(-sop(data, planA)+thr[0]))
    expB = 1/(1+math.exp(-sop(data, planB)+thr[1]))
    sub = expA*expA-2*ans*expA - expB*expB-2*ans*expB
    if best*best > sub*sub :
        best = sub
    plan = planA
    if sub > 0 :
        plan = planB
    print("plan:\n",plan,"\n",expA)
