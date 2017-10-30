#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Related to stemming, but the final result of the operation 
# is a real word, a synonym or closest to the input word.

import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better", pos="a"))


# ps = PorterStemmer()

# #example_words = "python","pythonly","pythoner","pythoning","pythoned"
# example_text = "With","this","line","strings","of","length","don't","go","through","the","stemming","process"

# print(example_text)

# for w in example_text:
# 	print(ps.stem(w))


# # #print(sent_tokenize(example_text))

# # stop_words = set(stopwords.words("portuguese"))

# # words = word_tokenize(example_text)

# # filtered_sentence = []

# # for w in words:
# # 	if w not in stop_words:
# # 		filtered_sentence.append(w)

# # print(example_text)
# # print("\n")
# # print(filtered_sentence)
# # print("\n")
# # print(stop_words)


# # #print(stop_words)

# # #print(word_tokenize(example_text))

# # #for i in word_tokenize(example_text):
# # #	print(i)
