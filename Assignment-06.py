'''
Student Name: K. Nikhitha
Student Id: 00983208
course: CSCI6651 Introduction to Python Programming
Git Repository: https://github.com/katragaddanikhitha/Python_projects

'''
def get_nonempty(prompt):
# Prompt until a non-empty input is received
    while True:
        value = input(prompt).strip()
        if value:
            return value
# else prompt again
        print(f"{prompt.split(':')[0]} cannot be empty. Try again.")
# Function to check if username already exists
def username_exists(users, username):
# Check if username exists in users dictionary (case-insensitive)
    for existing_username in users:
#Dictionary to check existing usernames
        if existing_username.lower() == username.lower():
            return True
    return False
# Prompt until a unique username is entered
def get_unique_username(users):
# Loop until a unique username is provided
    while True:
        username = input("Username: ").strip()
        if not username:
            print("Username cannot be empty. Try again.")
            continue
        if username_exists(users, username):
            print("Username is taken; please try another.")
            continue
        return username
# Prompt until password is entered twice and matches
def get_password():
    while True:
        pwd1 = input("Password: ").strip()
        pwd2 = input("Re-enter password: ").strip()
        if not pwd1 or not pwd2:
            print("Password cannot be empty. Try again.")
            continue
        if pwd1 != pwd2:
            print("Passwords do not match. Try again.")
            continue
        return pwd1
# Main application loop
def main():
    users = {}

    while True:
        print("Application Start!\r\n")

        first = get_nonempty("First name: ")
        last = get_nonempty("Last name: ")
        username = get_unique_username(users)
        password = get_password()
# Display proposed account with masked password
        masked = "*" * len(password)
        print(f"\nProposed account:")
        print(f" Username: {username}")
        print(f" Name: {last}, {first}")
        print(f" Password: {masked}")
# confirm to accept
        accept = input("Accept? (y/n): ").strip().lower()
        if accept == 'y':
# add to users dictionary
            users[username] = {
                "first_name": first,
                "last_name": last,
                "password": password
            }
            print("Account added.")
        else:
            print("Account discarded.")

# prompt to quit or continue
        quit_choice = input("Quit? (q to exit, any other key to continue): ").strip().lower()
        if quit_choice == 'q':
            print("Quitting Application!\r\n")
            break
# Final display of users dictionary
    print("\nFinal users dictionary:")
    print("Format: username → {first_name, last_name, password}\r\n")
    print(users)
# End of main()
if __name__ == "__main__":
    main()
