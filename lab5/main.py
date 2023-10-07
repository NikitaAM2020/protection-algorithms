def find_char_position(char, key_table):
    for row in range(3):
        for col in range(11):
            if key_table[row][col] == char:
                return col, row  # Повертайте позицію символу


def playfair_decrypt(ciphertext, key_table):
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        col1, row1 = find_char_position(char1, key_table)
        col2, row2 = find_char_position(char2, key_table)

        # Розшифруйте пару символів
        if row1 == row2:
            plaintext += key_table[row1][(col1 - 1) % 11] + key_table[row2][(col2 - 1) % 11]
        elif col1 == col2:
            plaintext += key_table[(row1 - 1) % 3][col1] + key_table[(row2 - 1) % 3][col2]
        else:
            plaintext += key_table[row1][col2] + key_table[row2][col1]

    return plaintext


def main():
    # Ваш текст та таблиця-ключ
    key_table = [
        ['Ч', 'И', 'Н', 'О', 'Л', 'А', 'Т', 'В', 'Г', 'Х', 'Я'],
        ['Ж', 'З', 'М', 'П', 'Р', 'С', 'Б', 'У', 'Ф', 'Д', 'Ц'],
        ['К', 'Ш', 'Ь', 'Й', 'І', 'Ґ', 'Е', 'Є', 'Ю', 'Щ', 'Ї']
    ]

    # Зчитайте зашифрований текст з файлу
    with open("ciphertext.txt", "r", encoding="utf-8") as file:
        ciphertext = file.read()

    # Розшифруйте текст
    decrypted_text = playfair_decrypt(ciphertext, key_table)
    print("Розшифрований текст:", decrypted_text)


if __name__ == "__main__":
    main()
