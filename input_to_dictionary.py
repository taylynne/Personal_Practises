definitions = {}

# information about the loop/'program' if you will...

msg = "We'll create a dictionary from the words and definitions you provide me"
msg += "\n you can type 'q' at any time to quit!"

print(msg)

while True:
    key = input("\nWhat is the word you would like to define? ")
    if key.lower() == "q":
        break
    value = input("And what is the definition for that word? ")
    if value.lower() == "q":
        break
    definitions[key.capitalize()] = value

print("\nHere's our 'homemade' dictionary!:")
print(definitions)