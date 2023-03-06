# Solving Problems using Dictionary in Python
#Emoji Converter
message = input("> ")
words = message.split(' ')
emojis = {
  ":)": "🙂",
  ":(": "😏"
}
output = ""
for word in words:
  output += emojis.get(word, word) + " "
print(output)

# Write a program that covert numbers to words using a dictionary
numbers = input("Phone number: ")
digits_mapping = {
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four",
  "5":"five",
  "6":"six",
  "7":"seven",
  "8":"eight",
  "9":"nine",
  "10":"ten",
  "0":"zero"
}
output = " "
for charater in numbers:
    output += digits_mapping.get(charater, "!" + " ")
print(output)
