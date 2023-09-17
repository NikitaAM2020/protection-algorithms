abc = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# Зчитуємо повідомлення з файлу
with open('input.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

print('Задане повідомлення:')
print(msg)
key = 10

# Відкриваємо файл для запису закодованого і розкодованого повідомлення
with open('output.txt', 'w', encoding='utf-8') as output_file:
    count = len(abc)

    output_file.write('Задане повідомлення:\n')
    output_file.write(msg + '\n\n')
    output_file.write('Закодоване повідомлення:\n')

    encrypted_msg = ''

    for letter in msg:
        if letter.lower() in abc:
            idx = abc.index(letter.lower())
            new_idx = (idx + key) % count
            encrypted_letter = abc[new_idx]

            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_msg += encrypted_letter
            output_file.write(encrypted_letter)
        else:
            encrypted_msg += letter
            output_file.write(letter)

    output_file.write('\n\n')
    output_file.write('Розкодоване повідомлення:\n')

    decrypted_msg = ''

    for letter in encrypted_msg:
        if letter.lower() in abc:
            idx = abc.index(letter.lower())
            new_idx = (idx - key) % count
            decrypted_letter = abc[new_idx]

            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_msg += decrypted_letter
            output_file.write(decrypted_letter)
        else:
            decrypted_msg += letter
            output_file.write(letter)

print('\nЗакодоване та розкодоване повідомлення збережено у файлі "output.txt".')

# Англійський алфавіт
abcEng = 'abcdefghijklmnopqrstuvwxyz'

# Зчитуємо повідомлення з файлу
with open('inputEng.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

print('\nРеалізація завдання для англійського алфавіту:')
print('Задане повідомлення:')
print(msg)
key = 10

# Відкриваємо файл для запису закодованого і розкодованого повідомлення
with open('outputEng.txt', 'w', encoding='utf-8') as output_file:
    output_file.write('Задане повідомлення:\n')
    output_file.write(msg + '\n\n')
    output_file.write('Закодоване повідомлення:\n')

    encrypted_msg = ''
    count = len(abcEng)

    for letter in msg:
        if letter.lower() in abcEng:
            idx = abcEng.index(letter.lower())
            new_idx = (idx + key) % count
            encrypted_letter = abcEng[new_idx]

            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_msg += encrypted_letter
            output_file.write(encrypted_letter)
        else:
            encrypted_msg += letter
            output_file.write(letter)

    output_file.write('\n\n')
    output_file.write('Розкодоване повідомлення:\n')

    decrypted_msg = ''

    for letter in encrypted_msg:
        if letter.lower() in abcEng:
            idx = abcEng.index(letter.lower())
            new_idx = (idx - key) % count
            decrypted_letter = abcEng[new_idx]

            if letter.isupper():
                decrypted_letter = decrypted_letter.upper()

            decrypted_msg += decrypted_letter
            output_file.write(decrypted_letter)
        else:
            decrypted_msg += letter
            output_file.write(letter)

print('\nЗакодоване та розкодоване повідомлення збережено у файлі "outputEng.txt".')
