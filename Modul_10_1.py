from datetime import datetime
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i + 1}' + '\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start

print(f'Работа потоков: {time_res}')

time_start2 = datetime.now()

thr_one = Thread(target=write_words, args=(10, 'example5.txt'))
thr_two = Thread(target=write_words, args=(30, 'example6.txt'))
thr_three = Thread(target=write_words, args=(200, 'example7.txt'))
thr_four = Thread(target=write_words, args=(100, 'example8.txt'))

thr_one.start()
thr_two.start()
thr_three.start()
thr_four.start()

thr_one.join()
thr_two.join()
thr_three.join()
thr_four.join()

time_end2 = datetime.now()
time_res2 = time_end2 - time_start2

print(f'Работа потоков: {time_res2}')