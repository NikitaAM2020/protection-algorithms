def create_substitution_table():
    # Створимо таблицю для шифру пропорційної заміни.
    # Використаємо наведену таблицю з двоцифровими числами.
    substitution_table = {

        'А': ['09', '31', '47', '54', '60', '80'],
        'Б': ['14', '15'],
        'В': ['01', '21', '37', '50', '68'],
        'Г': ['02', '16'],
        'Ґ': ['03'],
        'Д': ['04', '17', '32', '51'],
        'Е': ['05', '18', '34', '53'],
        'Є': ['06', '19'],
        'Ж': ['07', '20', '35'],
        'З': ['08', '22', '36', '52'],
        'И': ['23', '38', '55', '61'],
        'І': ['24', '39', '56', '62'],
        'Ї': ['25', '40'],
        'Й': ['26', '41'],
        'К': ['27', '42', '57', '63'],
        'Л': ['28', '43', '64'],
        'М': ['29', '44', '65'],
        'Н': ['30', '45', '66', '69'],
        'О': ['46', '67', '70', '71'],
        'П': ['48', '49', '72'],
        'Р': ['73', '74', '75', '76'],
        'С': ['77', '78', '79', '81'],
        'Т': ['82', '83', '84', '85'],
        'У': ['86', '87', '88'],
        'Ф': ['89'],
        'Х': ['90', '91'],
        'Ц': ['92', '93'],
        'Ч': ['94', '95'],
        'Ш': ['96', '97'],
        'Щ': ['98'],
        'Ь': ['99'],
        'Ю': ['100', '101'],
        'Я': ['102', '103', '104'],
        ',': ['105', '106', '107', '108'],
        '.': ['109', '110', '111', '112', '113', '114', '115', '116'],
        ' ': ['118', '117', '119', '120', '121', '122', '123', '124', '125', '126', '127', '128', '129', '130',
              '131', '132', '133', '134']

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



# Зчитуємо відкритий текст з файлу
with open('plaintext.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Зашифруємо текст і запишемо криптограму у файл
substitution_table = create_substitution_table()
ciphertext = encrypt(text, substitution_table)

with open('ciphertext.txt', 'w', encoding='utf-8') as file:
    file.write(ciphertext)

print('Текст успішно зашифровано')
