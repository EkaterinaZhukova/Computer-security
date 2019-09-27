from .language_info import Language

class Vigenere:

    def __init__(self, lang):
        self.lang = lang

    def encode(self, source_text, key):
        start_pos, num = self.lang.info()
        key_length = len(key)
        key_as_int = self.positions_from_string(key)
        plaintext_int = self.positions_from_string(source_text)
        ciphered = []
        for i in range(len(plaintext_int)):
            value = (plaintext_int[i] + key_as_int[i % key_length]) % num
            ciphered.append(value)
        return self.string_from_positions(ciphered)

    def decode(self, encoded, key):
        if key == None:
            return ""
        start_pos, num = self.lang.info()
        key_len = len(key)
        key_arr = self.positions_from_string(key)
        ciphered_arr = self.positions_from_string(encoded)
        plain_text = []
        for i in range(len(ciphered_arr)):
            value = (ciphered_arr[i] - key_arr[i % key_len]) % num
            plain_text.append(value)
        return self.string_from_positions(plain_text)

    def positions_from_string(self, text):
        res = []
        alphabet = self.lang.alphabet_arr()
        res = [alphabet.index(letter) for letter in text]
        return res

    def string_from_positions(self, positions):
        alphabet = self.lang.alphabet_arr()
        res = [alphabet[index] for index in positions]
        return res