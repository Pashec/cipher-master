class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        if is_encrypt:
            for letter in text:
                if letter.lower() in self.alphabet:
                    index = self.alphabet.index(letter.lower())
                    new_index = (index + shift) % len(self.alphabet)
                    result.append(self.alphabet[new_index])
                else:
                    result.append(letter)
            return ''.join(result)
        else:
            result = []
        shift = -shift
        for letter in text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.index(letter.lower())
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result)
    

cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 