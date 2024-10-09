# Реальный инцидент №3
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc3.jpg)


## Решение 

1. открываем тот же файл из первого задания

2. smb2.read.blob ставим в фильтр и сортируем по размеру 

![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc3_1.png)

3. Видим сигнатуру excel таблички и дампаем в файл через File -> export packet bytes

![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/rc3_2.png)

4. Как вы возможно и поняли, это была ловушка, поэтому ищем дальше и переходим на следующую страничку
    

## Флаг
PermCTF{ООО_АК_ЭЙРБРИДЖКАРГО}