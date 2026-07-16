filename = "pi.txt"

"""with open(filename) as file_object:
#    contents = file_object.read()
    for line in file_object:
        print(line.rstrip())"""

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

birthdate = input("Digite o seu aniversário mmddyy: ")
if birthdate in pi_string:
    print("Yes")
else:
    print("no")