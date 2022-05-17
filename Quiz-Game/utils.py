
def startGame(questions):
    score = 0
    correct = 0
    count = 0
    for question in questions:
        answer = input(question.prompt)
        count+=1
        if count==10:
            score+=4


        if answer == question.answer:
            score += 1
            correct += 1
            print('#####################')
            print("your score is :",score,"\nCorrect \U0001F602 ! the answer is" + " " + answer)
            print('#####################')
        else:
            print('#####################')
            print ("Wrong \U0001F612, the answer is" + " " + answer)
            print('#####################')


    print("You got " + str(correct) + "/" + str(len(questions)) + " answers correct")
