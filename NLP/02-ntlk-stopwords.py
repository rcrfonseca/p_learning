#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_text = "Nunca vou perdoar Nicki Minaj por ter desperdiçado Get On Your Knees"

#print(sent_tokenize(example_text))

stop_words = set(stopwords.words("portuguese"))

words = word_tokenize(example_text)

filtered_sentence = []

for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print(example_text)
print("\n")
print(filtered_sentence)
print("\n")
print(stop_words)


#print(stop_words)

#print(word_tokenize(example_text))

#for i in word_tokenize(example_text):
#	print(i)
