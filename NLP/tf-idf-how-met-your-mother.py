from collections import defaultdict
import csv
from sklearn.feature_extraction.text import TfidfVectorizer


episodes = defaultdict(list)
with open("data/import/sentences.csv", "r") as sentences_file:
    reader = csv.reader(sentences_file, delimiter=',')
    reader.next()
    for row in reader:
        episodes[row[1]].append(row[4])

for episode_id, text in episodes.iteritems():
    episodes[episode_id] = "".join(text)

corpus = []
for id, episode in sorted(episodes.iteritems(), key=lambda t: int(t[0])):
    corpus.append(episode)


tf = TfidfVectorizer(analyzer='word', ngram_range=(1,3), min_df = 0, stop_words = 'english')

tfidf_matrix =  tf.fit_transform(corpus)
feature_names = tf.get_feature_names() 

print ('=========================================')
print ('Length of Feature Names')
print ('\n')
print (len(feature_names))
print ('=========================================')
print ('Name of the Features')
print ('\n')
print (feature_names[50:70])
print ('=========================================')
dense = tfidf_matrix.todense()
print ('Lenght of the Dense Matrix')
print ('\n')
print (len(dense[0].tolist()[0]))
print ('=========================================')
print ('Lenght of Phrase Scores for the First Episode')
print ('\n')
episode = dense[0].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
print(len(phrase_scores))
print ('=========================================')
print ('Sort the Phrases by Score')
print ('\n')
print(sorted(phrase_scores, key=lambda t: t[1] * -1)[:5])
print ('=========================================')

print (feature_names[419207])

print (feature_names[312591])

print (feature_names[356632])

print ('=========================================')
print ('Terms and Scores: ')
print ('\n')

sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sorted_phrase_scores][:20]:
   print('{0: <20} {1}'.format(phrase, score))

print ('=========================================')
print ('Phrases which dont occur in other episodes')
print ('\n')

with open("data/import/tfidf_scikit.csv", "w") as file:
    writer = csv.writer(file, delimiter=",")
    writer.writerow(["EpisodeId", "Phrase", "Score"])

    doc_id = 0
    for doc in tfidf_matrix.todense():
        print "Document %d" %(doc_id)
        word_id = 0
        for score in doc.tolist()[0]:
            if score > 0:
                word = feature_names[word_id]
                writer.writerow([doc_id+1, word.encode("utf-8"), score])
            word_id +=1
        doc_id +=1
print ('=========================================')