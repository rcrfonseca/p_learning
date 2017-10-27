#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

#example_words = "python","pythonly","pythoner","pythoning","pythoned"
example_text = "With","this","line","strings","of","length","don't","go","through","the","stemming","process"

print(example_text)

for w in example_text:
	print(ps.stem(w))


# #print(sent_tokenize(example_text))

# stop_words = set(stopwords.words("portuguese"))

# words = word_tokenize(example_text)

# filtered_sentence = []

# for w in words:
# 	if w not in stop_words:
# 		filtered_sentence.append(w)

# print(example_text)
# print("\n")
# print(filtered_sentence)
# print("\n")
# print(stop_words)


# #print(stop_words)

# #print(word_tokenize(example_text))

# #for i in word_tokenize(example_text):
# #	print(i)
