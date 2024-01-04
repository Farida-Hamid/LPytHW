from sys import argv

script, filenamem = argv

txt = open(filenamem)

print(f"Here's your file {filenamem}\n")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())