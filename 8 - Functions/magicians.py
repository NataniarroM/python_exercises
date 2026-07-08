def show_magicians(names):
    for name in names:
        print(name)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"Great {magicians[i]}"
    return magicians
    

magicians = ["David", "John", "Will"]
new_magicians = make_great(magicians[:])


show_magicians(magicians)
show_magicians(new_magicians)