# Українська абетка (без пробілів і розділових знаків) у верхньому регістрі
ukrainian_alphabet = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'

def modular_encrypt(plaintext, key):
    encrypted_text = ''
    for char in plaintext:
        char = char.upper()  # Переводимо літеру у верхній регістр
        if char in ukrainian_alphabet:
            char_index = ukrainian_alphabet.index(char)
            encrypted_index = (char_index + key) % len(ukrainian_alphabet)
            encrypted_text += ukrainian_alphabet[encrypted_index]
        else:
            encrypted_text += char  # Залишаємо символи, які не знаходяться в абетці без змін
    return encrypted_text

def modular_decrypt(ciphertext, key):
    decrypted_text = ''
    for char in ciphertext:
        if char in ukrainian_alphabet:
            char_index = ukrainian_alphabet.index(char)
            decrypted_index = (char_index - key) % len(ukrainian_alphabet)
            decrypted_text += ukrainian_alphabet[decrypted_index]
        else:
            decrypted_text += char  # Залишаємо символи, які не знаходяться в абетці без змін
    return decrypted_text

# Приклад використання
plaintext = "КафедраПрикладноїМатематики"
key = 3  # Прикладний ключ
encrypted_text = modular_encrypt(plaintext, key)
print("Зашифрований текст:", encrypted_text)

# Збережемо зашифрований текст у файл
with open("encrypted_text.txt", "w") as file:
    file.write(encrypted_text)

# Дешифруємо зашифрований текст
decrypted_text = modular_decrypt(encrypted_text, key)
print("Розшифрований текст:", decrypted_text)

# Імпортуємо бібліотеку для хешування паролю
import hashlib

# Генеруємо ключ шифрування з парольної фрази
password = "читання"
key = int(hashlib.sha256(password.encode()).hexdigest(), 16) % len(ukrainian_alphabet)

# Зашифруємо відкритий текст
with open("department_text.txt", "r", encoding="utf-8") as file:
    plaintext = file.read()
encrypted_text = modular_encrypt(plaintext, key)

# Збережемо зашифрований текст у файл
with open("encrypted_department_text.txt", "w") as file:
    file.write(encrypted_text)

# Дешифруємо зашифрований текст з використанням тієї самої гами (ключа)
decrypted_text = modular_decrypt(encrypted_text, key)

# Збережемо розшифрований текст у файл
with open("decrypted_department_text.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_text)

print("Розшифрований текст:", decrypted_text)
