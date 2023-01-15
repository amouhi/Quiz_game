print("Welcome to my computer quiz!")

playing = input("Do you want to play ? ")
print (playing)
if playing.lower() != "yes":
    quit()
print("let's play then ! ")
score = 0
answer = input("what does CPU stand for ? ")
if answer.lower() == "central processing unit":
    print('correct! ')
    score += 1
else:
    print("Incorrect!")

    
answer = input("What does GPU stand for ?  ")
if answer.lower() == "graphics processing unit":
    print('correct! ')
    score += 1
else:
    print("Incorrect!")

   
answer = input("What does RAM stand for ? ")
if answer.lower() == "random access memory":
    print('correct! ')
    score += 1
else:
    print("Incorrect!")

   
answer = input("what does PSU stand for ? ")
if answer.lower() == "power supply":
    print('correct! ')
    score += 1
else:
    print("Incorrect!")

print("Yous got " + str(score) + " questions correct!")
print("Yous got " + str((score / 4) * 100) + "%.")

