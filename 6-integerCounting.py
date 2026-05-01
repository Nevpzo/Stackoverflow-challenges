import timeit

Numbers = []
with open('CodingChallenge/1M_random_numbers.txt') as fv:
    for row in fv:
        Numbers.extend(map(int, row.split()))
        
freq = {}
mostNum = 0

start = timeit.default_timer()

for n in Numbers:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

mostFreq = max(freq, key=freq.get)
mostNum = max(freq.values())

stop = timeit.default_timer()

print(f'Most frequent key, {mostFreq}, seen {mostNum} times.')
print('Time: ', stop - start, 's')  