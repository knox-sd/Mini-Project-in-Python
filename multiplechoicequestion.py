'''This program will asked user a question with 3 option and accept user answer (a, b, c) and give correct score as a feedback.
    By doing this program, you can understand the how to create and use class, function, list (store answer in list).
    and for loop and if, else statement.
'''

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

def main():
    print("Welcome to the Multiple Choice Question!!")
    print("Please enter the one correct option from the Answer!!\n")

    question_prompts = [
        "What is the shortcut-key for Copy?\n(a) Ctrl + Alt \n(b) Ctrl + C\n(c) Alt + C\n\n",
        "What is the shortcut-key for Past?\n(a) Ctrl + V\n(b) Window + P\n(c) Alt + P\n\n",
        "What is the shortcut-key for Lock the Windows?\n(a) Window Key + Lock \n(b) Window Key + L \n(c) Window Key + I\n\n",
        "What is the shortcut-key for Task Manager?\n(a) Ctrl + Shift + Tab \n(b) Ctrl + Shift + T \n(c) Ctrl + Shift + Esc\n\n",
        "What is the shortcut-key for Shutdown PC?\n(a) Ctrl + F4 \n(b) Alt + F4 \n(c) Window + F4\n\n",
    ]

    questions = [
        Question(question_prompts[0], "b"),
        Question(question_prompts[1], "a"),
        Question(question_prompts[2], "b"),
        Question(question_prompts[3], "c"),
        Question(question_prompts[4], "b"),
    ]

    def run_mcq(questions):
        score = 0
        for question in questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " Correct")

        if score >= 4:
            print("Cheers!! You are in next level!!")
        else:
            print("Oops!! Try Again")

    run_mcq(questions)


if __name__ == "__main__":
    main()