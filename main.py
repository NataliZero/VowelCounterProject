def count_vowels(text):
    vowels = "aeiou"  # Гласные буквы (теперь только строчные)
    count = 0
    for char in text.lower():  # Преобразуем строку к нижнему регистру
        if char in vowels:  # Проверяем только строчные гласные
            count += 1
    return count
