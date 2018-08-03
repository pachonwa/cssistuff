guess = raw_input("Let's play a game, pick a letter, any letter.")

word = ["programming"]

if guess == 'p' or guess == 'P':
        word.remove("e")
        word.insert(0, "p")
        print(word)
else:
    print("sorry,try again")
