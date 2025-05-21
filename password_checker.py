def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)  # special chars

    score = 0
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    if score == 5:
        return "Very Strong Password ✅"
    elif score >= 3:
        return "Moderate Password ⚠️"
    else:
        return "Weak Password ❌"

def main():
    pwd = input("Enter your password to check strength: ")
    result = check_password_strength(pwd)
    print(result)

if __name__ == "__main__":
    main()
