#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Nunca vou perdoar Nicki Minaj por ter desperdiçado Get On Your Knees"

print(sent_tokenize(example_text))

print(word_tokenize(example_text))

for i in word_tokenize(example_text):
	print(i)

