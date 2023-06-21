import re

def password_security_grade(password):
    score = 0

    # length
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # complexity
    if re.search(r"\d", password):  # digit
        score += 1
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):  # lowercase and uppercase
        score += 1
    if re.search(r"\W", password):  # special character
        score += 1

    # uniqueness
    if len(set(password)) > len(password) / 2:  # half characters unique
        score += 1

    # grading
    if score == 0:
        return "Can't grade"
    elif score == 1:
        return "Very weak"
    elif score == 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    elif score == 4:
        return "Strong"
    else:
        return "Very strong"

while True:
    user_input = input("Enter a password (q to quit): ")
    if user_input.lower() == "q":
        break
    else:
        security_grade = password_security_grade(user_input)
        print("Password security grade:", security_grade)
