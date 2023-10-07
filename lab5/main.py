def playfair_encrypt(plaintext, key_table):
    ciphertext = ""
    plaintext = plaintext.replace(" ", "").replace(",", "").replace(".", "")  # Видаліть пробіли та розділові знаки
    plaintext = plaintext.upper()  # Перетворіть текст у верхній регістр

    # Додайте символ 'Х' в кінець, якщо кількість символів непарна
    if len(plaintext) % 2 != 0:
        plaintext += 'Х'

    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], plaintext[i + 1]
        col1, row1 = find_char_position(char1, key_table)
        col2, row2 = find_char_position(char2, key_table)

        # Зашифруйте пару символів
        if row1 == row2:
            ciphertext += key_table[row1][(col1 + 1) % 11] + key_table[row2][(col2 + 1) % 11]
        elif col1 == col2:
            ciphertext += key_table[(row1 + 1) % 3][col1] + key_table[(row2 + 1) % 3][col2]
        else:
            ciphertext += key_table[row1][col2] + key_table[row2][col1]

    return ciphertext

def find_char_position(char, key_table):
    for row in range(3):
        for col in range(11):
            if key_table[row][col] == char:
                return col, row

# Ваш текст та таблиця-ключ
key_table = [
    ['Ч', 'И', 'Н', 'О', 'Л', 'А', 'Т', 'В', 'Г', 'Х', 'Я'],
    ['Ж', 'З', 'М', 'П', 'Р', 'С', 'Б', 'У', 'Ф', 'Д', 'Ц'],
    ['К', 'Ш', 'Ь', 'Й', 'І', 'Ґ', 'Е', 'Є', 'Ю', 'Щ', 'Ї']
]

text = "ЧАЙЦЕНАПОЙЯКИЙНАДАЄДУШІТЕПЛОТАЗАСПОКОЄННЯВІДЙОГОЧАРІВНЕЗАБУДЕШНІКОЛИЧАЙВЕЛИЧЕЗНИЙВІНСУПРОВОДЖУЄНАСНАВСІХЕТАПАХЖИТТЯВІДЗАСМАГЛИХШКІРКИПУЕРУДОАРОМАТНИХЛИСТКІВООЛОНГУ"
with open("plaintext.txt", "a+", encoding="utf-8") as file:
    file.write(text)

ciphertext = playfair_encrypt(text, key_table)
with open("ciphertext.txt", "a+", encoding="utf-8") as file:
    file.write(ciphertext)
