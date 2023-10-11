import re

def read_first_sentence(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Визначення першого речення
            match = re.search(r'^.*?[.!?]', text)
            if match:
                first_sentence = match.group(0)
                print("Перше речення з файлу:")
                print(first_sentence)
            else:
                print("Файл не містить речень.")
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")

def sort_and_count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text, re.UNICODE)
            words = [word for word in words if word.isalpha()]
            words = sorted(words, key=lambda x: (x.lower().replace("і", "ї").replace("ї", "й"), x.lower())) # Сортуємо слова так, щоб "і" та "ї" були перед "й"
            print("\nВідсортовані слова з усього файлу:")
            print(' '.join(words))
            print("\nКількість слів у тексті:", len(words))
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдений.")
    except Exception as e:
        print(f"Помилка: {e}")


file_path = 'read_text.txt'
read_first_sentence(file_path)
sort_and_count_words(file_path)
