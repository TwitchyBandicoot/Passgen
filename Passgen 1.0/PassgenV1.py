import string
import secrets
try:
    import pyperclip
    CLIP_AVAILABLE = True
except ImportError:
    CLIP_AVAILABLE = False

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("No characters available to generate password!")

    return ''.join(secrets.choice(chars) for _ in range(length))
def ask_yes_no(prompt, default=True):
    """Helper function to ask yes/no questions."""
    while True:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False
        elif choice == "" and default is not None:
            return default
        else:
            print("Please enter 'y' or 'n'.")

def main():
    print("=== Secure Password Generator ===\n")

    while True:
        # Ask for password length
        while True:
            try:
                length = int(input("Enter desired password length: "))
                if length > 0:
                    break
                else:
                    print("Length must be greater than 0.")
            except ValueError:
                print("Please enter a valid number.")

        # Ask about character options
        use_uppercase = ask_yes_no("Include uppercase letters?")
        use_digits = ask_yes_no("Include digits?")
        use_symbols = ask_yes_no("Include symbols?")

        # Generate the password
        password = generate_password(length, use_digits, use_symbols, use_uppercase)
        print("\nYour password is:\n" + password)

        # Copy to clipboard if available
        if CLIP_AVAILABLE:
            try:
                pyperclip.copy(password)
                print("(Password copied to clipboard!)")
            except Exception:
                print("(Could not copy password to clipboard.)")

        # Ask if the user wants another password
        again = ask_yes_no("\nGenerate another password?")
        if not again:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()