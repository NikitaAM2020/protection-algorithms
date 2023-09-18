def create_substitution_table():
    # Створимо таблицю для шифру пропорційної заміни.
    # Використаємо наведену таблицю з двоцифровими числами.
    substitution_table = {
        'А': '10113358', 'Б': '1174', 'В': '071228525974', 'Г': '137785', 'Ґ': '01', 'Д': '08147981',
        'Е': '1585919299', 'Є': '081698', 'Ж': '1771', 'З': '077086', 'И': '1928354886',
        'І': '132044', 'Ї': '212255', 'К': '02223354', 'Л': '2355', 'М': '052496',
        'Н': '2541444569', 'О': '0317265776', 'П': '022786', 'Р': '28295770', 'С': '11212945',
        'Т': '1027305174', 'У': '093154', 'Ф': '32', 'Х': '315963', 'Ц': '28',
        'Ч': '213599', 'Ш': '10', 'Щ': '29', 'Ь': '05385663', 'Ю': '3943',
        'Я': '044051', ' ': '1540415052536067757986', '.': '10122032496771' , ',': '1934566378'
    }
    return substitution_table

def encrypt(plaintext, substitution_table):
    ciphertext = ''

    for char in plaintext:
        char = char.upper()  # Конвертуємо у верхній регістр
        if char in substitution_table:
            ciphertext += substitution_table[char]
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
