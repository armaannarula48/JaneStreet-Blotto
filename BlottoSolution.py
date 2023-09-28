import numpy as np

def randomIntegers():
    x = np.random.randint(100,size=10)
    y=[0,0,0,0,0,0,0,0,0,0]
    randomSum = sum(x)
    for j in range(0,10):
        y[j] = x[j] * 100 / randomSum

    return y

def strategy1():
    x = [np.random.normal(30,6),np.random.normal(33,6),np.random.normal(37,6)]
    y = [0,0,0,0,0,0,0,0,0,0]
    randomSum = sum(x)
    for j in range(0,3):
        y[j] = x[j] * 100 / randomSum

    return y

def strategy2_1():
    x = [0,0,np.random.normal(37,6),np.random.normal(30,6),np.random.normal(33,6)]
    y = [0,0,0,0,0,0,0,0,0,0]
    randomSum = sum(x)
    for j in range(2,5):
        y[j] = x[j] * 100 / randomSum

    return y


def strategy2_2():
    x = [0,np.random.normal(31,6),np.random.normal(37,6),np.random.normal(32,6),0]
    y = [0,0,0,0,0,0,0,0,0,0]
    randomSum = sum(x)
    for j in range(2,5):
        y[j] = x[j] * 100 / randomSum

    return y


def strategy3_1():
    x = [0, 0, np.random.normal(36,7), 0, 0, np.random.normal(33,7), np.random.normal(15,3), np.random.normal(16,3), 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    randomSum = sum(x)
    for j in range(0,10):
        y[j] = x[j] * 100 / randomSum

    return y



def strategy3_2():
    x = [0, np.random.normal(33, 6), 0, 0, np.random.normal(36, 6), np.random.normal(15, 3), np.random.normal(16, 3), 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    randomSum = sum(x)
    for j in range(0, 10):
        y[j] = x[j] * 100 / randomSum

    return y

def strategy3_3():
    x = [np.random.normal(33, 7), 0, 0, np.random.normal(37, 7), np.random.normal(15, 3), np.random.normal(15, 3), 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    randomSum = sum(x)
    for j in range(0, 10):
        y[j] = x[j] * 100 / randomSum

    return y

JaneStreetSolutions = []


for a in range(0,200):
    JaneStreetSolutions.append(strategy1())

for b in range(0, 200):
    JaneStreetSolutions.append(strategy2_1())

for c in range(0, 80):
    JaneStreetSolutions.append(strategy2_2())

for d in range(0, 200):
    JaneStreetSolutions.append(strategy3_1())

for e in range(0, 120):
    JaneStreetSolutions.append(strategy3_2())

for f in range(0,50):
    JaneStreetSolutions.append(strategy3_3())

for g in range(0,150):
    JaneStreetSolutions.append((randomIntegers()))



Totalscore = []



for i in range(0, len(JaneStreetSolutions)):
    score = 0
    for j in range(0,len(JaneStreetSolutions)):
        k = 0
        player1consecutive = 0
        player2consecutive = 0
        #score = 0
        while (player1consecutive < 4 and player2consecutive < 3 and k < 10):
            if JaneStreetSolutions[i][k] > JaneStreetSolutions[j][k]:
                score += k + 1
                player1consecutive += 1
                player2consecutive = 0

            elif JaneStreetSolutions[i][k] == JaneStreetSolutions[j][k]:
                player1consecutive = 0
                player2consecutive = 0

            else:
                player1consecutive = 0
                player2consecutive += 1
            if player1consecutive == 3:
                for l in range(k+1,10):
                    score += l+1
                player1consecutive = 4

            k += 1
    Totalscore.append(score/len(JaneStreetSolutions))




maximum = Totalscore.index(max(Totalscore))
print("Best strategy in sample space", JaneStreetSolutions[maximum])
print("Maximum score of ", Totalscore[maximum])




mySolution = [0,0,46,1,1,25,12,15,0,0]
print("My solution", mySolution)
myscore = 0
for i in range(0, len(JaneStreetSolutions)):
    k = 0
    player1consecutive = 0
    player2consecutive = 0
    while (player1consecutive < 4 and player2consecutive < 3 and k < 10):
            if mySolution[k] > JaneStreetSolutions[i][k]:
                myscore += k + 1
                player1consecutive += 1
                player2consecutive = 0

            elif mySolution[k] == JaneStreetSolutions[i][k]:
                player1consecutive = 0
                player2consecutive = 0

            else:
                player1consecutive = 0
                player2consecutive += 1
            if player1consecutive == 3:
                for l in range(k+1,10):
                    myscore += l+1
                player1consecutive = 4

            k += 1

print("My score: ",  myscore/len(JaneStreetSolutions)) 