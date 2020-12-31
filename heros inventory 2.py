#  heros inventory 2.0
# demonstrates tuples

# create a tuple with some items and displays with a for loop
inventory = ("sword",
             "armour",
             "shield",
             "healing potion")
print ( "your items:")
for item in inventory:
    print ( item )

input (" pls press the enter key to continue.")
# get the lenght of a tuple
print (" you have", len(invenntory),"items with you")

input ("\n Press the enter key to continue")

# test for membership with in
if "healing potion" in inventory :
    print ("you will live to fight another my great hero")

    
# display one item through an index
index = int (input ("\n Enter the index number for an item inventory: ")
print("At index", index, "is", inventory[index])

# display a slice
start = int(input ("\n Enter the index number to begin a slice.")
finsh = int (input ("\n Enter the index number to end a slice .")
print ("inventory [" , start, ":", finish,"]is" end = "" )
print ( inventory [start:finish})

input ( "\n Press the enter key to continue.")

# concatenating two tuple

chest = ( "gold", "gems")
print (" you find a chest .  it contains : ")
print (chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print("Your inventory is now:")
print(inventory)
input("\n\nPress the enter key to exit.")

             

