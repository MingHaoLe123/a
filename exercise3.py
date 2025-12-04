class VigenereCipher:
    offset = ord('A')

    def __init__(self, keyword: str):
        self.keyword = keyword.upper()

    def __shift_letter(self, letter: str, shift: int, forward: bool):
        
        pos = ord(letter) - self.offset  
        if forward:
            new_pos = (pos + shift) % 26
        else:
            new_pos = (pos - shift) % 26
        return chr(self.offset + new_pos)

    def __generate_shift_list(self, plaintext_length: int):
        
        repeated = (self.keyword * ((plaintext_length // len(self.keyword)) + 1))[:plaintext_length]
        return [ord(ch) - self.offset for ch in repeated]  

    def encrypt(self, plaintext: str):
        
        cleaned = ''.join(ch for ch in plaintext.upper() if ch.isalpha())
        shifts = self.__generate_shift_list(len(cleaned))
        ciphertext_chars = [
            self.__shift_letter(cleaned[i], shifts[i], True)
            for i in range(len(cleaned))
        ]
        return ''.join(ciphertext_chars)

    def decrypt(self, ciphertext: str):
        cleaned = ''.join(ch for ch in ciphertext.upper() if ch.isalpha())
        shifts = self.__generate_shift_list(len(cleaned))
        plaintext_chars = [
            self.__shift_letter(cleaned[i], shifts[i], False)
            for i in range(len(cleaned))
        ]
        return ''.join(plaintext_chars)
