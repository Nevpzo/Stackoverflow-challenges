from nltk.corpus import wordnet as wn
import json

MIN_LEN = 4

with open('./CodingChallenge/words.txt') as f:
    words = f.read().split()

POS_words = {
    "noun": [],
    "verb": [],
    "adje": [],
    "short": [],
    "trash": []
}

for word in words:

    if len(word) <= MIN_LEN:
        POS_words["short"].append(word)
        continue

    synsets = wn.synsets(word)

    if not synsets:
        POS_words["trash"].append(word)
        continue

    pos_set = {s.pos() for s in synsets}

    if 'n' in pos_set:
        POS_words["noun"].append(word)

    if 'v' in pos_set:
        POS_words["verb"].append(word)

    if 'a' in pos_set or 's' in pos_set:
        POS_words["adje"].append(word)

    if not {'n', 'v', 'a', 's'} & pos_set:
        POS_words["trash"].append(word)

with open("./CodingChallenge/POS_words.json", "w") as f:
    json.dump(POS_words, f, indent=4)
