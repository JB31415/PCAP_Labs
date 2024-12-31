#Encrypts character using the Caesar Cipher by an arbitrary number of shifts
def encrypt(char, shift):
    #convert character to ordinal
    ordinal = ord(char)
    
    #If an upper case letter...
    if ordinal < 91:
        #Find place in alphabet
        ordinal = ordinal - 65
        
        #shift it
        ordinal = ordinal + shift
        
        #if overflows...
        if ordinal > 25:
            #wrap back around
            ordinal = ordinal - 26
            
        #return result
        return(chr(ordinal + 65))
    
    #if lowercase letter...
    if ordinal > 96:
        
        #Find place in alphabet
        ordinal = ordinal - 97
        
        #shift it
        ordinal = ordinal + shift
        
        #if overflows
        if ordinal > 25:
            #wrap back around
            ordinal = ordinal - 26
        
        #return result
        return(chr(ordinal + 97))


#Start of Main 

#Get needed input
message = input("Please enter you message to encrypt: ")
shift = input("Please enter the amount to shift: ")
shift = int(shift)

#empty encoded message to be displayed to user
encoded_message = ""

#Validate shift amount, exit if not
if shift > 25 or shift < 1:
    print("Invalid shift amount")
    exit()



#Loop through each character in user message
for char in message:
    #If letter, shift using encrypt function
    if char.isalpha():
        encoded_message += encrypt(char, shift)
    
    #else a number/whitespace, leave it alone
    else:
        encoded_message += char

#print the encoded message back to user
print("Encoded Message = " + encoded_message)



