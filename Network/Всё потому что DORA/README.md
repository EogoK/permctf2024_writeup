# Dora
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/dora.jpg)


## Решение 


1. Открываем файл через wireshark и отфильтруем по протоколам

2. Зная, что DORA базируется на DHCP

3. Видим странные байты в Option -> Host Name каждого пакета, давайте сделаем вывод этих байтов
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/dora_1.png)

## Ресурсы

https://www.xelent.ru/blog/printsipy-raboty-protokola-dhcp/


## Флаг
PermCTF{dora_the_traveler}