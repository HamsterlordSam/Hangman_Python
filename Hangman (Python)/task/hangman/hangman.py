from random import choice


def put_letter(letter, dest_word, word):
    if letter not in word:
        return False
    else:
        found, index = 0, 0
        while index != -1:
            index = word.find(letter, found)
            found = index + 1
            if index == -1:
                continue
            dest_word[index] = letter
        return True


# Main game code block
game_title = "H A N G M A N "
print(game_title)
words_list = ['python', 'java', 'swift', 'javascript']
win_counter = 0
loss_counter = 0
while True:
    attempts = 8
    guessed_letters = set()
    menu_answer = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if menu_answer == 'exit':
        break
    elif menu_answer == 'results':
        print(f"You won: {win_counter} times.")
        print(f"You lost: {loss_counter} times.")
        continue
    elif menu_answer == 'play':
        guess_word = choice(words_list)  # randomly picks a guess word from words list
        hint_word = ('-' * len(guess_word))
        hint_word = list(hint_word)
        while attempts and '-' in hint_word:
            print()
            print(*hint_word, sep='')
            user_letter = input('Input a letter:')
            if len(user_letter) != 1:
                print("Please, input a single letter.")
                continue
            if not user_letter.islower():
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            if user_letter not in guessed_letters:
                guessed_letters.add(user_letter)
            else:
                print("You've already guessed this letter.")
                continue
            if not put_letter(user_letter, hint_word, guess_word):
                print("That letter doesn't appear in the word.", "#", attempts, "attempts")
                attempts -= 1
        if attempts > 0:
            print(f"You guessed the word {guess_word}!")
            print("You survived!")
            win_counter += 1
        else:
            print("You lost!")
            loss_counter += 1
