# Shapshot thief
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/snapshot.jpg)


## Решение 

1. Переходим по пути 84.201.168.221:4000/dashboard/snapshot/:key
Отображается снапшот.

2. Удаляем его следующий запросом 
84.201.168.221:4000/api/snapshots-delete/:deleteKey?OrgId=0
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/st_1.jpg)


3. Повторяем до тех пор, пока в снапшоте в последней столбце не обнаружим флаг.
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/st_2.jpg)


## Ресурсы

https://github.com/kh4sh3i/Grafana-CVE

## Флаг
PermCTF{dfu8ikn6kpb1}