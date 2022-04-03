from Question import Question

question_prompt = [
    "1.The Olympics are held every how many years?\n(a) 4 years\n(b) 2 years\n(c) 5 years\n(d) 10 years\n\n",
    "2.Who has won more tennis grand slam titles, Venus Williams or Serena Williams?\n(a) Serena Williams\n(b) Venus Williams\n(c) mickael jordan\n(d) shaquille o'neal\n\n",
    "3.How many medals did China win at the Beijing Olympics?\n(a) 80\n(b) 100\n(c) 30\n(d) 150\n\n",
    "4.How long is a marathon?\n(a) 26 miles\n(b) 32 miles\n(c) 50 miles\n(d) 80 miles\n\n",
    "5.What type of race is the Tour de France?\n(a) jumping \n(b) running\n(c) swimming\n(d) Bicycle race\n\n",
    "6.Basketball player, Scottie Pippen, has a word tattooed on his forearm. What does it say?\n(a) basketball \n(b) jordan\n(c) Pip\n(d) winner\n\n",
    "7.How many Olympic games were held in countries that no longer exist?\n(a) 3\n(b) 5\n(c) 6\n(d) 8",
    "8.What African country was the first ever to qualify for a Soccer World Cup?\n(a) Ethiopia\n(b) Egypt\n(c) Cameroon\n(d) Senegal\n\n",
    "9.What is the only country to have played in every single soccer World Cup?\n(a) Brazil\n(b) USA\n(c) Israel\n(d) Nigeria\n\n",
    "10.What do the rings in the Olympics represent?\n(a) Number of sports\n(b) The continents of the world\n(c) Number of medals\n(d) Gold chains\n\n "
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "a"),
    Question(question_prompt[2], "b"),
    Question(question_prompt[3], "a"),
    Question(question_prompt[4], "d"),
    Question(question_prompt[5], "c"),
    Question(question_prompt[6], "a"),
    Question(question_prompt[7], "b"),
    Question(question_prompt[8], "a"),
    Question(question_prompt[9], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
