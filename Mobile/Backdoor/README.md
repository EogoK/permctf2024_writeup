# Backdoor
## Описание
![Описание задания](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/backdoor.jpg)

## Решение 
1. Открываем сайт c онлайн декомпилятором JADX http://www.javadecompilers.com/apk

2. Загружаем туда файл и нажимаем "Upload and Decompile"

3. Скачиваем архив и идем сначала к манифесту (файл resources/AndroidManifest.xml), видим, что у нас несколько активити, нас интересует только FlagActivity
![AndroidManifest](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/bd.png)

4. Видим там создание разных элементов, попробуем через adb посмотреть с телефона на этот активити
```
adb shell am start -n permctf.android.task3/.FlagActivity
```

5. Наблюдаем интересное окно на нашем устройстве и отправляем нашу команду и скрин @Oxygenation_9
![AndroidManifest](https://raw.githubusercontent.com/EogoK/permctf2024_writeup/refs/heads/main/photos/bd_3.png)

## Словарь

JADX - декомпилятор из dex/apk в jar

Activity - это фрейм или интерфейс приложения

adb (Android Debug Bridge) - это инструмент для управления андроидом через терминал
 * am - активити менеджер
 * am start - запуск активити на устройстве
 * am start -n - выбор запускаемого активити приложения

## Флаг
PermCTF{MASTER_APPROVED}