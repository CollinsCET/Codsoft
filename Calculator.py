def calculate(num1, operator, num2):
  """
  Performs the specified arithmetic operation on two numbers.

  Args:
      num1: The first number.
      operator: The arithmetic operator (+, -, *, /).
      num2: The second number.

  Returns:
      The result of the calculation.
  """
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    if num2 == 0:
      print("Error: Division by zero!")
      return None  # Indicate error
    else:
      return num1 / num2
  else:
    print("Invalid operator!")
    return None  # Indicate error

def main():
  while True:
    # Get user input for numbers and operator
    try:
      num1 = float(input("Enter the first number: "))
      operator = input("Enter the operator (+, -, *, /): ")
      num2 = float(input("Enter the second number: "))
    except ValueError:
      print("Invalid input! Please enter numbers.")
      continue

    # Perform calculation
    result = calculate(num1, operator, num2)

    # Display result (if no error)
    if result is not None:
      print(f"{num1} {operator} {num2} = {result}")

    # Ask if user wants to perform another calculation
    choice = input("Do you want to calculate again? (y/n): ")
    if choice.lower() != 'y':
      break

if __name__ == "__main__":
  main()

