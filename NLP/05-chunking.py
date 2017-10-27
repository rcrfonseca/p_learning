#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sentence_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>} """

			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)

			#print(chunked)

			chunked.draw()






	except Exception as e:
		print(str(e))

process_content()

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
