from collections import defaultdict
import csv

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