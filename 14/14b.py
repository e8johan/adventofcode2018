target_string = raw_input("Target string? ")

target_values = []
for c in target_string:
    target_values.insert(0, int(c))

class Node:
    def __init__(self, v, n, p):
        self.v = v
        self.n = n
        self.p = p

# Initialize list
first = Node(3, None, None)
last = Node(7, first, first)
first.n = last
# first.p is None on purpose

elves = [None] * 2
elves[0] = first
elves[1] = last

added_nodes = 0
no_of_recipes = 2
while True:
    # Calculate next recipe
    recipe = 0
    for e in elves:
        recipe += e.v
    recipe_string = str(recipe)
    
    # Append it
    added_nodes = 0
    for c in recipe_string:
        n = Node(int(c), last.n, last)
        last.n = n
        last = n
        no_of_recipes += 1
        added_nodes += 1

    # Find the numbers - it does not have to be last
    found = True
    while added_nodes > 0:
        added_nodes -= 1
        current = last

        for i in range(added_nodes):
                if current.p:
                    current = current.p
                else:
                    found = False
                    break

        for v in target_values:
            if not current.v == v:
                found = False
                break
            else:
                if current.p:
                    current = current.p
                else:
                    found = False
                    break
            
        if found:
            break
    if found:
        break
    
    # Move elves
    for i in range(len(elves)):
        e = elves[i]
        steps = e.v + 1
        while steps > 0:
            e = e.n
            steps -= 1
        elves[i] = e

print no_of_recipes - len(target_string) - added_nodes
