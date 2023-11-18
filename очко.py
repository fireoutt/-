# -*- coding: utf-8 -*-

koloda = [6, 7, 8, 9, 10, 11, 2, 3, 4] * 4
import random
random.shuffle(koloda)

print('ставлю душу своей матери')
count = 0

while True:
    choice = input('берешь карту?')
    if choice == 'da':
        current = koloda.pop()
        print('ваша карта %d' % current)
        count += current
        if count > 21:
            print('АНЛАК)))')
            break
        elif count == 21:
            print('очко')
            break
        else:
            print('ровно %d птс' % count)
    elif choice == 'n':
        print('ваш птс это %d счет закончен' % count)
        break