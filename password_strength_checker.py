import string

#load the list of common passwords
def load_wordlists(wordlist_path):
    common_passwords = []
    try:
        with open(wordlist_path,'r') as f:
            for password in f.read():
                common_passwords.append(password.strip())
    except FileNotFoundError:
        print("The wordlist not found!")
    return common_passwords

#scoring the password strength
def score_password(password, wordlists):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("The password should be at least 8 characters")

    #extra score
    if len(password) >= 12:
        score += 1
    
    if any(c in string.digits for c in password):
        score += 1
    else:
        feedback.append("The password should contain one numeric value")

    if any(c in string.ascii_uppercase for c in password):
        score += 1
    else:
        feedback.append("The password should contain one uppercase character")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("The password should contain at least one special character")
    
    if password in wordlists:
        score = 0
        feedback = ["The password is already in common password list please use another passowrds"]
    
    return score, feedback

def main():

    score_label = {1:'poor', 2:'weak', 3: 'good', 4:'strong', 5: 'very strong' }
    while True:
        password_list = load_wordlists("common_passwords.txt")  #change the passwords list path/name if needed
        user_pass = str(input("Enter the your password (q - quit): "))
        if len(user_pass) == 0:
            print("The password can't be empty!")
            continue
        if user_pass.lower().strip() == 'q':
            print("Bye!!")
            break

        score, feedback = score_password(user_pass, password_list)
        print(f"Your password is : {score_label.get(score, 'very poor')} and score is: {score/5}")
        print("Here is the Feedback:")
        for tip in feedback:
            print(f"- {tip}")


main()