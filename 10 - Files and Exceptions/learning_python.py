filename = "learn_python.txt"

with open(filename) as file_object:
    content = file_object.read()
    print(content)

with open(filename) as file_object:
    lines = file_object.readlines()

text = ""
for line in lines:
    text += line.replace("C", "Python")

print(text)