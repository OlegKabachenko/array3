#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import importlib
from TK_1 import input_data_from_console
from TK_2 import find_min_max
from TK_3 import get_average_list
from TK_4 import get_multiplication_list
def main():
    count = int(input('Get count data:'))
    list_data = input_data_from_console(count)
    print('Max/Min:' + str(find_min_max(list_data)))
    print('List_Of_Values_Divided_On_Average:' + str(get_average_list(list_data)))
    print('List_Of_Multiplicated_Values:' + str(get_multiplication_list(list_data)))
    print('List_Of_Root_Values:' + str(get_root_list(list_data)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
