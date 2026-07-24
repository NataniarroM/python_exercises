filename = "the_three_musketeers.txt"

with open(filename, encoding="utf-8") as f_object:
    lines = f_object.readlines()

count = 0

for line in lines:
    count += line.lower().count("the")
    
print(count)