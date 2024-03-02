def read_phonebook(filename):
    """
    Считывает телефонный справочник по имени файла
    :param filename: передаёт имя файла
    :return: возвращает телефонный справочник
    """
    phonebook = []
    with open(filename, 'r', encoding='utf-8') as file: #открывает файл для чтения
        for line in file: #построчно считывает данные и разделяет их запятой
            entry = line.strip().split(',')
            phonebook.append(entry) #добавляет в телефонный справочник
    return phonebook

def print_phonebook(phonebook):
    """
    Выводит телефонный справочник на экран
    :param phonebook:
    :return: ничего не возвращает, а печатает телефонный справочник с пояснениями
    """
    for entry in phonebook:
        print("Фамилия: {}, Имя: {}, Номер телефона: {}, Описание: {}".format(*entry))

def find_by_lastname(phonebook, lastname):
    """
    Функция поиска в телефонной книге по фамилии
    :param phonebook: принимает телефонную книгу
    :param lastname: принимает фамилию
    :return: возвращает результат поиска
    """
    results = []
    for entry in phonebook:
        if lastname in entry[0]:
            results.append(entry)
    return results

def find_by_phone(phonebook, phone):
    """
    Функция поиска в телефонной книге по номеру телефона
    :param phonebook: телефонная книга
    :param phone: номер телефона
    :return: результат поиска
    """
    for entry in phonebook:
        if phone in entry[2]:
            return entry
    return None

def add_entry(phonebook, entry):
    """
    Функция ввода в телефонную книгу
    :param phonebook: телефонная книга
    :param entry: сохраняемые значения
    :return: изменённую телефонную книгу
    """
    phonebook.append(entry)

def save_phonebook(phonebook, filename):
    """
    сохраняет справочник в файле
    :param phonebook: Получает справочник
    :param filename: Название файла
    :return: сохранённый файл
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for entry in phonebook:
            file.write(','.join(entry) + '\n')

def main():
    filename = "phonebook.txt"
    phonebook = read_phonebook(filename)
    while True:
        print("\nВыберите необходимое действие\n"
              "1. Отобразить весь справочник\n"
              "2. Найти абонента по фамилии\n"
              "3. Найти абонента по номеру телефона\n"
              "4. Добавить абонента в справочник\n"
              "5. Сохранить справочник в текстовом формате\n"
              "6. Закончить работу")
        choice = input("Ваш выбор: ")
        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            lastname = input("Введите фамилию для поиска: ")
            results = find_by_lastname(phonebook, lastname)
            if results:
                print("Найденные записи:")
                print_phonebook(results)
            else:
                print("Абонент с такой фамилией не найден.")
        elif choice == '3':
            phone = input("Введите номер телефона для поиска: ")
            result = find_by_phone(phonebook, phone)
            if result:
                print("Найденный абонент:")
                print("Фамилия: {}, Имя: {}, Номер телефона: {}, Описание: {}".format(*result))
            else:
                print("Абонент с таким номером телефона не найден.")
        elif choice == '4':
            lastname = input("Введите фамилию абонента: ")
            firstname = input("Введите имя абонента: ")
            phone = input("Введите номер телефона абонента: ")
            description = input("Введите описание абонента: ")
            add_entry(phonebook, [lastname.strip(), firstname.strip(), phone.strip(), description.strip()])
            print("Абонент успешно добавлен в справочник.")
        elif choice == '5':
            save_phonebook(phonebook, filename)
            print("Справочник успешно сохранен в файле {}.".format(filename))
        elif choice == '6':
            print("Завершение работы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие из списка.")

if __name__ == "__main__":
    main()