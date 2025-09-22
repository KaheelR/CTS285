import random

def memory_bank():
    num_of_problems = int(input("Enter the number of problems (maximum 10): "))
    if num_of_problems > 10:
        num_of_problems = 10

    problems = []
    for i in range(num_of_problems):
        problem_input = input(f"Enter problem {i+1}: ")
        problems.append(problem_input)

    attempts = 0
    correct_answers = 0

    while problems:
        rand_index = random.randint(0, len(problems) - 1)
        problem = problems.pop(rand_index)
        print(f"\nSolve this: {problem}")
        answer_checker = eval(problem)

        try:
            user_answer = int(input("Your answer: "))
            if user_answer == answer_checker:
                print("Correct!")
                correct_answers += 1
            else:
                print(f"Incorrect, correct answer is {answer_checker}")
            attempts += 1
        except ValueError:
            print("Invalid input. Skipped.")
            attempts += 1

        if not problems:
            break
        cont = input("Try another? (y/n): ")
        if cont.lower() == "n":
            break

    print(f"\nYou got {correct_answers} out of {attempts} correct.")

if __name__ == "__main__":
    memory_bank()
