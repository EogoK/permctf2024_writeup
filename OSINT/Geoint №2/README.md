# Geoint 2
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/geoint2.jpg)


## Решение 

1. Попробуем конвертнуть из IMG_4073.HEIC в PNG и посмотреть, что на картинке (на линукс не открывает heic)

2. Здесь мы можем заметить мост, от которого можно отталкиваться, и попробуем закинуть эту обрезанную картинку в яндекс.картинки
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gi2_1.png)
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gi2_2.png)

3. И это у нас Большой Обуховский мост и это Питер! Интересно, давайте еще посмотрим, что видно на картинке, в самом низу видим автобус 115. Давайте посмотрим, как он ходит на яндекс.картах.  
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gi2_3.png)

4. Круг поиска сузился, напоследок посмотрим немного повыше на Ниву и увидим пяторочку, попробуем поискать ее в этом районе.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gi2_4.png)

5. Начнем с пятерочки, которая самая отдаленная, и видим, что вот этот дом, который мы искали.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gi2_5.png)


## Словарь
Реверсивный поиск - это технология, которая позволяет искать изображения в интернете, используя сами изображения, а не слова

## Флаг
PermCTF{Санкт-Петербург_Советский_проспект_39/1}