import random

missed_word_count = 0
used_words = list()
correct_words = list()
words = open('spellingbeewords.txt').read().split()

while len(used_words) <= len(words):
    random_word = random.choice(words)
    print(random_word, "\n")
    user_input = input("spell:\n")

    if user_input.lower() == random_word:
        print("You got it right! Nice Job")
        correct_words.append(user_input)
        used_words.append(user_input)
    else:
        print("You got it wrong!", missed_word_count)
        missed_word_count += 1
        used_words.append(user_input)

