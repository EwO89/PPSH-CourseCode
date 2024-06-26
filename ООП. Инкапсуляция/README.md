# ООП. Инкапсуляция

## Задача 1

Приёмная комиссия НИУ "Московский исследовательский институт рандома" попросила упростить работу комиссии из-за нескончаемого потока абитуриентов в этом году. Вам поручили реализовать интерфейс взаимодействия поступающих с "Центральным распределительным модулем".

Чтобы абитуриенты не знали, как работает система, все атрибуты классов были запривачены.

У университета уже есть две функции, которые помогают им обеспечивать работу:

* `__fetch_RNE()` — возвращает баллы ЕГЭ, которые путём некоторых махинаций должны браться из официальной базы данных. 
* `__check()` — функция автоматического ответа на вопросы "я прохожу?", поступающие на почту приёмной комиссии.

Текущая реализация дана ниже, но она не работает, потому что не все функции ещё реализованы:

```python
from random import *

class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()

        # добавление абитуриента в словарь, 
        # где информация хранится под СНИЛСами
        self.__abiturients[number] = abiturient


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age

        # СНИЛС
        self.__number = number

        # Russian National Exam (ЕГЭ), баллы 
        self.__RNE = self.__fetch_RNE()

        # есть ли БВИ
        self.__bvi = bvi

    # функция получения результатов ЕГЭ
    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))

    # функция ответа на вопрос, проходит ли абитуриент
    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"


module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))

# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))

# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))
```

Информацию об абитуриентах нужно как отображать, так и иметь возможность изменить в случае ошибки. Реализуйте следующие **getter**-ы и **setter**-ы для класса `Abiturient()` для следующих данных:

* ФИО абитуриента (`__surname`, `__name`, `__patronymic`);
* возраст абитуриента (`__age`);
* баллы ЕГЭ абитуриента (`__RNE`);
* статус БВИ абитуриента (`__bvi`).

Значения СНИЛС изменить нельзя, потому что под их номерами хранится сама информация об абитуриентах в словаре `self.__abiturients`, поэтому:

* реализуйте только **getter** `get_number(self)` для получения информации о СНИЛСе абитуриента;
* реализуйте **getter** `get_status(self, number)` для получения информации о том, проходит ли абитуриент;
* на текущий момент метод `add()` в классе `CRM()` может перезаписать информацию уже существующего абитуриента полностью заново. Исправьте это, добавив соответствующую проверку.

## Задача 2

В сказке А. С. Пушкина "Сказка о царе Салтане" упоминается невиданное чудо: остров, на котором живёт белка, которая грызёт орехи из чистого золота с изумрудными ядрами. Ниже приведён этот отрывок:

```
«Мы объехали весь свет;
За морем житье не худо;
В свете ж вот какое чудо:
Остров на море лежит,
Град на острове стоит
С златоглавыми церквами,
С теремами да садами;
Ель растет перед дворцом,
А под ней хрустальный дом;
Белка там живет ручная,
Да затейница какая!
Белка песенки поет,
Да орешки всё грызет,
А орешки не простые,
Всё скорлупки золотые,
Ядра — чистый изумруд;
Слуги белку стерегут,
Служат ей прислугой разной —
И приставлен дьяк приказный
Строгий счет орехам весть;
Отдает ей войско честь;
Из скорлупок льют монету,
Да пускают в ход по свету;
Девки сыплют изумруд
В кладовые, да под спуд;
Все в том острове богаты,
Изоб нет, везде палаты;
А сидит в нем князь Гвидон;
Он прислал тебе поклон».
```

Мы понимаем, что А. С. Пушкин описывает чрезвычайно хорошо налаженный процесс поднятия экономики княжества с помощью золотых монет и изумрудов.

**Напишите реализацию этого процесса.** В нём участвуют несколько ключевых объектов, взаимодействие с которыми ради обеспечения безопасности казны осуществляется **только** с помощью **setter**-ов и **getter**-ов, которые вам необходимо реализовать. Это позволит скрыть от чужих глаз то, что трогать не следует. Вот инициализации и описания ключевых объектов:


### Изумруд (`Emerald`)

```python
class Emerald:
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0

        # цена изумруда
        self.__price = 0
```

Что можно делать с изумрудом:

* получать информацию о статусе;
* изменять информацию о статусе:
    * числовое значение статуса изумруда не может стать меньше;
    * учитывать (`account()`);
    * отправлять под спуд (`store()`);
* оценивать изумруд;
* получать информацию о цене изумруда.


