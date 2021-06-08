# Задача 1.
Вы работаете в Яндекс.Поиск, пользователи часто добавляют в поисковую систему схожие элементы. Вы должны разработать алгоритм, который бы нашёл повторяющиеся элементы и вывела бы их имя и количество на экран. 

**Ввод:** количество элементов, элементы в формате: Имя_элемента, описание_элемента; с новой строки.<br>
**Вывод:** название элемента и количество повторений в формате: {'Имя_элемента'} = количество_повторений

Мы гарантируем, что вы получаете название и описание в input через ",".

Пример 1.<br>
Input:
```
3
LEarn Python, The site contains content about python programming language
learn python, New description
Learn C++, c++ site description.
```
Output: 
```
{'Learn Python'} = 2.
```

Пример 2.<br>
Input:
```
4
google, An American multinational corporation.
Google, The most popular search engine in the world.
Microsoft, one of the largest multinational companies producing proprietary software for various types of computing equipment
microsoft, the company that developed the worst operating system.
```
Output:
```
{'google'} = 2
{'microsoft'} = 2
```

# Задача 2.

На этот раз вы разработчик в Яндекс.Go. Вы должны определить заработную плату водителя на основе общего списка заказов. Учитывайте, что зарплата водителя фиксированная - 200₽ за поездку.

**Ввод:** 
* количество заказов.
* информация о заказе в формате: имя_водителя -> имя_пассажира; с новой строки. 
* имя водителя, у которого мы должны подсчитать зарплату.

**Вывод:**
* Информация о зарплате водителя в формате: имя_водителя: зарплата₽

Пример 1.<br>
Input:
```
7
Andrew Walker -> Max Smith
Sara Stewart -> Kenneth Jones
William Mills -> Kenneth Jones
Joseph Ross -> Max Smith
Elsie Chapman -> William Johnson
Elsie Chapman -> Max Smith
Elsie Chapman -> Kenneth Jones
Elsie Chapman
```
Output:
```
Elsie Chapman: 600₽
```

# Задача 3.

На этот раз вам не повезло и вы разработчик в «Школьный портал». У вас есть успеваемость класса, на основе которой вы должны определить худшего и лучшего ученика класса.

**Ввод:**
* Количество оценок учеников
* Список оценок учеников в формате: имя_ученика: оценка; с новой строчки.

**Вывод:**<br>
Ученик с минимальным и максимальным средним баллом.

Пример.<br>
Input:
```
8
Andrew Walker: 3
Sara Stewart: 5
William Mills: 4
Joseph Ross: 2
Sara Stewart: 5
Joseph Ross: 3
Andrew Walker: 5
William Mills: 4
```
Output:
```
Худший - Joseph Ross
Лучший - Sara Stewart
```

# Задача 4.

Вы работаете в Eduprog, вы должны создать анализатор, который бы переводил JSON представление тестового случая, в представление на языке программирования Python.

**Ввод**: данные в формате JSON.<br>
**Вывод**: структура данных, в который были записаны данные.

Пример.<br>
Input:
```
{"input_expression":5,"output_expression":120}
```
Output:
```
{'input_expression': '5'}
{'output_expression': '120}'}
```