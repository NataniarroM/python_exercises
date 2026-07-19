filename = "well.txt"

with open(filename, "a") as file_object:
    file_object.write("I love this\n")
    file_object.write("Just because I love it\n")

print("Made it")

with open(filename, "w") as file_object:
    file_object.write("HAHAHAHA")