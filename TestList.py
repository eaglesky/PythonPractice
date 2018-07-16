#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    print('Testing list:')
    test_list = ['first', 'second', 'third']
    test_list.append('fourth')
    test_list.insert(1, 'inserted')

    # Common iteration using keyword in
    # 'inserted' is the second element in the list
    for word in test_list:
        print(word)

    # len() is used to get the number of items in a sequence (string, tuple or list) or a
    # mapping (dictionary)
    # range(..) returns a iterator!
    for id in range(len(test_list)):
        print('{}: {}'.format(id, test_list[id]))

    test_list2 = list(test_list)
    print('test_list2 is copy of test_list1: {}'.format(test_list2))
    print('test_list2 is test_list? {}'.format(test_list2 is test_list))
    # Items are compared lexicographically in all sequence types, when using '=='
    print('test_list2 is equal to test_list? {}'.format(test_list2 == test_list))
    test_list2.sort()
    print('sorted test_list2: {}'.format(test_list2))
    print('sorted test_list2 is equal to test_list? {}'.format(test_list2 == test_list))