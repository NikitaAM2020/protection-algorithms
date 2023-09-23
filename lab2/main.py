def create_substitution_table():
    # Створимо таблицю для шифру пропорційної заміни.
    # Використаємо наведену таблицю з двоцифровими числами.
    substitution_table = {

        'А': ['09', '31', '47', '54'],
        'Б': ['14', '15'],
        'В': ['01', '21', '37'],
        'Г': ['02', '16'],
        'Ґ': ['03'],
        'Д': ['04', '17', '32'],
        'Е': ['05', '18', '34', '53'],
        'Є': ['06', '19'],
        'Ж': ['07', '20', '35'],
        'З': ['08', '22'],
        'И': ['23', '38', '55'],
        'І': ['24', '39'],
        'Ї': ['25', '40'],
        'Й': ['26', '41'],
        'К': ['27', '42'],
        'Л': ['28', '43', '64'],
        'М': ['29', '44'],
        'Н': ['30', '45', '66'],
        'О': ['46', '67'],
        'П': ['48', '49', '72'],
        'Р': ['73', '74'],
        'С': ['77', '78'],
        'Т': ['82', '83'],
        'У': ['86'],
        'Ф': ['89'],
        'Х': ['90'],
        'Ц': ['92'],
        'Ч': ['94'],
        'Ш': ['96'],
        'Щ': ['98'],
        'Ь': ['99'],
        'Ю': ['60'],
        'Я': ['80'],
        ',': ['97', '65'],
        '.': ['95', '50', '51', '68'],
        ' ': ['36', '52', '61', '63', '76']
    }
    return substitution_table


import random


def encrypt(plaintext, substitution_table):
    ciphertext = ''

    for char in plaintext:
        char = char.upper()  # Конвертуємо у верхній регістр
        if char in substitution_table:
            random_index = random.randint(0, len(substitution_table[char]) - 1)
            random_number = substitution_table[char][random_index]
            ciphertext += random_number
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, substitution_table):
    plaintext = ''
    reverse_substitution_table = {}

    # Створюємо зворотню таблицю замін для ефективного розшифрування
    for char, numbers in substitution_table.items():
        for number in numbers:
            reverse_substitution_table[number] = char

    i = 0
    while i < len(ciphertext):
        # Якщо можливо, витягнемо двоцифровий код
        if ciphertext[i:i + 2].isdigit():
            code = ciphertext[i:i + 2]
            i += 2
        else:
            # Якщо не можливо, витягнемо одну цифру
            code = ciphertext[i]
            i += 1

        # Спробуємо розшифрувати код
        if code in reverse_substitution_table:
            plaintext += reverse_substitution_table[code]
        else:
            plaintext += code

    return plaintext


def decrypt_file(input_file, output_file, substitution_table):
    with open(input_file, 'r', encoding='utf-8') as file:
        ciphertext = file.read()

    plaintext = decrypt(ciphertext, substitution_table)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(plaintext)


# Зчитуємо відкритий текст з файлу
with open('plaintext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Зашифруємо текст і запишемо криптограму у файл
substitution_table = create_substitution_table()
ciphertext = encrypt(text, substitution_table)

with open('ciphertext.txt', 'w', encoding='utf-8') as file:
    file.write(ciphertext)

print('Текст успішно зашифровано')

# Використовуйте ім'я файлу, в якому зберігається криптограма,
# і ім'я файлу, в якому зберігатиметься розшифрований текст.
input_file = 'ciphertext.txt'
output_file = 'decrypted.txt'

# Розшифровуємо криптограму та записуємо розшифрований текст у файл
decrypt_file(input_file, output_file, substitution_table)

print('Текст успішно розшифровано')


def calculate_letter_frequency_from_file(file_name):
    frequency = {}  # Створюємо пустий словник для зберігання частоти літер

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            text = file.read()

        # Перетворюємо текст у верхній регістр і видаляємо всі символи, окрім літер та пробіла
        text = text.upper()
        text = ''.join(filter(lambda char: char.isalpha() or char.isspace(), text))

        total_characters = len(text)  # Загальна кількість символів у тексті

        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        # Перетворюємо кількість кожного символу у відсотки
        for char, count in frequency.items():
            frequency[char] = (count / total_characters) * 100

    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return frequency


# Приклад використання функції для аналізу частоти літер та пробіла у файлі
file_name = 'plaintext.txt'  # Замініть це на шлях до вашого файлу
letter_frequency = calculate_letter_frequency_from_file(file_name)

print("\nАналіз частоти літер в тексті")
# Виведення результатів у відсотках
for char, percentage in letter_frequency.items():
    print(f"'{char}': {percentage:.2f}%")


def analyze_character_usage_in_ciphertext(file_name, substitution_table):
    character_count = {}  # Створимо словник для зберігання кількості кожного символу

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            ciphertext = file.read()

        total_characters = len(ciphertext)  # Загальна кількість символів у криптограмі

        # Пройдемося по криптограмі, враховуючи двоцифрові коди
        i = 0
        while i < len(ciphertext):
            # Якщо можливо, витягнемо двоцифровий код
            if ciphertext[i:i + 2].isdigit():
                code = ciphertext[i:i + 2]
                i += 2
            else:
                # Якщо не можливо, витягнемо одну цифру
                code = ciphertext[i]
                i += 1

            # За допомогою зворотної таблиці визначаємо символ, який відповідає коду
            char = substitution_table.get(code, code)

            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

        # Перетворюємо кількість кожного символу у відсотки
        for char, count in character_count.items():
            character_count[char] = (count / total_characters) * 100

    except FileNotFoundError:
        print(f"Файл '{file_name}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return character_count

# Приклад використання функції для аналізу символів у криптограмі на основі substitution_table
file_nameС = 'ciphertext.txt'  # Замініть це на шлях до вашого файлу з криптограмою
character_usage = analyze_character_usage_in_ciphertext(file_nameС, substitution_table)

print("\nАналіз частоти цифр в криптограмі")
# Виведення результатів у відсотках
for char, percentage in character_usage.items():
    print(f"'{char}': {percentage:.2f}%")
