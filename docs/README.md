# <span style="color: #00FF00;">Geometry_lib</span>

## <span style="color: #0000FF;">Geometry_lib - является пайтон библиотекой с базовыми функциями для вычисления площадей и периметров таких фигур ,как: треугольник , квадрат , прямоугольник и круг.</span>

![geometry](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYG0RgfUb_2QjwlBOmik9nERItKh5VLKRMpw&s)
---

## <span style="color: #0000FF;">Краткое описание библиотеки:</span>
### Использование:

- Чтобы использоавть библиотеку ,клонируйте данный репозиторий в папку с проектом через команду:

    >git clone <ссылка>

- После импортируйте библиотеку в пайтон файл следующей командой и приступайте к написанию кода:
    ```python
    from geometry_lib import*
    ```
<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> более подробно расписано в папке docs.
</p>

## <span style="color: #0000FF;">Коды функций:</span>
### Круг
```python
import math

def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r
```
### Треугольник
```python
def area(a, h): 
    return a * h / 2

def perimeter(a, b, c): 
    return a + b + c 
```
### Прямоугольник
```python
def area(a, b):
    return a * b

def perimeter(a, b):
    return 2 * (a + b)
```
### Квадрат
```python
def area(a):
    return a * a

def perimeter(a):
    return 4 * a
```

<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> для более полного ознакомления смотрите .py файлы и папку docs.
</p>

## <span style="color: #0000FF;">Формулы:</span>
| геометрическая фигуры| формулы |
|:-------------|:-----------:|
|   Круг       | S = πR²     |
| Прямоугольник| S = ab      |
|  Квадрат     |  S = a²     |
| Треугольник  | (a*h)/2     |
## Периметр
| геометрическая фигуры| формулы |
|:-------------|:-----------:|
|   Круг       | P = 2πR     |
| Прямоугольник| P = 2(a + b)|
|  Квадрат     |  P = 4a     |
| Треугольник  | a + b + c   |
<p style="color: gray; font-size: 90%;">
<b>Примечание:</b> более подробно расписано в папке docs.
</p>
