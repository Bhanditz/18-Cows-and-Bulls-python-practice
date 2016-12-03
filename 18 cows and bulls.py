import random
import sys

def main():
    
    print('----------------------')
    print('Rules:')
    print('----------------------')
    print('For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.')
    print('----------------------')
    
    number = get_number()
    
    
    number = ''.join(str(e) for e in number)
   

    cow = 0
    bull = 0
    guesses = 0
    
    while cow < 4:
        user_number = ask_user()
        
        cow = 0
        bull = 0
        for i in range(0,4):
          
            if number[i] == user_number[i]:
                cow += 1

            if number[i] != user_number[i]:
                if number[i] == user_number[0]:
                    bull+=1
                elif number[i] == user_number[1]:
                    bull+=1
                elif number[i] == user_number[2]:
                    bull+=1
                elif number[i] == user_number[3]:
                    bull+=1
            
        print('There were ',cow,'cows and ',bull,' bulls')
        print('')
        guesses+=1
        #user_number = ask_user()
    if cow == 4:
        print('You win.')
        print('It took you ',guesses,' guesses.')
        sys.exit()
        
    

def get_number():
    random_number = []
    #Get the 4 digit number for the game
    for i in range(4):
        num = random.randint(0,9)
        random_number.append(num)

    return random_number

def ask_user():
    #Get the 4 digit number from the user
    user_number = input('Enter a 4 digit number: ')
    stringNumber = str(user_number)
    
    return stringNumber


main()
