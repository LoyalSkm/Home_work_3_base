from math import sqrt
import string

def disc():
    def prov(mes):
        while True:
            try:
                val = float(input(mes))
                return val
            except:
                print("Должны быть числом, повторите ввод!")
    a = prov("Введите значения a: ")
    b = prov("Введите значения b: ")
    c = prov("Введите значения с: ")

    D = (b ** 2) - 4 * a * c
    print("Дискриминант: D = " + str(D))

    try:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print("x1 = " + str(x1) + " x2 = " + str(x2))
    except:
        print("Нет решения, дискриминант отрицательный")

'''**********************************************************'''

def link_found():
    url = input("Ввести ссылку в формате \"https://www.google.com/?search/478257/...-=\": ")
    substr = '://'
    # subend = '.com/'
    if '.ru/' in url:
        subend = '.ru'
    if '.com/' in url:
        subend = '.com'
    if '.net/' in url:
        subend = '.net'
    if '.ua/' in url:
        subend = '.ua'
    while substr and (subend + "/") not in url:
        return "Не корректный url"
    else:
        index_str = url.find(substr) + len(substr)
        index_nd = url.find(subend) + len(subend)
        if url.find(substr)!= -1:
            api_id  = url[index_str:index_nd]
            print(api_id)
'''**********************************************************'''

def correct_name():

    name = str(input("Введите полное имя для корректировки: "))

    def chelenge(x):
        Low_fullN = x.lower()         # делаю все слова с ималенькой буквы
        Separate = Low_fullN.split()  # делю введённую строку на отдельные слова
        num = len(Separate)           # количество введённых слов

        for i in range(0, num):
            word = Separate[i]            # беру первое слово из списка
            Letter_1 = word[0][0].upper() # отделяю первую букву и делаю ее заглавной списка
            end_word = word[1:]           # удаляю первую букву из слова
            D = Letter_1 + end_word       # прибавляю первую букву первого слова к первому слову по списку
            print(D, end=' ')
    return chelenge(name)

'''**********************************************************'''

def vote():
    print('''   Выберите интерисующее задание:
              1 задание - 1 (Квадратное уровнение)
              2 задание - 2 (Вывод адреса сайта)
              3 задание - 3 (Вывод нормальный вид ФИО)
        ''')

    v1 = int(input("Ваш выбор: "))
    v2 = 0
    if v1 == 1:
         v2 = disc()
    elif v1 == 2:
        v2 = link_found()
    elif v1 == 3:
        v2 = correct_name()
    return(v2)

vote()
# link_found()