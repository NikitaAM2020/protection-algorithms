# 1. Реалізація процедури шифрування пропорційної заміни

def create_substitution_table():
    # Створимо таблицю для шифру пропорційної заміни.
    # В цьому прикладі використаємо відображення українського алфавіту в двоцифрові числа.
    alphabet = 'АБВГҐДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    number_mapping = {}

    for i in range(len(alphabet)):
        number_mapping[alphabet[i]] = str(i + 10)  # Додамо 10 для отримання двоцифрового числа

    return number_mapping


def encrypt(plaintext, number_mapping):
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()

            if char in number_mapping:
                substitution_char = number_mapping[char]
                if not is_upper:
                    substitution_char = substitution_char.lower()
                ciphertext += substitution_char
            else:
                ciphertext += char
        else:
            ciphertext += char

    return ciphertext

# 2. Зчитування тексту про місцевість з файлу plaintext.txt

with open('plaintext.txt', 'r', encoding='utf-8') as file:
    locality_description = file.read()

# 3. Зашифрування тексту та запис криптограми у файл

number_mapping = create_substitution_table()
ciphertext = encrypt(locality_description, number_mapping)

with open('ciphertext.txt', 'w', encoding='utf-8') as file:
    file.write(ciphertext)

print('Текст успішно зашифровано та записано у файл ciphertext.txt')
