def caesar_cipher(message, code, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words = message.split(" ")
    lst_cipher_words = []
    if code == "code":
        offset = offset * -1
    for word in words:
        cipher_word = ""
        for letter in word:
            letter_index = alphabet.find(letter)
            if letter_index > -1:
                cipher_word += alphabet[((letter_index + offset) % 26)]
            elif letter_index == -1:
                cipher_word += letter
        lst_cipher_words.append(cipher_word)
    cipher_message = " ".join(lst_cipher_words)
    return cipher_message


coded_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
decoded_msg = caesar_cipher(coded_message, "decode", 10)
#print(decoded_msg)

recoded_msg = caesar_cipher(decoded_msg, "code", 10)
#print(recoded_msg)

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

f_msg = caesar_cipher(first_message, "decode", 10)
#print(f_msg)

s_msg = caesar_cipher(second_message, "decode", 14)
#print(s_msg)

'''
unknown_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
for i in range(0, 26):
    print(caesar_cipher(unknown_message, "decode", i), "Value:", i)
    print("\n")
'''

def vigenere_cipher(message, keyword, code):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_keyword = ""
    i = 0
    n = 0
    while i < len(message):
        if alphabet.count(message[i]) == 0:
            new_keyword += message[i]
            i += 1
        elif alphabet.count(message[i]) != 0:
            new_keyword += keyword[n % len(keyword)]
            i += 1
            n += 1        

    lst_message = message.split(" ")
    lst_keyword = new_keyword.split(" ")
    lst_cipher_words = []

    if code == "decode":
        offset = -1
    elif code == "code":
        offset = 1

    for i in range(0, len(lst_message)):
        cipher_word = ""
        for n in range(0, len(lst_message[i])):
            message_index = alphabet.find(lst_message[i][n])
            if message_index > -1:
                keyword_index = alphabet.find(lst_keyword[i][n])
                new_index = (message_index + (keyword_index * offset)) % 26
                cipher_word += alphabet[new_index]
            elif message_index == -1:
                cipher_word += lst_message[i][n]
        lst_cipher_words.append(cipher_word)
    cipher_message = " ".join(lst_cipher_words)
    return cipher_message


message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

d_msg = vigenere_cipher(message, keyword, "decode")
print(d_msg)

c_msg = vigenere_cipher(d_msg, keyword, "code")
print(c_msg)

