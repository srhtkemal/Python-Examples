text = open(
    "C:/Users/serha/Desktop/Python Examples/lecture_01/text_example.txt", encoding="utf8")

text = str(text.read())
text_split = text.split()
word_count = int(0)
character_count=int(0)
longest_word = text_split[0]
shortest_word = text_split[0]
most_common_word = text_split[0]
most_common_word_count = int(0)
count_of_each_word = {}

print(text_split)

for i in text_split:
    if (len(i) > len(longest_word)):
        longest_word = i
    if (len(i) < len(shortest_word)):
        shortest_word = i
    word_count += 1
    character_count+=len(i)
    if i in count_of_each_word:
        count_of_each_word[i] += 1
    else:
        count_of_each_word[i] = 1

    for word, word_count in count_of_each_word.items():
        if (word_count > most_common_word_count):
            most_common_word_count = word_count
            most_common_word = word

print(f"--- Text Report ---\n"
      f"Total Word Count: {word_count}\n"
      f"Total Character Count: {character_count}\n"
      f"Longest Word is: {longest_word}\n"
      f"Shortest Word is: {shortest_word}\n"
      f"Most Common Word is: {most_common_word} (Found {most_common_word_count} times)")
