filename = "learn_python.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

with open(filename) as file_object:
    content = file_object.read()
    print(content)

text = ""
for line in lines:
    text += line

print(text)

