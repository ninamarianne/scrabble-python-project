#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

buchstabenliste = ['A', 'A', 'A', 'A', 'A', 
        #'Ä',
        'B', 'B',
        'C', 'C',
        'D', 'D', 'D', 'D',
        'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E',
        'F', 'F',
        'G', 'G', 'G',
        'H', 'H', 'H', 'H',
        'I', 'I', 'I', 'I', 'I', 'I',
        'J',
        'K', 'K',
        'L', 'L', 'L',
        'M', 'M', 'M', 'M',
        'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N',
        'O', 'O', 'O',
        #'Ö',
        'P',
        'Q',
        'R', 'R', 'R', 'R', 'R', 'R',
        'S', 'S', 'S', 'S', 'S', 'S', 'S',
        'T', 'T', 'T', 'T', 'T', 'T',
        'U', 'U', 'U', 'U', 'U', 'U',
        #'Ü',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        '_', '_']

path = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
with open(path+"/wortsammlung.txt", 'r') as file:
    f = file.read()
    wortsammlung = f.lower()
file.close()


punktzahl = {'A': 1,
            'Ä': 6,
            'B': 3,
            'C': 4,
            'D': 1,
            'E': 1,
            'F': 4,
            'G': 2,
            'H': 2,
            'I': 1,
            'J': 6,
            'K': 4,
            'L': 2,
            'M': 3,
            'N': 1,
            'O': 2,
            'Ö': 8,
            'P': 4,
            'Q': 10,
            'R': 1,
            'S': 1,
            'T': 1,
            'U': 1,
            'Ü': 6,
            'V': 6,
            'W': 3,
            'X': 8,
            'Y': 10,
            'Z': 3,
            '_': 0
            }

