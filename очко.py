# -*- coding: utf-8 -*-

koloda = [6, 7, 8, 9, 10, 11, 2, 3, 4] * 4
import random
random.shuffle(koloda)

print('������ ���� ����� ������')
count = 0

while True:
    choice = input('������ �����?')
    if choice == 'da':
        current = koloda.pop()
        print('���� ����� %d' % current)
        count += current
        if count > 21:
            print('�����)))')
            break
        elif count == 21:
            print('����')
            break
        else:
            print('����� %d ���' % count)
    elif choice == 'n':
        print('��� ��� ��� %d ���� ��������' % count)
        break