# Password Strength Checker

This Python script checks the strength of passwords entered by users. It evaluates the strength based on various criteria such as length, presence of uppercase letters, lowercase letters, digits, and special characters. Additionally, it checks if the password is common by comparing it against a list of common passwords.

## Prerequisites
- Python 3.x

## How to Use
1. Run the script in a Python environment.
2. You will be prompted to enter a password.
3. The script will evaluate the password and provide a strength score out of 7.
4. Depending on the score, it will classify the strength level as Weak, Okay, or Strong.
5. You will be asked if you want to continue or exit.
6. If you choose to continue, you can enter another password.

## Code Overview
- The script imports the `string` module for character manipulation and the `time` module for adding delays.
- It defines a function to check the strength of a password.
- It prompts the user to input a password and evaluates its strength based on various criteria.
- It reads a file containing a list of common passwords and checks if the entered password is common.
- The script then calculates the strength score based on password length and other factors.
- It categorizes the password strength level as Weak, Okay, or Strong based on the score.
- Users can choose to continue checking passwords or exit the program.

## Files
- `10k-most-common.txt`: Contains a list of common passwords.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
