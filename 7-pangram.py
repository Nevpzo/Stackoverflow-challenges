
import json

with open("CodingChallenge/List of 1000 strings.json", "r") as f:
    Strings = json.load(f)

def is_pangram(s):
    s = ''.join(e for e in s if e.isalnum())
    if not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower()):
        if len(s) == 26:
            return 'PP'
        return 'P'
    else:
        return False

pangrams = {'PP': 0, 'P': 0, False: 0}

for s in Strings:
    type = is_pangram(s)
    if type == 'PP':
        pangrams['PP'] += 1
    elif type == 'P':
        pangrams['P'] += 1
    else:
        pangrams[False] += 1

print(pangrams)