secrete_key = 'secrete'
shift_val = 13
max_ord = 125
min_ord = 32



#start the hash
def hash_function(text):
    hashString = ''
    new_hash = ''
    input_with_salt = text + secrete_key
    for letter in input_with_salt:
        hold = ord(letter)
        if hold + shift_val >= max_ord:
            remainder = (hold+shift_val) - max_ord
            hashString += chr(min_ord + remainder)
        else:
            hashString+= chr(hold + shift_val)
    new_hash = hashString
    res = mod_the_hash(new_hash)
    return res



#if the number is even and the index is even add 2 to it
def mod_the_hash(new_hash):
    modded_hash = ''
    for i in range(len(new_hash)):
        if i % 2 == 0 and ord(new_hash[i]) % 2 == 0 and ord(new_hash[i]) != max_ord -1:
            asc_two = ord(new_hash[i]) + 2
            modded_hash += chr(asc_two)
        else:
            modded_hash += new_hash[i]
    return modded_hash



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
    res = dehash_function(unmodded_hash)
    return res



#dehash the shift 13
def dehash_function(new_hash):
    dehashed_string = ''
    for letter in new_hash:
        hold = ord(letter)
        if hold < 45:
            remainder = min_ord - (hold-shift_val)
            dehashed_string += chr(max_ord - remainder)
            #dehashed_string += chr((max_ord + min_ord) - (hold+shift_val))
        else:
            dehashed_string += chr(hold - shift_val)
    return dehashed_string




einput = input("encrpyt or decrypt: ")
filename = input("enter filename: ")
encryption_name = filename.split('.')[0] + "_encrypt.txt"
decrpyt_name = filename.split(".")[0] + "_decrypt.txt"


if einput == "encrypt":
    f = open(filename, "r")
    text = f.read()
    encrypted_text = hash_function(text);
    f2 = open(encryption_name, "w")
    f2.write(encrypted_text)
    f2.close()
else:
    f = open(filename, "r")
    text = f.read()
    decrypted_text = demodded_hash(text);
    f2 = open(decrpyt_name, "w")
    f2.write(decrypted_text)
    f2.close()

