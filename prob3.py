people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# Use a lambda function as the sorting key
sorted_people = sorted(people, key=lambda x: x[0])
print(sorted_people)
