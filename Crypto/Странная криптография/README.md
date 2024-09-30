# Странная криптография
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/crypto.jpg)

## Подсказки
![Подсказка2](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/crypto_hint2.jpg)
![Подсказка1](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/crypto_hint.jpg)

## Решение 
1. При открытии файла видим текст с хешом
![текст](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/cr_1.png)

2. Попробуем идентифицировать хеш с помощью hashcat и видим, что несколько вариантов (в основном sha256)
```
hashcat <ХЕШ>
```

3. Прочитаем снова задание и видим, что часто повторяется число 5 и в уведомлении поймем, что это хеш-функция STREEBOG 256

4. Очевидно, что нужно хешировать каждую строку в вордлисте rockyou.txt 5 раз и потом попробовать искать похожий хеш(скрипт solve.py) и получаем ответ
![решение](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/cr_2.png)

## Словарь
hashcat - это инструмент для восстановления пароля методом перебора при известном хеше

hash (хеш) - это строка или набор данных в виде короткой строки, в лучшем случае уникальна и созданная путем преобразования сообщения с использованием мат. функций

## Ресурсы
https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%B8%D0%B1%D0%BE%D0%B3_(%D1%85%D0%B5%D1%88-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F)
https://github.com/drobotun/gostcrypto



## Флаг
PermCTF{spongebob}