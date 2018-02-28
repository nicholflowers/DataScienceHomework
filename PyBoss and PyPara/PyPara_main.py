import os
#with open('paragraph_1.txt', 'r') as file:

# store file path
file = 'paragraph_1.txt'

# declare variables
letter_count = 0
word_count = 0
sentence_count = 0

# open file
with open(file, 'r') as txtfile:
    # read file
    paragraph = txtfile.read()

    # find word count
    word_count = paragraph.count(" ") + 1 # +1 to account for the last word

    # find sentence count
    sentence_count = paragraph.count(".") + paragraph.count("!") + paragraph.count("?")

    # find average letter count
    for character in paragraph:
        if character.isalpha():
            letter_count += 1 # counting how many characters are letters
    avg_letter_count = letter_count/word_count

    # find average sentence length
    avg_sentence = word_count/sentence_count

# validate
# print(word_count)
# print(sentence_count)
print(letter_count)
# print(avg_letter_count)
# print(avg_sentence)

# print results to terminal
print("Paragraph Analysis")
print("----------------------------------")
print("Approximate Word Count:", word_count)
print("Approximate Sentence Count:", sentence_count)
print("Average Letter Count:", avg_letter_count)
print("Average Sentence Length:", avg_sentence)
