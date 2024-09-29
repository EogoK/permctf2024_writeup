# Pin Bypass
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/pin_bypass.jpg)

## Решение 
1. Открываем сайт c онлайн декомпилятором JADX http://www.javadecompilers.com/apk

2. Загружаем туда файл и нажимаем "Upload and Decompile"

3. Скачиваем архив и идем сначала к манифесту (файл resources/AndroidManifest.xml), чтобы узнать, где находится главный Activity
![AndroidManifest](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/pb_1.png)

4. Переходим по пути android:name, где лежит MainActivity.java
![MainActivity](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/pb_2.png)

5.
    * Видим в строке, что из xor_pincode возврашается значение равное 6554, а в аргументе метода - значение из pinCodeEditText, которое приводится к целочисленному
    * Затем читаем метод xor_pincode и видим, что на выводе метода строка, в которую форматирируется какое-то число, и оно вычисляется по XOR операции
   ```
   user_input ^ XOR_KEY
   ```
    * Далее мы видим статичную переменную XOR_KEY и просто в калькуляторе или удобном другом интерфейсе вычисляем ответ
   ```
   user_input ^ XOR_KEY = 6554
   user_input = 6554 ^ XOR_KEY
   user_input = 6554 ^ 1337
   user_input = 7331
   ```
   ![xor.pw](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/pb_3.png)

## Словарь

JADX - декомпилятор из dex/apk в jar

Activity - это фрейм или интерфейс приложения

Главный (Main) Activity - активити, запускающееся при запуске приложения (должно иметь в интенте категорию LAUNCHER и action MAIN)


## Флаг
PermCTF{7331}