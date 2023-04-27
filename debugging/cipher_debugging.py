def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))#'char' is a function that converts an integer into its ASCII character.
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        # plain_char = cipher[65 - ord(i)] #'ord' is a function that converts the ASCII value of the character into an integer. This piece of code subtracts the number from 65(the ASCII value for 'A') and gives the index of the corresponding plaintext character in the cipher list.
        plain_char = cipher[ord(i) - 65] #instead of minusing ord from 65 do it the other way around. So that it's counting from the uppercase end of the list.

        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    # alphabet = [chr(i + 98) for i in range(1, 26)] #This is only iterating from lettrs 98 to 122, as the ASCII value of 97 is 'a' it is currently being missed out. #The new version is:
    alphabet = [chr(i + 97) for i in range(0, 26)] #changing the 98 to 97 includes 'a' in our alphabet. Changing the range to start from 0 also allows the code to iterate through the whole alphabet.
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")