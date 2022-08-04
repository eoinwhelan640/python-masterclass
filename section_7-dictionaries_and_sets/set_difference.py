from primes_and_squares import squares_generator,primes_generator

evens = set(range(0,50,2))
odds = set(range(1,50,2))
print(evens,odds,sep="\n")

primes = set(primes_generator(100))
squares = set(squares_generator(100))

print(odds.difference(primes))

print(odds - primes)