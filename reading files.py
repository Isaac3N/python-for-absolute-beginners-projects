# read it
# demonstrates reading from a text file

print("opening and a closing file.")
text_file= open("readit.txt", "r")
text_file.close()

print("\nReading characters from a file.")
text_file= open ("readit.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading the entire file at once.")
text_file = open("readit.txt","r")
whole_thing= text_file.read()
print(whole_thing)
text_file.close() 

print("\nReading characters from a line.")
text_file= open("readit.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time.")
text_file= open("readit.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()


print("\nReading the entire file into a list.")
text_file= open("readit.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print (line)
text_file.close()

print("\nlooping through a file line by line")
text_file= open("readit.txt", "r")
for line in text_file:
    print (line)
text_file.close()
