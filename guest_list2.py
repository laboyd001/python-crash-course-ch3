#this program demos a list and a way to add and remove items

guest_list = ['Jenn', 'Kathy', 'BT']
cannot_attend = guest_list.pop(0)
print(cannot_attend + " is unable to attend.")
new_guest = guest_list.append('Salty')
print(guest_list[0] + ", you're invited!")
print(guest_list[1] + ", you're invited!")
print(guest_list[2] + ", you're invited!")


