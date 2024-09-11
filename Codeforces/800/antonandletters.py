s = input()

unique = set(filter(lambda x: x != '{' and x != '}' and x != ',' and x != ' ', s))

print(len(unique))