#this program demos the different ways to remove list items

guest_list = ['Jenn', 'Kathy', 'BT']
guest_list.insert(0, 'Meow')
guest_list.insert(2, 'Layla')
guest_list.append('Tanner')

print("Change of plans, only 2 people can come...")

person_removed = guest_list.pop()
print("Sorry, " + person_removed + " you cannot come.")

person_removed = guest_list.pop()
print("Sorry, " + person_removed + " you cannot come.")

person_removed = guest_list.pop()
print("Sorry, " + person_removed + " you cannot come.")

person_removed = guest_list.pop()
print("Sorry, " + person_removed + " you cannot come.")

print(guest_list[0] + ", you're still invited!")

print(guest_list[1] + ", you're still invited!")

del guest_list[0]
print(guest_list)

del guest_list[0]
print(guest_list)