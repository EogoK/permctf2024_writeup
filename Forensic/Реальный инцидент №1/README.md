# Реальный инцидент №1
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc1.jpg)


## Решение 1

1. Откроем файл в Wireshark из задания и посмотрим стек запросов предполагаемой эксплуатации атаки

2. В графе Proto видим частое упоминание протокола SMB. Попробуем загуглить уязвимости возможные на этом протоколе. И переберем.

![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc1_1.png)


## Решение 2

1. откроем файл в Wireshark из задания и посмотрим стек запросов предполагаемой эксплуатации атаки

2. Видим частое упоминание протокола SMB, давайте узнаем с какого порта велась атака.

![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc1_2.png)

3. Также в тех же пакетах можно заметить упоминание Windows, поэтому можем предположить, что атака велась на операционную систему Windows.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc1_3.png)

4. Windows 2000, давайте попробуем поискать, какие атаки существуют на эту ОС и протокол SMB.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc1_4.png)


## Словарь

Wireshark - это инструмент для захвата и анализа сетевого трафика

## Ресуры

https://book.hacktricks.xyz/network-services-pentesting/pentesting-smb


## Флаг
PermCTF{MS08-068}