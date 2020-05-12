from collections import Counter

non_letters=["1","2","3","4","5","6","7","8","9","0",":",";"," ","/n",".",","]
key_phrase_1=input("Enter the phrase:").lower()

#Removing non letters from phrase
for non_letters in non_letters:
    key_phrase_1=key_phrase_1.replace(non_letters,'')
total_occurences=len(key_phrase_1)

#Counter object
"""""A Counter is a collection where elements are stored as dictionary keys and their
counts are stored as dictionary values. Counts are allowed to be any integer
value including zero or negative counts.
"""
letter_count=Counter(key_phrase_1)
print("frequency analysisfrom the phrase:")
for key,value in sorted(letter_count.items()):
    percentage=100 * value/total_occurences
    percentage=round(percentage,2)
    print("\t \t"+key+"\t\t"+str(value)+"\t\t"+str(percentage))
ordered_letter_count=letter_count.most_common()
key_phrase_1_ordered_letters=[]
for pair in ordered_letter_count:
    key_phrase_1_ordered_letters.append(pair[0])
print("letters from high occurence to lower occurence:")
for letter in key_phrase_1_ordered_letters:
    print(letter, end='')
key_phrase_2 = """
Quite so! You have not observed. And yet you have seen.
That is just my point. Now, I know that there are seventeen steps, because I
have both seen and observed.
By the way, since you are interested in these little problems,
and since you are good enough to chronicle one or two of my trifling
experiences, you may be interested in this.
He threw over a sheet of thick, pink tinted notepaper which had been lying open
upon the table.
It came by the last post, said he. Read it aloud.
The note was undated, and without either signature or address.
There will call upon you tonight, at a quarter to eight o'clock,
it said, "a gentleman who desires to consult you upon a matter of the very
deepest moment."""
key_phrase_2 = key_phrase_2.lower()
#Removing all non letters from key_phrase_2
for non_letter in non_letters:
 key_phrase_2 = key_phrase_2.replace(non_letter, '')
total_occurrences = len(key_phrase_2)
#Create a counter object to tally the number of each letter
letter_count = Counter(key_phrase_2)
#Determine the frequency analysis for the message
print("\n\nHere is the frequency analysis from key phrase 2: ")
print("\n\tLetter\t\tOccurrence\tPercentage")
for key, value in sorted(letter_count.items()):
 percentage = 100*value/total_occurrences
 percentage = round(percentage, 2)
 print("\t" + key + "\t\t" + str(value) + "\t\t" + str(percentage) + "%")
 ordered_letter_count = letter_count.most_common()
key_phrase_2_ordered_letters = []
for pair in ordered_letter_count:
 key_phrase_2_ordered_letters.append(pair[0])
#Print the list
print("\nLetters ordered from highest occurrence to lowest: ")
for letter in key_phrase_2_ordered_letters:
 print(letter, end='')
#Encode/Decode a given message using key_phrase_1 and key_phrase_2
choice = input("\n\nWould you like to encode or decode a message: ").lower()
phrase = input("What is the phrase: ").lower()
#Removing all non letters from the users phrase
for non_letter in non_letters:
 phrase = phrase.replace(non_letter, '')
user_input=input("Encode or Decode").title()
encode_msg=input("Enter the message:").lower()
for non_letters in non_letters:
    encode_msg=encode_msg.replace(non_letters,'')
if user_input=="encode":
    encode_phrase=[]
    for letter in encode_msg:
        index=key_phrase_1_ordered_letters.index(letter)
        letter=key_phrase_2_ordered_letters[index]
        encode_phrase.append(letter)
        print("\nThe encoded message is: ")
        for letter in encode_phrase:
            print(letter, end='')
elif user_input=="decode":
    decoded_phrase = []
    for letter in phrase:
        index = key_phrase_2_ordered_letters.index(letter)
    letter = key_phrase_1_ordered_letters[index]
    decoded_phrase.append(letter)
    print("\nThe decoded message is: ")
    for letter in decoded_phrase:
        print(letter, end='')
    # User entered an invalid option
    else:
        print("Please type 'encode' or 'decode'.Try again. ")
