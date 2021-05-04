#This is known, given from the homework
ciphertext = "011011010101101001000010110110010001000001011001011010110101010100010110110111001110100111110110111110110101010000101111"
m = 5
alphabet = "abcdefghijklmnopqrstuvwxyz ?!.'$"

#Because Alice starts every message with hi, this is known from what is given
h = ciphertext[0:5]
i = ciphertext[5:10]

#xor function of binary string x with binary string y returns the xor binary string of x and y
def xor(x, y):
    resStr = ""
    #print(s1, s2) using for checking/testing
    for i in range(m):
        a = int(x[i])
        b = int(y[i])
        res = a ^ b
        resStr += str(res)
    #print("resStr", resStr)
    return resStr

keyH = '01010'
keyI = '11101'
#print(xor('01101', keyH)) checking/testing and switched in for I to validate function
key = keyH

#Using recurrence relation: (zi + zi+3) mod 2 as shown for x
for i in range(len(ciphertext)):
    x = (int(key[i]) + int(key[i+3])) % 2
    #print("X:", x) checking
    key = key + (str(x))
    #print("Feedback?", key[i]+key[i+1])
    print("Key: ", key, "X: ", x) #testing/debugging

for i in range(0, len(ciphertext), m):
    letter = ciphertext[i:i + m]
    tempKey = key[i:i + m]
    xorletter = xor(letter, tempKey) #binary correlating to letter in alphabet
    #print("Letter: ", xorletter)
    s = alphabet[int(xorletter, 2)]
    print(s, end="") #attach at the end of the for loop

