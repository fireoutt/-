# -*- coding: utf-8 -*-

koloda = [6, 7, 8, 9, 10, 11, 2, 3, 4] * 4
import random
random.shuffle(koloda)      

print('bet my mothers soul')
count = 0

while True:
    choice = input('take card?')
    if choice == 'da':
        current = koloda.pop()
        print('your card %d' % current)
        count += current
        if count > 21:
            print('UNLUCK)))')
            break
        elif count == 21:
            print('ochko')
            break
        else:
            print('equal %d pts' % count)
    elif choice == 'n':
        print('your pts is $d count is ended' % count)
        break
