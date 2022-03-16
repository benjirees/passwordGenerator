import random
import time

def password_generator(x):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','@','#','!','£',
                'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','#','!','£']
    
    password = []

    for i in range(x):
        letter = random.choice(alphabet)
        if i == 9:
            password.append('-')
        elif i == 10:
            password.append('@')
        elif i == 18:
            password.append('-')
        elif i == 20:
            password.append('@')
        elif i == 27:
            password.append('-')
        elif i == 30:
            password.append('@')
        else:
            password.append(letter)            
    
    userPassword = ''.join(password)
    return userPassword
    
def main():

    savedPasswords = []
    
    run = True

    while run:

        length = random.randint(35, 40)

        passwordGen = password_generator(length)

        print(f"\nPassword: {passwordGen}")

        again = input("\nWould you like to use this password? (Y/N): ").lower()
        if again == 'y':
            regenerate = input("\nWould you like to regenerate a password? (Y/N): ").lower()
            if regenerate == 'n':
                run = False
            elif regenerate == 'y':
                print("\nGenerating new password...")
                time.sleep(3)

            savedPasswords.append(passwordGen)
            
        elif again == 'n':
            print("\nGenerating new password...")
            time.sleep(3)

    view = input("\nType 'View' to see saved passwords: ").lower()
    if view == 'view':
        print('\n '.join(savedPasswords))

    google = {
            "googlePassword": ' '
        }
    youtube = {
            "youtubePassword": ' '
        }
    instagram = {
            "instagramPassword": ' '
        }

    assignment = True
    while assignment:
        passwordAssignment = input("\nWould you like to assign a saved password to an account? (Y/N): ").lower()
        if passwordAssignment == 'y':
            print(savedPasswords)
            accounts = input("\nPlease input the account you would assign a password to: ").lower() 
            if accounts == 'google':
                passwordGoogleChoice = int(input("\nPassword (1, 2, 3...): "))
                passwordGoogle = savedPasswords[passwordGoogleChoice-1]
                google["googlePassword"] = passwordGoogle
                outfile = open("passwords.txt", "w")
                outfile.write(f"Google Password: {passwordGoogle}")
                outfile.close()
            elif accounts == 'youtube':
                passwordYoutubeChoice = int(input("\nPassword (1, 2, 3...): "))
                passwordYoutube = savedPasswords[passwordYoutubeChoice-1]
                youtube["youtubePassword"] = passwordYoutube
                outfile = open("passwords.txt", "w")
                outfile.write(f"Youtube Password: {passwordYoutube}")
                outfile.close()
            elif accounts == 'instagram':
                passwordInstagramChoice = int(input("\nPassword (1, 2, 3...): "))
                passwordInstagram = savedPasswords[passwordInstagramChoice-1]
                instagram["instagramPassword"] = passwordInstagram
                outfile = open("passwords.txt", "w")
                outfile.write(f"Instagram Password: {passwordInstagram}")
                outfile.close()
        elif passwordAssignment == 'n':
            assignment = False

    viewAccount = input("\nView Password (Account): ").lower()

    if viewAccount == 'google':

        print(f'\nGoogle password: {google["googlePassword"]}')

    elif viewAccount == 'youtube':

        print(f'\nyoutube password: {youtube["youtubePassword"]}')

    elif viewAccount == 'instagram':

        print(f'\ninstagram password: {instagram["instagramPassword"]}')

main()

    
