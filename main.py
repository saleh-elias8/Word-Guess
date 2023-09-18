import random

LEXICON_FILE = "Lexicon.txt"    
INITIAL_GUESSES = 8 

def play(secret_word):
    g_word = ['-']* len(secret_word)
    g_left =  INITIAL_GUESSES

    while True:
        print('The word now looks like this:', ''.join(g_word))
        print('You have', g_left, 'guesses left')
        guess = input('Type a single letter here, then press enter: ').upper()

        if len(guess) != 1:
            print('Guess should only be a single character.')
            continue

        if guess in secret_word:
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    g_word[i] = guess
        else:
            print('There are no', guess + "'s in the word")
            g_left -= 1

        if '-' not in g_word:
            print('Congratulations, the word is:', secret_word)
            break

        if g_left == 0:
            print('Sorry, you lost. The secret word was:', secret_word)
            break


def get_word():
    with open(LEXICON_FILE, 'r') as file:
        word_list = file.read().splitlines()

    return random.choice(word_list)

def main():

    secret_word = get_word()
    play(secret_word)


if __name__ == "__main__":
    main()