### Скорлупка (`Shell`)

```python
class Shell:
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0

        # цена скорлупки
        self.__price = 0
```

Что можно делать со скорлупкой:

* получать информацию о статусе;
* изменять информацию о статусе:
    * числовое значение статуса скорлупки не может стать меньше.
    * учитывать (`account()`);
    * отправлять в монетолитейное отделение (`process()`);
    * переплавлять в монету (`smelt()`);
        * в таком случае создаётся новый объект: монета `Coin()` -- для неё нужно создать запись в архиве;
* оценивать скорлупку;
* получать информацию о цене скорлупки.
* для изменения статуса можно предварительно реализовать **setter**, а затем вызывать его в реализации вышеописанных функций.

### Монета (`Coin`)

```python
class Coin:
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number

        # год выпуска монеты
        self.__year = year

        # номинал монеты
        self.__value = value
```

При создании монеты все её атрибуты инициализируются и потом нигде не изменяются. Что можно делать с монетой:

* получать информацию о серийном номере;
* получать информацию о годе выпуска;
* получать информацию о номинале монеты;

### Запись (`Entry`)

```python
class Entry: 
    def __init__(self, item, date="01.01.1970", info="", secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()

        # указатель на объект
        self.__item = item

        # дата создания записи 
        self.__date = date 

        # дополнительная информация об объекте
        self.__info = info

        # информация засекречена?
        self.__secret = secret
    
    def __get_next_ID(self):
        # можно создать свою функцию вместо этой
        return hash(self)
```

Что можно делать с записью:

* получать информацию об ID объекта;
* получать информацию о записанном объекте;
* получать информацию о дате создания записи;
* получать дополнительную информацию об объекте;
* изменять дополнительную информацию об объекте;
* получать информацию о засекреченности записи;
* засекречивать или рассекречивать запись.

### Архив (`Archive`)

```python
class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []
```

Что можно делать с помощью архива:

* добавлять запись `Entry()` о новом изумруде/скорлупке/монете (`add()`) в конец архива;
* получать информацию из записи об изумруде/скорлупке/монете из архива по индексу (`get()`);
    * здесь нужно реализовать **getter** для атрибутов как записи `Entry()` (получение типа сохранённого объекта, даты записи, дополнительной информации), так и атрибутов объектов (`Coin()`, `Shell()`, `Emerald()`), на которые указывает `self.__item`;
    * при попытке получить информацию об удалённом или засекреченном объекте нужно возвращать `None`;
* изменять запись об изумруде/скорлупке/монете в архиве (`edit()`) по индексу;
    * менять указатель на объект **нельзя**;
    * дату создания изменять **нельзя**;
    * дополнительную информацию изменять **можно**, здесь нужно реализовать **setter**;
* засекречивать информацию о записи (`classify()`) по индексу;
    * в таком случае получить информацию об этой записи нельзя;
* рассекречивать информацию о записи (`declassify()`) по индексу;
    * в этом случае ограничения на получение информации снимаются;
* удалять запись об изумруде/скорлупке/монете (`delete()`) по индексу;
    * в таком случае запись по индексу перезаписывается на `None`.

### Проверка

> #### Отображение информации (необязательное задание)
>
> Создайте **getter** для создания строкового отображения архива.
>
> * используйте этот метод, чтобы выводить всю информацию, которая хранится в архиве, на экран после каждого из шагов;
> * можно использовать этот метод после каждого из пунктов ниже, чтобы визуализировать статус архива.

#### Реализация

Для того, чтобы удостовериться, что вы всё реализовали правильно, запустите следующие действия процесса:

* создайте архив;
* создайте 20 объектов `Shell()` и 10 объектов `Emerald()`;
* оцените все созданные объекты и учтите их в архиве, создав соответствующие записи `Entry()`;
* отправьте все изумруды `Emerald()` под спуд, а скорлупки `Shell()` в монетолитейное отделение, обновив существующие записи о них;
* переплавьте все золотые скорлупки `Shell()` в монеты `Coin()`, обновите существующие записи о скорлупках и создайте новые о монетах;
* засекретьте все записи об изумрудах;
* удалите записи о скорлупках;
* рассекретьте часть записей об изумрудах;
* добавьте дополнительную информацию к записям о рассекреченных изумрудах;
* получите информацию о всех монетах в архиве.

> Вспомните, какие способы реализации были в ролике, и попытайтесь использовать как можно больше из них. Это позволит вам проработать различные способы соблюдения парадигмы инкапсуляции.*
