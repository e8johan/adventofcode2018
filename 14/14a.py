learning_time = int(raw_input("Number of recipes to learn? "))

class Node:
    def __init__(self, v, n):
        self.v = v
        self.n = n

# Initialize list
first = Node(3, None)
last = Node(7, first)
first.n = last

elves = [None] * 2
elves[0] = first
elves[1] = last

no_of_recipes = 2
while no_of_recipes < learning_time + 10:
    # Calculate next recipe
    recipe = 0
    for e in elves:
        recipe += e.v
    recipe_string = str(recipe)
    
    # Append it
    for c in recipe_string:
        n = Node(int(c), last.n)
        last.n = n
        last = n
        no_of_recipes += 1
    
    # Move elves
    for i in range(len(elves)):
        e = elves[i]
        steps = e.v + 1
        while steps > 0:
            e = e.n
            steps -= 1
        elves[i] = e

current = first
for i in range(learning_time):
    current = current.n
    
res = ""
for i in range(10):
    res += str(current.v)
    current = current.n

print res
