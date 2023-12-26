import random as rd
import numpy as np

#boxscore is a 2D list of the game so far
# [ [player 1 decisions], [player 2 decisions] ]

def always_cooperate(boxscore, playernum):
    return True

def always_defect(boxscore, playernum):
    return False

def cooperate_once(boxscore, playernum):
    if (len(boxscore[0]) == 0):
        return True
    else:
        return False

def defect_once(boxscore, playernum):
    if (len(boxscore[0]) == 0):
        return False
    else:
        return True

def random_strategy(boxscore, playernum):
    return rd.randint(0, 1)


def tit_for_tat(boxscore, playernum):
    if (len(boxscore[0]) == 0):
        return True
    else:
        opponent_num = (not playernum)
        return boxscore[opponent_num][-1]
    
def grudge(boxscore, playernum):
    if (len(boxscore[0]) == 0):
        return True
    else:
        opponent_num = (not playernum)
        return ( boxscore[opponent_num].count(0) == 0 )

#This is a less extreme version of grudge
def disproportionate_response(boxscore, playernum, n = 3):
    if (len(boxscore[0]) == 0):
        return True
    else:
        opponent_num = (not playernum)
        
        if (len(boxscore[opponent_num]) < n):
            check = (False not in boxscore[opponent_num])
        else:
            check = (False not in boxscore[opponent_num][-n:])
        
        return check
            

#Cooperate if 2 of your opponent's last 3 moves have been to cooperate
def nicestrat(boxscore, playernum):
    if (len(boxscore[0]) < 3):
        return True
    else:
        opponent_num = (not playernum)
        return ( sum(boxscore[opponent_num][-3:]) >= 2 )

#tit for n tats
def pushover(boxscore, playernum, n = 3):
    
    if (len(boxscore[0]) < n):
        return True
    else:
        opponent_num = (not playernum)
        return ( sum(boxscore[opponent_num][-n:]) >= 1 )    


#Cooperate if 2 of your opponent's last 3 moves have been to cooperate
def sneakystrat(boxscore, playernum):
    n = 6
    opponent_num = (not playernum)
    
    if (len(boxscore[0]) == 0):
        return True
    
    elif (len(boxscore) < n):
        return boxscore[opponent_num][-1]
    
    else:
        num_of_coops = sum(boxscore[opponent_num][-3:])
        if (num_of_coops <= 1):
            return False
        elif (num_of_coops == 2):
            return True
        elif ((sum(boxscore[opponent_num][-n:]) == n) and (boxscore[playernum][-1] == True)):
            return (rd.random() < 0.5)
        else:
            return True

def run_game(f, g, num_rounds, noise = 0.002, output_log = False):
    boxscore = [ [], [] ]
    player1_score = 0
    player2_score = 0

    i = 0
    
    while (i < num_rounds):
        X1 = f(boxscore, 0)
        X2 = g(boxscore, 1)
        
        if (rd.random() < noise):
            X1 = not X1
        
        if (rd.random() < noise):
            X2 = not X2
    
        if (X1):
            if (X2):
                player1_score += 3
                player2_score += 3
            else:
                player2_score += 5
        else:
            if (X2):
                player1_score += 5
            else:
                player1_score += 1
                player2_score += 1
              
        boxscore[0].append(X1)
        boxscore[1].append(X2)
        
        i += 1

    #print("Player 1: %d" %player1_score)
    #print("Player 2: %d" %player2_score)
    
    if (output_log):
        
        f = open("Output.txt", 'w')
        for j in range(num_rounds):
            f.write(str(boxscore[0][j]) + '\t' + str(boxscore[1][j]) + '\n')
        f.close()
    
    return (player1_score, player2_score)

strategies = [ always_cooperate, always_defect, tit_for_tat, grudge, random_strategy,
              disproportionate_response, nicestrat, sneakystrat, pushover]

names = ["always cooperate", "always defect", "tit for tat", "grudge", "pray to RNGesus",
              "disproportionate response", "nice", "sneaky", "pushover"]

N = len(strategies)
playerscores = np.zeros((N, N), dtype=np.int32)
opponentscores = np.zeros((N, N), dtype=np.int32)

for s1 in range(N):
    for s2 in range(N):
        p1score = 0
        p2score = 0
        
        for j in range(5):
            banana = run_game(strategies[s1], strategies[s2], 200)
            p1score += banana[0]
            p2score += banana[1]
        
        playerscores[s1][s2] = p1score
        opponentscores[s1][s2] = p2score

for i in range(N):
    total_score = 0
    for j in range(N):
        total_score += playerscores[i][j]
        total_score += opponentscores[j][i]
    #scores
    print("Average number of points per 200 round game \n")
    print(names[i], '\t', total_score / 100)




