import nltk
from itertools import product
from nltk.corpus import reuters
corpus = [w.casefold() for w in reuters.words() if len(w)== 5]
corpus.append('shard')

alphabet = "abcdefghijklmnopqrstuvwxyz"
one = 's'
two = alphabet
three = alphabet
four = ''.join([l for l in alphabet if not l in "pnle"])
five = 'd'

loop=0
# Wordle
print('Have letters [s][][][][d]')
print("-"*80)
for a,b,c,d,e in product (one, two, three, four, five):
    loop += 1
    word = a+b+c+d+e
    if word in corpus:
        print(a+b+c+d+e)
    if loop % 2000 == 0:
        print('{} letter combinations checked'.format(loop))
