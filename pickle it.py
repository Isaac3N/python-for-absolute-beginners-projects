# pickle it
# demonstrates pickling and shelving data


import pickle, shelve
print("pickling lists.")
variety= ["sweet", "hot", "dill"]
shape= ["whole", "spear", "chip"]
brand=["heinz","claussen","vlassic"]

f = open("pickle_it.dat", "wb")

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("\nUnpickling lists")
f = open("pickle_it.dat", "rb")
variety= pickle.load(f)
shape= pickle.load(f)
brand= pickle.load(f)

print(variety)
print(brand)
print(shape)
f.close()

print("\nShelving lists")
s = shelve.open("pickle2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s.sync()

print("\nRetrieving lists from a shelved file:")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])

s.close()
