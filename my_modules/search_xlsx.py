from openpyxl import load_workbook


class SearchInXLSX:  # Клас для пошуку в декількох файлах ексел
    def __init__(self):
        self.__maxLenRow = 0  # Максимальна довжина строки
        self.__fileNames = []  # Масив шляхів до файлів ексел
        self.__requestSearch = ""  # Пощуковий запит
        self.__resultAll = []  # Загальний результат

    def setFileNames(self, fileNames):  # Отримує масив щляхів до файлів ексел
        self.__fileNames = fileNames

    def setRequestSearch(self, requestSearch):  # Отримує пошуковий запит
        self.__requestSearch = requestSearch

    def __strresult(self, m):
        res = []
        for i in m:
            x = i.value  # Значення в ячейці
            if x:
                res.append(str(i.value))
            else:
                res.append('-')  # Якщо немає значення в ячейці то створюємо відступ
        return res

    def __searchInAllBook(self):
        result = []
        lengF = len(self.__fileNames)  # Кількість книг
        for i in range(lengF):  #
            fileName = self.__fileNames[i]  # Шлях до файлу ексел
            work_book = load_workbook(fileName, data_only=True)  # завантаження книги
            # print(fileName)
            resultBook = self.__searchInOneBook(work_book, fileName)  # Передаємо книгу та шлях до файлу
            result.append(resultBook)
        #print("Result for all book")
        #print(result)
        #result = self.__resultAll
        #return result

    def __searchInOneBook(self, book, fileName):  #Пошук в одній книзі
        lengS = len(book.sheetnames)  #Кількість листів в книзі
        result = []  #Массив для додавання результатів
        for i in range(lengS):  #
            book.active = i
            sheetName = book.sheetnames[i]  #Отримуємо ім'я листа
            sheetBook = book.active  #Отримуємо активний лист (в теорії)
            resultSheet = self.__searchInOneSheet(sheetBook, sheetName, fileName)  #
            result.append(resultSheet)
        #print("Result for one book")
        #print(result)
        return result

    def __searchInOneSheet(self, sheet, sheetName, fileName):
        result = []  # Масив рядків які відповідають запиту
        for i in sheet:  # Перебір рядків в одному листі
            b = False  # Запис рядка в масив заборонено
            lenRow = len(i)  #Кількість ячеєк в рядку
            if lenRow >> self.__maxLenRow:  #Кількісне порівняння
                self.__maxLenRow = lenRow  #Запис максимального значення
            for x in i:  # Перебір ячеєк в одному рядку
                if x.value:
                    if self.__requestSearch.lower() in str(
                            x.value).lower():  # Перевірка на совпадіння слів (у нижньому регістрі) в ячейці
                        # if dat: #При пустому пошуку буде пуста таблиця
                        b = True  # Запис рядка в масив дозволено


            if b:  # Перевірка дозволу на запис рядка в масив
                r = self.__strresult(i)  # Формуємо рядок

                r = [sheetName] + r  # Додаэмо назву листа
                r = [fileName] + r  # Додаэмо назву файла
                if r:
                    result.append(r)  # Записуємо рядок в масив
                    self.__resultAll.append(r)
        #print("Result for one sheet")
        #print(result)
        return result

    def getTableDate(self):
        if self.__fileNames:
            self.__searchInAllBook()
            result = self.__resultAll
            return result
        print("Not filesName")
        return []
