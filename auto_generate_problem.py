import random

def generate_problem():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])
    
    if operator == '+':
        solution = operand1 + operand2
    elif operator == '-':
        operand1, operand2 = max(operand1, operand2), min(operand1, operand2)
        solution = operand1 - operand2
    elif operator == '*':
        solution = operand1 * operand2
    else:
        operand1, operand2 = operand1 * operand2, operand2
        solution = operand1 / operand2
    
    problem_text = f"What is {operand1} {operator} {operand2}?"
    return problem_text, solution

if __name__ == "__main__":
    problem, answer = generate_problem()
    print(problem)
    user_answer = float(input("Your answer: "))
    
    if abs(user_answer - answer) < 1e-6:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {answer:.2f}")
