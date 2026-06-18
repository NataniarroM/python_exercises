guests = ["J. R. R. Tolkien", "Olavo de Carvalho", "Graciliano Ramos"]
invitation = ' I would like to invite you to dinner with me'

print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)

print('\n')
print("Unfortunately, " + guests[0] + " couldn't make it")
guests[0] = "José Geraldo Vieira"

print('\n')
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)

guests.insert(0, 'Fyodor Dostoevsky')
guests.insert(2, 'Machado de Assis')
guests.append('Jane Austen')

print('\n')
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(guests[5] + invitation)

print('\n')
print('Sorry, can invite only two of you')

message = "Forgive me, you can't come "
print(message + guests.pop())
print(message + guests.pop())
print(message + guests.pop())
print(message + guests.pop())

second_invitation = 'You still may come '
print(second_invitation + guests[0])
print(second_invitation + guests[1])

del guests[0]
del guests[0]
print(guests)