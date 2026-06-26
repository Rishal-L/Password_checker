import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("• Make it longer (at least 8 characters).")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("• Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:

        feedback.append("• Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("• Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+-]", password):
        score += 1
    else:
        feedback.append("• Add at least one special character (e.g., !, @, #, $, %).")

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Medium 😐"
    elif score == 2:
        strength = "Weak ⚠️"
    else:
        strength = "Very Weak ❌"

    return strength, score, feedback

print("=== Cybersecurity Password Strength Tool ===")
user_password = input("Enter a password to test: ")

strength_rating, final_score, user_feedback = check_password_strength(user_password)

print("\n--- Results ---")
print(f"Password Strength: {strength_rating}")
print(f"Total Score: {final_score}/5")

if user_feedback:
    print("\nSuggestions to improve your password:")
    for tip in user_feedback:
        print(tip)