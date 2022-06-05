secrete_key = 'secrete'
shift_val = 13
max_ord = 125
min_ord = 33

sinput = input('Enter the string to be hashed: ') #input for the hashing algo


##########################################################
#                                                        #
#             ---//      K3LLY      \\---                #
#                                                        #
##########################################################


#start the hash
def hash_function():
    result = validate_input()
    hashString = ''
    new_hash = ''
    input_with_salt = sinput + secrete_key
    if result:
        for letter in input_with_salt:
            hold = ord(letter)
            if hold + shift_val >= max_ord:
                remainder = (hold+shift_val) - max_ord
                hashString += chr(min_ord + remainder)
            else:
                hashString+= chr(hold + shift_val)
        new_hash = hashString
        mod_the_hash(new_hash)
    else:
        print('invalid input')



#if the number is even and the index is even add 2 to it
def mod_the_hash(new_hash):
    modded_hash = ''
    for i in range(len(new_hash)):
        if i % 2 == 0 and ord(new_hash[i]) % 2 == 0 and ord(new_hash[i]) != max_ord -1:
            asc_two = ord(new_hash[i]) + 2
            modded_hash += chr(asc_two)
        else:
            modded_hash += new_hash[i]
    print('hashed ======> ' + modded_hash)

    #start the dehash
    demodded_hash(modded_hash)


#demodd the modded hashed string
def demodded_hash(modded_hash):
    unmodded_hash = ''
    modded_original_length = len(modded_hash) - len(secrete_key)
    modded_hash_without_salt = modded_hash[:modded_original_length]
    for i in range(len(modded_hash_without_salt)):
        if i % 2 == 0 and ord(modded_hash_without_salt[i]) % 2 == 0:
            asc_two = ord(modded_hash_without_salt[i]) - 2
            unmodded_hash += chr(asc_two)
        else:
            unmodded_hash += modded_hash_without_salt[i]
    dehash_function(unmodded_hash)



#dehash the shift 13
def dehash_function(new_hash):
    dehashed_string = ''
    for letter in new_hash:
        hold = ord(letter)
        if hold < 46:
            remainder = min_ord - (hold-shift_val)
            dehashed_string += chr(max_ord - remainder)
            #dehashed_string += chr((max_ord + min_ord) - (hold+shift_val))
        else:
            dehashed_string += chr(hold - shift_val)
    print('dehashed ======> ' + dehashed_string)




def validate_input():
    for letter in sinput:
        if ord(letter) < min_ord or ord(letter) > max_ord:
            return False
    return True


print('input ======> ' + sinput)
hash_function()