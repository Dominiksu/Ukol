
alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    ' ': ' ',
}


alphabet_reverse = {value: k for k, value in alphabet.items()}


class Morse:
    def encode(self, text):
        encode = [alphabet[x] for x in text]
        return ''.join(encode)
    
    def decode(self, code):
        message_list = code.split()
        decode = [alphabet_reverse[k] for k in message_list]
        return ''.join(decode)



Test_1 = Morse()
print(Test_1.encode('HAPPY NEW YEAR'))
print(Test_1.decode('-- .- .-. .-. -.--   -.-. .... .-. .. ... - -- .- ...   .- -. -..   .... .- .--. .--. -.--   -. . .--   -.-- . .- .-.'))