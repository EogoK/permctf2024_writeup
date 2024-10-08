# Реальный инцидент №2
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc2.jpg)


## Решение 

1. Открываем тот же файл из прошлого задания

2. Попробуем найти возможные способы создания юзера с локальными правами админа.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc2_1.png)

3. Хм, net user, давайте используем поиск в wireshark по hex и попробуем найти подобные строки.
```
"net user" > "6e65742075736572"
```
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc2_2.png)

4. И получаем наши креды для флага
```
net user "Пользователь" "Пароль" 
```

## Флаг
PermCTF{user_Passw0rd}