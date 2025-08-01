import random

g_score = 0
v_score = 0
snakes = {3:0,99:54,77:49,21:12,96:5,50:20,7:5,19:9,32:12,46:6,68:39,80:40}
ladders = {2:17,13:63,10:98,24:76,33:56,79:84,88:92}
while g_score < 51 and v_score < 51:
    g = input("Goutham-[s]top and [c]ontinue: ")
    if g == "c":
        g_turn = random.randint(1,6)
        g_score += g_turn
        if g_score in snakes:
            g_score = snakes[g_score]
            print(f"***Goutham - snake bit - score: Goutham score: {g_score}-Dice: {g_turn}***\n")
        elif g_score in ladders:
            g_score = ladders[g_score]
        print(f"\n***Goutham - ladder - score - {g_score}-Dice: {g_turn}***\n")
    else:
        print("varma win")
        break

    v = input("Varma-[s]top and [c]ontinue: ")
    if v == 'c':
        v_turn = random.randint(1,6)
        v_score += g_turn
        if v_score in snakes:
            v_score = snakes[v_score]
            print(f"\n***varma - snake bit - score: varma score: {v_score}-Dice: {v_turn}***\n")
        elif v_score in ladders:
            v_score = ladders[v_score]
            print(f"\n***varma - ladder - score - {v_score}-Dice: {v_turn}***\n")
        print(f"\nvarma score: {v_score}-Dice: {v_turn}\n")
    else:
        print("Goutham win")
        break
if g_score > v_score:
    print("goutham win")
else:
    print("varma win")


