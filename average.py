class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        result = []
        for letter in original_text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.index(letter.lower())
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        result = []
        shift = -shift
        for letter in cipher_text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.index(letter.lower())
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
