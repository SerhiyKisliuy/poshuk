from openpyxl import load_workbook

def strresult(m):
    res = []
    for i in m:
        x = i.value  # Значення в ячейці
        if x:
            res.append(str(i.value))
        else:
            res.append('-')  # Якщо немає значення в ячейці то створюємо відступ
    return res

def search(filename, entry):

    wb = load_workbook(filename, data_only=True)  #завантаження книги
    print(wb.sheetnames)

    for i in range(len(wb.sheetnames)):  #перебір по таблицям (ws - Листи, wb - вся книга)
        print(i)
        wb.active = i
        ws = wb.active
        print(ws[2])
        dat = entry
        result = []

        #print('____  ' + wb.sheetnames[ws] + '  ____')  # Друкуємо назву листа
        head = []
        le = len(ws[1])  #додаєм стовбців для імен файла та листа
        for s in range(le):  #розмір рядка (кількість слів)
            head.append(str(s))

        head = ['Лист'] + head
        head = ['Файл'] + head

        # print(m)  # Друкуємо першу строку таблиці
        wsd = ws

        #wsd.delete_rows(0)  # Видаляємо першу строку в таблиці

        for i in wsd:  # Перебор строк
            b = False
            for x in i:  # Перебор ячеєк
                if x.value:

                    if dat.lower() in str(x.value).lower():  # Перевірка на совпадіння слів (у нижньому регістрі)
                        #if dat: #при пустому пошуку буде пуста таблиця
                            b = True

            if b:
                r = strresult(i)  # Формуємо строку
                lis = wb.sheetnames[0]
                r = [lis] + r
                r = [filename] + r
                if r:
                    result.append(r)  # Формуємо список строк

        return head, result



