#this program demos the use of the methods that add, remove, identify, count, and organize list items

cats = ['BT', 'Grits', 'Meow', 'Salty']
print(cats)
print("\nThis is the second cat in the list:")
print(cats[1])
print("\nThis is the last cat in the list:")
print(cats[-1])
print("\nThis changes the first cat in the list:")
cats[0] = 'Gravy'
print(cats)
print("\nThis adds a cat to the end of the list")
cats.append('BT')
print(cats)
print("\nThis adds a cat wherever you want:")
cats.insert(2,'Biscuit')
print(cats)
print("\nThis removes a cat from the list:")
del cats[2]
print(cats)
print("\nThis removes a cat, but saves for later use")
popped_cat = cats.pop(0)
print(popped_cat + " was removed from the cat list.")
print("\nYou can also use remove to take away cats by name")
removed_cat = 'Salty'
cats.remove(removed_cat)
print(cats)
print("\nI removed " + removed_cat + " from the list.")

cats = ['BT', 'Grits', 'Meow', 'Salty']
cats.sort(reverse=True)
print("\nHere is the cat list in reverse order")
print(cats)
print("\nHere's a temp version of the list:")
print(sorted(cats))
print("\nHere's the reversed list again:")
print(cats)
print("\nHere's use of the reverse method:")
cats.reverse()
print(cats)
cat_length = len(cats)
print("\nThere are " + str(cat_length) + " cats in the list.")