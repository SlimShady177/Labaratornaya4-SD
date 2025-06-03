import time
from typing import List, Dict
from collections import Counter
import os


def preprocess_dictionary(file_path: str) -> Dict[int, List[tuple[str, str]]]:
    start_time = time.time()
    dictionary_by_length = {}

    try:
        with open(file_path, encoding='utf-8') as f:
            words = [line.strip().lower() for line in f if line.strip()]

        for word in words:
            length = len(word)
            sorted_word = ''.join(sorted(word))
            if length not in dictionary_by_length:
                dictionary_by_length[length] = []
            dictionary_by_length[length].append((word, sorted_word))

        print(f"Словарь обработан за {time.time() - start_time:.2f} секунд")
        return dictionary_by_length
    # Проверка файла словаря
    except FileNotFoundError:
        raise FileNotFoundError("Файл словаря не найден. Убедитесь, что файл словаря существует.")
    except UnicodeDecodeError:
        raise UnicodeDecodeError("Ошибка декодирования. Убедитесь, что файл в кодировке UTF-8.")

    # Проверка на составление слова из букв входного слова, использую отсортированные строки букв
def can_form_word(input_sorted: str, word_sorted: str) -> bool:
    if len(word_sorted) > len(input_sorted):
        return False

    input_counter = Counter(input_sorted)
    word_counter = Counter(word_sorted)

    for char, count in word_counter.items():
        if input_counter[char] < count:
            return False
    return True

    # Находим все слова из словаря, которые можно составить из букв входного слова, затем возвращаем список слов, отсортированный по длине
def find_words(input_word: str, dictionary: Dict[int, List[tuple[str, str]]]) -> List[str]:
    start_time = time.time()
    input_word = input_word.lower()
    input_sorted = ''.join(sorted(input_word))
    result = []

    # Проверка длины слов
    max_length = len(input_word)
    for length in range(max_length, 0, -1):
        if length in dictionary:
            for word, sorted_word in dictionary[length]:
                if can_form_word(input_sorted, sorted_word):
                    result.append(word)

    print(f"Обработка слова '{input_word}' заняла {time.time() - start_time:.2f} секунд")
    return result


def main():
    print("Выполнил: Шишкалов Иван Дмитриевич, Группа: 090301-ПОВа-о24")
    dictionary_file = "russian_nouns.txt"

    print("Инициализация словаря...")
    dictionary = preprocess_dictionary(dictionary_file)

    while True:
        input_word = input("\nВведите слово (или 'выход' для завершения): ")
        if input_word.lower() == 'выход':
            break

        result = find_words(input_word, dictionary)
        print(f"\nСлова, которые можно составить из '{input_word}':")
        if result:
            for word in result:
                print(word)
        else:
            print("Слов не найдено.")
        print(f"Найдено слов: {len(result)}")


if __name__ == "__main__":
    main()