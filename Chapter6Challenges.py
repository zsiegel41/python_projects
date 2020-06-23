string_ex = "Camus"
print(string_ex[0])
print(string_ex[1])
print(string_ex[2])
print(string_ex[3])



first_string = input("Enter a word: ")
second_string = input("Enter another word: ")

print("Yesterday I wrote a {}. I sent it to {}!".format(first_string, second_string))


fact = "aldous Huxley was born in 1894.".capitalize()
print(fact)


x = "Where now? Who now? When now?".split("?")
print(x)


word_list = ["The",
             "fox",
             "jumped",
             "over",
             "the",
             "fence",
             "."
             ]
word_list[5] = word_list[5]+word_list[6]
word_list.pop()
sentence = " ".join(word_list)
print(sentence)


poem = "A screaming comes across the sky."
poem = poem.replace("s", "$")
print(poem)


author = "Hemingway"
print(author.index("m"))
print(author.find("m"))

dialogue = "\"Find some dialogue,\" said Snape. \"No!\" Harry screamed."
alt_dialogue = "'Find some dialogue,' said Snape. 'No!' Harry screamed."
print(dialogue)


three = "three "
print(three + three + three)
print(three * 3)

story = """It was a bright cold day in April,
        and the clocks were striking thirteen."""
n = story.index(",")
story = story[:n]
print(story)
