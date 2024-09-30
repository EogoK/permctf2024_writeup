# библиотека ГОСТ криптографии
import gostcrypto

# хеш задания
cipher = "f31ee7104596eb96f0edddfacbafeff24f21fda7f1e3dbec97bce430a70fa2f6"

# создаем указатель к файлику (ну или дескриптор кому как удобно называть) 
with open('rockyou.txt', 'r') as f:
    # пробегаемся по каждой строке в файле вордлиста
    for line in f:
        # удаляем символ переноса строки
        line = line.rstrip('\n')
        # создаем временную переменную резалт для вывода заведомого ответа
        result = line
        
        # цикл работает 5 раз
        for i in range(5):
            # cоздаешь объект хеша стрибога256 по нашей строке из вордлиста
            hash_object = gostcrypto.gosthash.new('streebog256', data=line.encode())
            # переводим из объекта хеша в строку
            line = hash_object.hexdigest()
        
        # отлаживаем результаты
        print(f"Text: {result} | Cipher: {line}")
        #сравниваем равен ли хеш задания с хешом, который мы получаем 5-ричного хеширования строки вордлиста
        if line == cipher:
            #ответ
            print(f"!Answer: {result}")
            #заверщаем цикл
            break