"""
                                                    Encryption

In case of encryption we extract each character (if not a space) from a word one at a time and match it with its
corresponding morse code stored in whichever data structure we have chosen(if you are coding in python, dictionaries
can turn out to be very useful in this case)
Store the morse code in a variable which will contain our encoded string and then we add a space to our string which will contain the result.
While encoding in morse code we need to add 1 space between every character and 2 consecutive spaces between every word.
If the character is a space then add another space to the variable containing the result. We repeat this process till
we traverse the whole string

                                                    Decryption

In case of decryption, we start by adding a space at the end of the string to be decoded (this will be explained later).
Now we keep extracting characters from the string till we are not getting any space.
As soon as we get a space we look up the corresponding English language character to the extracted sequence of characters
(or our morse code) and add it to a variable which will store the result.
Remember keeping track of the space is the most important part of this decryption process. As soon as we get 2 consecutive
spaces we will add another space to our variable containing the decoded string.
The last space at the end of the string will help us identify the last sequence of morse code characters
(since a space acts as a check for extracting characters and start decoding them).

"""


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

#def encrypt(msg)
#def decrypt(msg)
#count -> space count

def encrypt(msg):
    cipher = ""       #initially our morse code string is empty
    for letter in msg:
        if (letter!=" "):        #if letter not equal to space -> means there is a letter corresponding print morese code
            cipher = cipher + MORSE_CODE_DICT[letter] + " "          #update cipher which contains the morse code of a string
        else:                      #if letter == space, then update cipher with a space
            cipher = cipher + " "
    return cipher                 #return morse code of a string

def decrypt(msg):
    msg = msg + " "           #for decrytion, add a space at the final of a string so that in the end it got to know that string is finished
    decipher = ""             #contains the english string of a morse code
    citext = ""               #contains the letter of the english alphabet corresponding to morse code

    for letter in msg:
        if (letter!=" "):       #if letter not equal to space -> means we have to decrypt that letter of string, so contains into citext
            count=0
            citext = citext + letter
        else:                   #if letter == space, means there is a space between two strings
            count = count + 1
            if(count==2):        #string end, new string begin
                decipher = decipher + " "      #adding space to seperate the words
            else:
                decipher = decipher + list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]       #reverse of encryption
                citext = ""      #update citext to take next character
    return decipher              #return string of english alphabet

def main():
    print("Type English word to encrypt : ")
    msg = input()
    result = encrypt(msg.upper())
    print(result)

    print()
    print("Type morse code to decrypt : ")
    msg = input()
    result = decrypt(msg)
    print(result)

if __name__ == '__main__':
    main()