import random

value = random.random()  # generate random float between [0.0 to 1.0]
print(value)
value = random.uniform(1, 10)  # generates a random float N ∈ (a <= N <= b)
print(value)
dice = random.randint(1, 6)  # generate a random integer between  1 to 6
print(dice)

greetings = ['Hello', 'Hi', 'Hey', 'Hola', 'Howdy', 'Namastey']
value = random.choice(greetings)  # returns a random element from the sequence
print(value + ', Kamal!')

colors = ['Red', 'Green', 'Black']
results = random.choices(colors, weights=[18, 18, 2], k=10)  # returns a k sized list of sequence
print(results)

deck = list(range(1, 53))
random.shuffle(deck)  # shuffle the sequence
hand = random.sample(deck, k=5)  # returns k sized list of unique elements from the sequence
print(hand)
