questions = [
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
    [
        "Who developed Python Programming Language?", "Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom", 3
    ],
    [
        "Which type of Programming does Python support?", "object-oriented programming", " structured programming", "functional programming", "All of the mentioned", 4
    ],
    [
        "Which of the following is used to define a block of code in Python language?", " Indentation", "Key", "Brackets", "All of the mentioned", 1
    ],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):

    ques = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")

    print(f"a. {ques[1]}              b. {ques[2]}")
    print(f"c. {ques[3]}              d. {ques[4]}")

    reply = int(input("Enter your answer (1-4) or 0 to quit: "))

    if(reply == 0):
        money = levels[i-1]
        break

    if(reply == ques[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("Wrong answer")
        break

print(f"Your take home money {money}")
