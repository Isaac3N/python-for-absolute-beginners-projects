# write it
# demonstrates writing to a text file

print("Creating a text file with the write() method")
text_file= open("write_it.txt", "w")
text_file.write("line 1\n")
text_file.write("this is line 2\n")
text_file.write("that makes this line threee\n")
text_file.close()

print("\nreading the newly created file.")
text_file= open("write_it.txt", "r")
print(text_file.read())
text_file.close()
