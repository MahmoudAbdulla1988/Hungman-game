import random
options = ['python', 'java', 'kotlin', 'javascript']
chossed_word = list(random.choice(options))
dash_word = '-' * len(chossed_word)
correct_word = list(dash_word)
typed_letter = set()
print('H A N G M A N')
user_selection = str(input('Type "play" to play the game, "exit" to quit:'))

if user_selection == "play":
    print(dash_word)
    count = 0
    while count < 8:
        inpute_letter = str(input("Input a letter:"))
    

        if inpute_letter in correct_word or inpute_letter in typed_letter:
                print('You already typed this letter')
                typed_letter.add(inpute_letter)

        if not inpute_letter.islower():
            print('It is not an ASCII lowercase letter')
            typed_letter.add(inpute_letter)

        if len(inpute_letter) > 1 or inpute_letter == 0:
            print('You should print a single letter')
            typed_letter.add(inpute_letter)   

        if inpute_letter in chossed_word and inpute_letter not in typed_letter:
            for i in range(len(chossed_word)):
                if chossed_word[i] == inpute_letter:
                    correct_word[i] = inpute_letter
    
        if inpute_letter not in chossed_word and inpute_letter not in typed_letter:
            count += 1
            typed_letter.add(inpute_letter)
            if count <= 7:
               print('No such letter in the word')
            if count > 7 and correct_word != chossed_word:
                print(*correct_word, sep = "")
                print('No such letter in the word')
                print('You are hanged!')
                print()
                break
       
        if correct_word == chossed_word:
            print(*correct_word, sep = "")
            print('You guessed the word!\nYou survived!')
            print()
            break
    
        print()
        print(*correct_word, sep = "")
else:
    if user_selection == "exit":
        user_selection = str(input('Type "play" to play the game, "exit" to quit:'))