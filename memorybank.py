import random

num_of_problems = int(input("Enter the number of problems(maximum 10 problems): "))
user_answer = 0
answer_checker = 0
problem_input = ""
attempts = 0
correct_answers = 0
problems = []

if num_of_problems > 10:
    num_of_problems = 10

for i in range(num_of_problems):
    problem_input = input("Enter a problem: ")
    problems.append(problem_input)

user_choice = "y"

while problems:
    rand_index = random.randint(0, len(problems) - 1)
    problem = problems.pop(rand_index)
    print(f"{problem}, solve this problem")

    answer_checker = eval(problem)
    user_answer = int(input("Enter your answer: "))

    if user_answer == answer_checker:
        print("Correct!")
        correct_answers += 1
        attempts += 1
    else:
        print(f"Incorrect, the correct answer is {answer_checker}")
        attempts += 1
    num_of_problems -= 1
    print(f"You have {num_of_problems} problems left")

    if num_of_problems == 0:
        break
    user_choice = input("Would you like to quit or try another problem? (y/n): ")
    if user_choice == "n":
        break


print(f"You got {correct_answers} out of {attempts} correct")
