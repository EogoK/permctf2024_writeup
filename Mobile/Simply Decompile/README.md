# Simply Decompile
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/simply_decompile.jpg)

## Решение 1
1. Открываем сайт c онлайн декомпилятором JADX http://www.javadecompilers.com/apk 

2. Загружаем туда файл и нажимаем "Upload and Decompile"

3. Скачиваем архив и идем сначала к манифесту (файл resources/AndroidManifest.xml), чтобы узнать, где находится главный Activity
![AndroidManifest](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/sd_1.png)


4. Переходим по пути android:name, где лежит MainActivity.java и там захардкоженный флаг
![MainActivity](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/sd_2.png)


## Решение 2
```
strings Simply_Decompile.apk | grep PermCTF

# смотрит все печатаемые символы из файлика, а потом ищет строки похожие на PermCTF
```
![strings](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/sd_3.png)

## PS
Можно было и в любом hex-вьювере увидеть или через apktool посмотреть строки

## Словарь
JADX - декомпилятор из dex/apk в jar

Activity - это фрейм или интерфейс приложения

Главный (Main) Activity - активити, запускающееся при запуске приложения (должно иметь в интенте категорию LAUNCHER и action MAIN)

strings - unix-утилита, применяемая для поиска печатаемых строк в двоичных файлах

grep - поиск образца в файле

hex-вьювер - программа, которая показывает данные или текст в виде hex формата

apktool - утилита для исследования apk файлов

## Флаг
PermCTF{basic_android_reverse}