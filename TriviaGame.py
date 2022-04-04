from Question import Question

question_prompt1 = ['\t\t\t\nRound 1\n'
    "1.The Olympics are held every how many years?\n(a) 4 years\n(b) 2 years\n(c) 5 years\n(d) 10 years\n\n",

    "2.Who has won more tennis grand slam titles?\n(a) Serena Williams\n(b) Venus Williams\n(c) mickael jordan\n(d) shaquille o'neal\n\n",

    "3.How many medals did China win at the Beijing Olympics?\n(a) 80\n(b) 100\n(c) 30\n(d) 150\n\n",

]
question_prompt2 = ['Round 2\n'
    "4.How long is a marathon?\n(a) 26 miles\n(b) 32 miles\n(c) 50 miles\n(d) 80 miles\n\n",

    "5.What type of race is the Tour de France?\n(a) jumping \n(b) running\n(c) swimming\n(d) Bicycle race\n\n",

    "6.Basketball player, Scottie Pippen, has a word tattooed on his forearm. What does it say?\n(a) basketball \n(b) jordan\n(c) Pip\n(d) winner\n\n",

]
question_prompt3 = ['\t\t\tRound 3\n'
    "7.How many Olympic games were held in countries that no longer exist?\n(a) 3\n(b) 5\n(c) 6\n(d) 8\n\n",

    "8.What African country was the first ever to qualify for a Soccer World Cup?\n(a) Ethiopia\n(b) Egypt\n(c) Cameroon\n(d) Senegal\n\n",

    "9.What is the only country to have played in every single soccer World Cup?\n(a) Brazil\n(b) USA\n(c) Israel\n(d) Nigeria\n\n",

]
question_prompt4 = ['\t\t\t\nBonus\n'
    "10.What do the rings in the Olympics represent?\n(a) Number of sports\n(b) The continents of the world\n(c) Number of medals\n(d) Gold chains\n\n "

]
questions = [
    Question(question_prompt1[0], "a"),
    Question(question_prompt1[1], "a"),
    Question(question_prompt1[2], "b"),
    Question(question_prompt2[0], "a"),
    Question(question_prompt2[1], "d"),
    Question(question_prompt2[2], "c"),
    Question(question_prompt3[0], "a"),
    Question(question_prompt3[1], "b"),
    Question(question_prompt3[2], "a"),
    Question(question_prompt4[0], "b"),
]

def run_test(questions):
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

run_test(questions)
