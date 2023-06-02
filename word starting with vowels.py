import re


def starting_with_vowels(sentence: str):
    list_of_words = sentence.split(" ")
    pattern = r'[aeiouAEIOU].*?'
    count = 0
    for word in list_of_words:
        if re.match(pattern, word):
            count += 1
    return f'number of word starting with vowels: {count}'


print(starting_with_vowels("If you end up not succeeding with any small or big amount of success with achieving any "
                           "one of your goals, it’s time to change the plan, not the goal nor to give up on it in any "
                           "way. Nothing is impossible and you can achieve anything as long as you set your mind to "
                           "it and don’t give up."))
