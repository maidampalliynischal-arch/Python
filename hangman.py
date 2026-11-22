import random
from caselist import words

hangman_art = {
               0: ("   ",
                   "   ",
                   "   ",
                   "   "),
               1: (" | ",
                   "   ",
                   "   ",
                   "   "),
               2: (" | ",
                   " o ",
                   "   ",
                   "   "),
               3: (" | ",
                   " o ",
                   " | ",
                   "   "),
               4: (" | ",
                   " o ",
                   " | ",
                   "/  "),
               5: (" | ",
                   " o ",
                   " | ",
                   "/ \\"),
               6: (" | ",
                   " o ",
                   "/| ",
                   "/ \\"),
               7: (" | ",
                   " o ",
                   "/|\\",
                   "/ \\")}
for line in hangman_art[7]:
    print(line)

def choose_word_type():
    print("Choose a word type:")
    type = input("1. Fruits\n2. Animals\n3. Countries\nEnter the number of your choice: ")
    answer = random.choice(list(words.values())[int(type) - 1])
    return answer
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_ans(answer):
    print(" ".join(answer))

def main():
    answer = choose_word_type()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
#        display_ans(answer)
        guess = input("enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue
        if guess in guessed_letters:
            print(f"{guess} is already placed try another")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if '_' not in hint:
            display_man(wrong_guesses)
            display_ans(answer)
            print("YOU WIN!")
            is_running = False 
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_ans(answer)            
            print("YOU LOST!")
            exit()
if __name__ == "__main__":
    main()
