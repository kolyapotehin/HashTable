class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size
        self.count = 0

    # Хеш-функция для чисел
    def hash_function(self, key):
        return key % self.size

    # Добавление элемента
    def insert(self, key, value):
        if self.count >= self.size * 0.7:
            self.resize()

        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

        self.table[index] = (key, value)
        self.count += 1

    # Поиск элемента
    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

            if index == start:
                break

        return None

    # Удаление элемента
    def delete(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return True

            index = (index + 1) % self.size

            if index == start:
                break

        return False

    # Увеличение таблицы в 2 раза
    def resize(self):
        old_table = self.table

        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for item in old_table:
            if item is not None:
                self.insert(item[0], item[1])

# ==========================================
# 3. Хеш-функция для строк
# ==========================================

def string_hash(string):
    result = 0

    for char in string:
        result += ord(char)

    return result

# ==========================================
# 4. Словарь со строковыми ключами
# ==========================================

class StringDictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    # Хеш-функция строки
    def hash_function(self, key):
        return string_hash(key) % self.size

    # Добавление
    def add(self, key, value):
        index = self.hash_function(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return

            index = (index + 1) % self.size

        self.table[index] = (key, value)

    # Поиск
    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]

            index = (index + 1) % self.size

            if index == start:
                break

        return None

# ==========================================
# ПРОВЕРКА РАБОТЫ
# ==========================================

print("1. Хеш-таблица")

table = HashTable(5)

table.insert(1, "one")
table.insert(2, "two")
table.insert(3, "three")

print("Поиск ключа 2:", table.search(2))

table.delete(2)

print("После удаления ключа 2:", table.search(2))

print("\n2. Resize")

table = HashTable(5)

for i in range(10):
    table.insert(i, "value" + str(i))

print("Количество элементов:", table.count)
print("Размер таблицы:", table.size)

print("\n3. Хеш-функция строки")

print("Хеш слова 'cat':", string_hash("cat"))

print("\n4. Словарь")

dictionary = StringDictionary()

dictionary.add("apple", "яблоко")
dictionary.add("cat", "кот")
dictionary.add("dog", "собака")

print("cat:", dictionary.search("cat"))
print("dog:", dictionary.search("dog"))
print("car:", dictionary.search("car"))