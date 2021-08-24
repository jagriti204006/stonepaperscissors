import random 

print(" STONE PAPER SCISSORS ".center(80))
print("---------------------------------".center(80))

print('''
1. STONE 
2. PAPER
3. SCISSORS 
''')

userPoints = 0
cpuPoints = 0

# winning conditions
# 1, 2 -> 2
# 1, 3 -> 1
# 2, 3 -> 3

for i in range(10):
    print("ROUND: ", i+1)
    userChoice = int(input("Enter your choice: "))
    cpuChoice = random.randint(1, 3)
    # print("User Choice: ", userChoice)
    print("CPU Choice: ", cpuChoice)

    if(userChoice == cpuChoice):
        print("Draw Round")

    elif (userChoice == 1 and cpuChoice == 2):
        cpuPoints += 1
        print("CPU wins this round")

    elif (userChoice == 1 and cpuChoice == 3):
        userPoints += 1
        print("User wins this round")

    elif (userChoice == 2 and cpuChoice == 1):
        userPoints += 1
        print("User wins this round")

    elif (userChoice == 2 and cpuChoice == 3):
        cpuPoints += 1
        print("CPU wins this round")

    elif (userChoice == 3 and cpuChoice == 1):
        cpuPoints += 1
        print("CPU wins this round")
    
    elif (userChoice == 3 and cpuChoice == 2):
        userPoints += 1
        print("User wins this round")

    print("------------------------".center(80))
    

    # print("USER POINTS: ", userPoints)
    # print("CPU POINTS: ", cpuPoints)

print("USER POINTS: ", userPoints)
print("CPU POINTS: ", cpuPoints)

print(" -----RESULT-----")
if(cpuPoints > userPoints):
    print("CPU Wins")
elif(cpuPoints < userPoints):
    print("User Wins")
else: 
    print("Game Draw")

