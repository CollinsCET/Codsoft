import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
  """
  Generates a random password based on user-specified criteria.

  Args:
      length: The desired length of the password.
      include_uppercase: True to include uppercase letters.
      include_lowercase: True to include lowercase letters.
      include_digits: True to include digits.
      include_symbols: True to include symbols.

  Returns:
      A randomly generated password meeting the specified criteria.
  """

  # Define character sets based on user options
  char_set = ""
  if include_uppercase:
    char_set += string.ascii_uppercase
  if include_lowercase:
    char_set += string.ascii_lowercase
  if include_digits:
    char_set += string.digits
  if include_symbols:
    char_set += string.punctuation

  # Check if at least one character set is chosen
  if not char_set:
    print("Error: Please select at least one character type for the password.")
    return None

  # Generate random password
  password = ''.join(random.sample(char_set, length))
  return password

def main():
  while True:
    try:
      # Get password length
      length = int(input("Enter desired password length (minimum 8 characters): "))
      if length < 8:
        print("Password length must be at least 8 characters.")
        continue

      # Get complexity options
      include_uppercase = input("Include uppercase letters (y/n)? ").lower() == 'y'
      include_lowercase = input("Include lowercase letters (y/n)? ").lower() == 'y'
      include_digits = input("Include digits (y/n)? ").lower() == 'y'
      include_symbols = input("Include symbols (y/n)? ").lower() == 'y'

      # Generate and display password
      password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
      if password:
        print(f"Your generated password: {password}")

      # Ask if user wants to generate another password
      choice = input("Generate another password? (y/n): ")
      if choice.lower() != 'y':
        break

    except ValueError:
      print("Invalid input! Please enter a number for password length.")

if __name__ == "__main__":
  main()

