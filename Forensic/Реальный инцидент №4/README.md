# Реальный инцидент №4
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc4.jpg)


## Решение 

1. открываем тот же файл из первого задания

2. Попробуем отсортировать по SMTP и найти, кому отправилось. Также давайте поищем кому вообще что-то отправлялось фильтром
```
smtp.req.command == "RCPT"
```
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc4_1.png)



## Ресурсы

https://selectel.ru/blog/smtp-protocol/

## Флаг
PermCTF{director@negative.tech}