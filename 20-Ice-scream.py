from collections import defaultdict
import math

scoops = defaultdict(float)

def print_count(d):
    for flavour, tub_count in d.items():
        print(f"{flavour}: {tub_count}")

with open("./CodingChallenge/challenge_20_s1.txt") as f:
    for s in f:
        decomposition = s.strip().split(": ")
        guests = int(decomposition[1]) + 1  
        flavour = decomposition[2]

        scoops[flavour] += 1.5 * guests

tubs = {flavour: math.ceil(count / 9) for flavour, count in scoops.items()}

print_count(tubs)
