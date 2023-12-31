sex_mapping = {
    1: 'Male',
    2: 'Female'
}

disability_mapping = {
    1: 'With a disability',
    2: 'Without a disability'
}

worker_class_mapping = {
    1: "Employee of a private for-profit company or business, or of an individual, for wages, salary, or commissions",
    2: "Employee of a private not-for-profit, tax-exempt, or charitable organization",
    3: "Local government employee (city, county, etc.)",
    4: "State government employee",
    5: "Federal government employee",
    6: "Self-employed in own not incorporated business, professional practice, or farm",
    7: "Self-employed in own incorporated business, professional practice or farm",
    8: "Working without pay in family business or farm",
    9: "Unemployed and last worked 5 years ago or earlier or never"
}

is_STEM_field_mapping = {
    1: "Yes",
    2: "No"
}

arrival_hours_mapping = {
    'bb': "N/A (not a worker; worker who worked at home)",
    1: "12:00 a.m. to 12:04 a.m.",
    2: "12:05 a.m. to 12:09 a.m.",
    3: "12:10 a.m. to 12:14 a.m.",
    4: "12:15 a.m. to 12:19 a.m.",
    5: "12:20 a.m. to 12:24 a.m.",
    6: "12:25 a.m. to 12:29 a.m.",
    7: "12:30 a.m. to 12:39 a.m.",
    8: "12:40 a.m. to 12:44 a.m.",
    9: "12:45 a.m. to 12:49 a.m.",
    10: "12:50 a.m. to 12:59 a.m.",
    11: "1:00 a.m. to 1:04 a.m.",
    12: "1:05 a.m. to 1:09 a.m.",
    13: "1:10 a.m. to 1:14 a.m.",
    14: "1:15 a.m. to 1:19 a.m.",
    15: "1:20 a.m. to 1:24 a.m.",
    16: "1:25 a.m. to 1:29 a.m.",
    17: "1:30 a.m. to 1:34 a.m.",
    18: "1:35 a.m. to 1:39 a.m.",
    19: "1:40 a.m. to 1:44 a.m.",
    20: "1:45 a.m. to 1:49 a.m.",
    21: "1:50 a.m. to 1:59 a.m.",
    22: "2:00 a.m. to 2:04 a.m.",
    23: "2:05 a.m. to 2:09 a.m.",
    24: "2:10 a.m. to 2:14 a.m.",
    25: "2:15 a.m. to 2:19 a.m.",
    26: "2:20 a.m. to 2:24 a.m.",
    27: "2:25 a.m. to 2:29 a.m.",
    28: "2:30 a.m. to 2:34 a.m.",
    29: "2:35 a.m. to 2:39 a.m.",
    30: "2:40 a.m. to 2:44 a.m.",
    31: "2:45 a.m. to 2:49 a.m.",
    32: "2:50 a.m. to 2:54 a.m.",
    33: "2:55 a.m. to 2:59 a.m.",
    34: "3:00 a.m. to 3:04 a.m.",
    35: "3:05 a.m. to 3:09 a.m.",
    36: "3:10 a.m. to 3:14 a.m.",
    37: "3:15 a.m. to 3:19 a.m.",
    38: "3:20 a.m. to 3:24 a.m.",
    39: "3:25 a.m. to 3:29 a.m.",
    40: "3:30 a.m. to 3:34 a.m.",
    41: "3:35 a.m. to 3:39 a.m.",
    42: "3:40 a.m. to 3:44 a.m.",
    43: "3:45 a.m. to 3:49 a.m.",
    44: "3:50 a.m. to 3:54 a.m.",
    45: "3:55 a.m. to 3:59 a.m.",
    46: "4:00 a.m. to 4:04 a.m.",
    47: "4:05 a.m. to 4:09 a.m.",
    48: "4:10 a.m. to 4:14 a.m.",
    49: "4:15 a.m. to 4:19 a.m.",
    50: "4:20 a.m. to 4:24 a.m.",
    51: "4:25 a.m. to 4:29 a.m.",
    52: "4:30 a.m. to 4:34 a.m.",
    53: "4:35 a.m. to 4:39 a.m.",
    54: "4:40 a.m. to 4:44 a.m.",
    55: "4:45 a.m. to 4:49 a.m.",
    56: "4:50 a.m. to 4:54 a.m.",
    57: "4:55 a.m. to 4:59 a.m.",
    58: "5:00 a.m. to 5:04 a.m.",
    59: "5:05 a.m. to 5:09 a.m.",
    60: "5:10 a.m. to 5:14 a.m.",
    61: "5:15 a.m. to 5:19 a.m.",
    62: "5:20 a.m. to 5:24 a.m.",
    63: "5:25 a.m. to 5:29 a.m.",
    64: "5:30 a.m. to 5:34 a.m.",
    65: "5:35 a.m. to 5:39 a.m.",
    66: "5:40 a.m. to 5:44 a.m.",
    67: "5:45 a.m. to 5:49 a.m.",
    68: "5:50 a.m. to 5:54 a.m.",
    69: "5:55 a.m. to 5:59 a.m.",
    70: "6:00 a.m. to 6:04 a.m.",
    71: "6:05 a.m. to 6:09 a.m.",
    72: "6:10 a.m. to 6:14 a.m.",
    73: "6:15 a.m. to 6:19 a.m.",
    74: "6:20 a.m. to 6:24 a.m.",
    75: "6:25 a.m. to 6:29 a.m.",
    76: "6:30 a.m. to 6:34 a.m.",
    77: "6:35 a.m. to 6:39 a.m.",
    78: "6:40 a.m. to 6:44 a.m.",
    79: "6:45 a.m. to 6:49 a.m.",
    80: "6:50 a.m. to 6:54 a.m.",
    81: "6:55 a.m. to 6:59 a.m.",
    82: "7:00 a.m. to 7:04 a.m.",
    83: "7:05 a.m. to 7:09 a.m.",
    84: "7:10 a.m. to 7:14 a.m.",
    85: "7:15 a.m. to 7:19 a.m.",
    86: "7:20 a.m. to 7:24 a.m.",
    87: "7:25 a.m. to 7:29 a.m.",
    88: "7:30 a.m. to 7:34 a.m.",
    89: "7:35 a.m. to 7:39 a.m.",
    90: "7:40 a.m. to 7:44 a.m.",
    91: "7:45 a.m. to 7:49 a.m.",
    92: "7:50 a.m. to 7:54 a.m.",
    93: "7:55 a.m. to 7:59 a.m.",
    94: "8:00 a.m. to 8:04 a.m.",
    95: "8:05 a.m. to 8:09 a.m.",
    96: "8:10 a.m. to 8:14 a.m.",
    97: "8:15 a.m. to 8:19 a.m.",
    98: "8:20 a.m. to 8:24 a.m.",
    99: "8:25 a.m. to 8:29 a.m.",
    100: "8:30 a.m. to 8:34 a.m.",
    101: "8:35 a.m. to 8:39 a.m.",
    102: "8:40 a.m. to 8:44 a.m.",
    103: "8:45 a.m. to 8:49 a.m.",
    104: "8:50 a.m. to 8:54 a.m.",
    105: "8:55 a.m. to 8:59 a.m.",
    106: "9:00 a.m. to 9:04 a.m.",
    107: "9:05 a.m. to 9:09 a.m.",
    108: "9:10 a.m. to 9:14 a.m.",
    109: "9:15 a.m. to 9:19 a.m.",
    110: "9:20 a.m. to 9:24 a.m.",
    111: "9:25 a.m. to 9:29 a.m.",
    112: "9:30 a.m. to 9:34 a.m.",
    113: "9:35 a.m. to 9:39 a.m.",
    114: "9:40 a.m. to 9:44 a.m.",
    115: "9:45 a.m. to 9:49 a.m.",
    116: "9:50 a.m. to 9:54 a.m.",
    117: "9:55 a.m. to 9:59 a.m.",
    118: "10:00 a.m. to 10:04 a.m.",
    119: "10:05 a.m. to 10:09 a.m.",
    120: "10:10 a.m. to 10:14 a.m.",
    121: "10:15 a.m. to 10:19 a.m.",
    122: "10:20 a.m. to 10:24 a.m.",
    123: "10:25 a.m. to 10:29 a.m.",
    124: "10:30 a.m. to 10:34 a.m.",
    125: "10:35 a.m. to 10:39 a.m.",
    126: "10:40 a.m. to 10:44 a.m.",
    127: "10:45 a.m. to 10:49 a.m.",
    128: "10:50 a.m. to 10:54 a.m.",
    129: "10:55 a.m. to 10:59 a.m.",
    130: "11:00 a.m. to 11:04 a.m.",
    131: "11:05 a.m. to 11:09 a.m.",
    132: "11:10 a.m. to 11:14 a.m.",
    133: "11:15 a.m. to 11:19 a.m.",
    134: "11:20 a.m. to 11:24 a.m.",
    135: "11:25 a.m. to 11:29 a.m.",
    136: "11:30 a.m. to 11:34 a.m.",
    137: "11:35 a.m. to 11:39 a.m.",
    138: "11:40 a.m. to 11:44 a.m.",
    139: "11:45 a.m. to 11:49 a.m.",
    140: "11:50 a.m. to 11:54 a.m.",
    141: "11:55 a.m. to 11:59 a.m.",
    142: "12:00 p.m. to 12:04 p.m.",
    143: "12:05 p.m. to 12:09 p.m.",
    144: "12:10 p.m. to 12:14 p.m.",
    145: "12:15 p.m. to 12:19 p.m.",
    146: "12:20 p.m. to 12:24 p.m.",
    147: "12:25 p.m. to 12:29 p.m.",
    148: "12:30 p.m. to 12:34 p.m.",
    149: "12:35 p.m. to 12:39 p.m.",
    150: "12:40 p.m. to 12:44 p.m.",
    151: "12:45 p.m. to 12:49 p.m.",
    152: "12:50 p.m. to 12:54 p.m.",
    153: "12:55 p.m. to 12:59 p.m.",
    154: "1:00 p.m. to 1:04 p.m.",
    155: "1:05 p.m. to 1:09 p.m.",
    156: "1:10 p.m. to 1:14 p.m.",
    157: "1:15 p.m. to 1:19 p.m.",
    158: "1:20 p.m. to 1:24 p.m.",
    159: "1:25 p.m. to 1:29 p.m.",
    160: "1:30 p.m. to 1:34 p.m.",
    161: "1:35 p.m. to 1:39 p.m.",
    162: "1:40 p.m. to 1:44 p.m.",
    163: "1:45 p.m. to 1:49 p.m.",
    164: "1:50 p.m. to 1:54 p.m.",
    165: "1:55 p.m. to 1:59 p.m.",
    166: "2:00 p.m. to 2:04 p.m.",
    167: "2:05 p.m. to 2:09 p.m.",
    168: "2:10 p.m. to 2:14 p.m.",
    169: "2:15 p.m. to 2:19 p.m.",
    170: "2:20 p.m. to 2:24 p.m.",
    171: "2:25 p.m. to 2:29 p.m.",
    172: "2:30 p.m. to 2:34 p.m.",
    173: "2:35 p.m. to 2:39 p.m.",
    174: "2:40 p.m. to 2:44 p.m.",
    175: "2:45 p.m. to 2:49 p.m.",
    176: "2:50 p.m. to 2:54 p.m.",
    177: "2:55 p.m. to 2:59 p.m.",
    178: "3:00 p.m. to 3:04 p.m.",
    179: "3:05 p.m. to 3:09 p.m.",
    180: "3:10 p.m. to 3:14 p.m.",
    181: "3:15 p.m. to 3:19 p.m.",
    182: "3:20 p.m. to 3:24 p.m.",
    183: "3:25 p.m. to 3:29 p.m.",
    184: "3:30 p.m. to 3:34 p.m.",
    185: "3:35 p.m. to 3:39 p.m.",
    186: "3:40 p.m. to 3:44 p.m.",
    187: "3:45 p.m. to 3:49 p.m.",
    188: "3:50 p.m. to 3:54 p.m.",
    189: "3:55 p.m. to 3:59 p.m.",
    190: "4:00 p.m. to 4:04 p.m.",
    191: "4:05 p.m. to 4:09 p.m.",
    192: "4:10 p.m. to 4:14 p.m.",
    193: "4:15 p.m. to 4:19 p.m.",
    194: "4:20 p.m. to 4:24 p.m.",
    195: "4:25 p.m. to 4:29 p.m.",
    196: "4:30 p.m. to 4:34 p.m.",
    197: "4:35 p.m. to 4:39 p.m.",
    198: "4:40 p.m. to 4:44 p.m.",
    199: "4:45 p.m. to 4:49 p.m.",
    200: "4:50 p.m. to 4:54 p.m.",
    201: "4:55 p.m. to 4:59 p.m.",
    202: "5:00 p.m. to 5:04 p.m.",
    203: "5:05 p.m. to 5:09 p.m.",
    204: "5:10 p.m. to 5:14 p.m.",
    205: "5:15 p.m. to 5:19 p.m.",
    206: "5:20 p.m. to 5:24 p.m.",
    207: "5:25 p.m. to 5:29 p.m.",
    208: "5:30 p.m. to 5:34 p.m.",
    209: "5:35 p.m. to 5:39 p.m.",
    210: "5:40 p.m. to 5:44 p.m.",
    211: "5:45 p.m. to 5:49 p.m.",
    212: "5:50 p.m. to 5:54 p.m.",
    213: "5:55 p.m. to 5:59 p.m.",
    214: "6:00 p.m. to 6:04 p.m.",
    215: "6:05 p.m. to 6:09 p.m.",
    216: "6:10 p.m. to 6:14 p.m.",
    217: "6:15 p.m. to 6:19 p.m.",
    218: "6:20 p.m. to 6:24 p.m.",
    219: "6:25 p.m. to 6:29 p.m.",
    220: "6:30 p.m. to 6:34 p.m.",
    221: "6:35 p.m. to 6:39 p.m.",
    222: "6:40 p.m. to 6:44 p.m.",
    223: "6:45 p.m. to 6:49 p.m.",
    224: "6:50 p.m. to 6:54 p.m.",
    225: "6:55 p.m. to 6:59 p.m.",
    226: "7:00 p.m. to 7:04 p.m.",
    227: "7:05 p.m. to 7:09 p.m.",
    228: "7:10 p.m. to 7:14 p.m.",
    229: "7:15 p.m. to 7:19 p.m.",
    230: "7:20 p.m. to 7:24 p.m.",
    231: "7:25 p.m. to 7:29 p.m.",
    232: "7:30 p.m. to 7:34 p.m.",
    233: "7:35 p.m. to 7:39 p.m.",
    234: "7:40 p.m. to 7:44 p.m.",
    235: "7:45 p.m. to 7:49 p.m.",
    236: "7:50 p.m. to 7:54 p.m.",
    237: "7:55 p.m. to 7:59 p.m.",
    238: "8:00 p.m. to 8:04 p.m.",
    239: "8:05 p.m. to 8:09 p.m.",
    240: "8:10 p.m. to 8:14 p.m.",
    241: "8:15 p.m. to 8:19 p.m.",
    242: "8:20 p.m. to 8:24 p.m.",
    243: "8:25 p.m. to 8:29 p.m.",
    244: "8:30 p.m. to 8:34 p.m.",
    245: "8:35 p.m. to 8:39 p.m.",
    246: "8:40 p.m. to 8:44 p.m.",
    247: "8:45 p.m. to 8:49 p.m.",
    248: "8:50 p.m. to 8:54 p.m.",
    249: "8:55 p.m. to 8:59 p.m.",
    250: "9:00 p.m. to 9:04 p.m.",
    251: "9:05 p.m. to 9:09 p.m.",
    252: "9:10 p.m. to 9:14 p.m.",
    253: "9:15 p.m. to 9:19 p.m.",
    254: "9:20 p.m. to 9:24 p.m.",
    255: "9:25 p.m. to 9:29 p.m.",
    256: "9:30 p.m. to 9:34 p.m.",
    257: "9:35 p.m. to 9:39 p.m.",
    258: "9:40 p.m. to 9:44 p.m.",
    259: "9:45 p.m. to 9:49 p.m.",
    260: "9:50 p.m. to 9:54 p.m.",
    261: "9:55 p.m. to 9:59 p.m.",
    262: "10:00 p.m. to 10:04 p.m.",
    263: "10:05 p.m. to 10:09 p.m.",
    264: "10:10 p.m. to 10:14 p.m.",
    265: "10:15 p.m. to 10:19 p.m.",
    266: "10:20 p.m. to 10:24 p.m.",
    267: "10:25 p.m. to 10:29 p.m.",
    268: "10:30 p.m. to 10:34 p.m.",
    269: "10:35 p.m. to 10:39 p.m.",
    270: "10:40 p.m. to 10:44 p.m.",
    271: "10:45 p.m. to 10:49 p.m.",
    272: "10:50 p.m. to 10:55 p.m.",
    273: "10:55 p.m. to 10:59 p.m.",
    274: "11:00 p.m. to 11:04 p.m.",
    275: "11:05 p.m. to 11:09 p.m.",
    276: "11:10 p.m. to 11:14 p.m.",
    277: "11:15 p.m. to 11:19 p.m.",
    278: "11:20 p.m. to 11:24 p.m.",
    279: "11:25 p.m. to 11:29 p.m.",
    280: "11:30 p.m. to 11:34 p.m.",
    281: "11:35 p.m. to 11:39 p.m.",
    282: "11:40 p.m. to 11:44 p.m.",
    283: "11:45 p.m. to 11:49 p.m.",
    284: "11:50 p.m. to 11:54 p.m.",
    285: "11:55 p.m. to 11:59 p.m."
}

departure_hours_mappping = {
    'bb': "N/A (not a worker; worker who worked at home)",
    1: "12:00 a.m. to 12:29 a.m.",
    2: "12:30 a.m. to 12:59 a.m.",
    3: "1:00 a.m. to 1:29 a.m.",
    4: "1:30 a.m. to 1:59 a.m.",
    5: "2:00 a.m. to 2:29 a.m.",
    6: "2:30 a.m. to 2:59 a.m.",
    7: "3:00 a.m. to 3:09 a.m.",
    8: "3:10 a.m. to 3:19 a.m.",
    9: "3:20 a.m. to 3:29 a.m.",
    10: "3:30 a.m. to 3:39 a.m.",
    11: "3:40 a.m. to 3:49 a.m.",
    12: "3:50 a.m. to 3:59 a.m.",
    13: "4:00 a.m. to 4:09 a.m.",
    14: "4:10 a.m. to 4:19 a.m.",
    15: "4:20 a.m. to 4:29 a.m.",
    16: "4:30 a.m. to 4:39 a.m.",
    17: "4:40 a.m. to 4:49 a.m.",
    18: "4:50 a.m. to 4:59 a.m.",
    19: "5:00 a.m. to 5:04 a.m.",
    20: "5:05 a.m. to 5:09 a.m.",
    21: "5:10 a.m. to 5:14 a.m.",
    22: "5:15 a.m. to 5:19 a.m.",
    23: "5:20 a.m. to 5:24 a.m.",
    24: "5:25 a.m. to 5:29 a.m.",
    25: "5:30 a.m. to 5:34 a.m.",
    26: "5:35 a.m. to 5:39 a.m.",
    27: "5:40 a.m. to 5:44 a.m.",
    28: "5:45 a.m. to 5:49 a.m.",
    29: "5:50 a.m. to 5:54 a.m.",
    30: "5:55 a.m. to 5:59 a.m.",
    31: "6:00 a.m. to 6:04 a.m.",
    32: "6:05 a.m. to 6:09 a.m.",
    33: "6:10 a.m. to 6:14 a.m.",
    34: "6:15 a.m. to 6:19 a.m.",
    35: "6:20 a.m. to 6:24 a.m.",
    36: "6:25 a.m. to 6:29 a.m.",
    37: "6:30 a.m. to 6:34 a.m.",
    38: "6:35 a.m. to 6:39 a.m.",
    39: "6:40 a.m. to 6:44 a.m.",
    40: "6:45 a.m. to 6:49 a.m.",
    41: "6:50 a.m. to 6:54 a.m.",
    42: "6:55 a.m. to 6:59 a.m.",
    43: "7:00 a.m. to 7:04 a.m.",
    44: "7:05 a.m. to 7:09 a.m.",
    45: "7:10 a.m. to 7:14 a.m.",
    46: "7:15 a.m. to 7:19 a.m.",
    47: "7:20 a.m. to 7:24 a.m.",
    48: "7:25 a.m. to 7:29 a.m.",
    49: "7:30 a.m. to 7:34 a.m.",
    50: "7:35 a.m. to 7:39 a.m.",
    51: "7:40 a.m. to 7:44 a.m.",
    52: "7:45 a.m. to 7:49 a.m.",
    53: "7:50 a.m. to 7:54 a.m.",
    54: "7:55 a.m. to 7:59 a.m.",
    55: "8:00 a.m. to 8:04 a.m.",
    56: "8:05 a.m. to 8:09 a.m.",
    57: "8:10 a.m. to 8:14 a.m.",
    58: "8:15 a.m. to 8:19 a.m.",
    59: "8:20 a.m. to 8:24 a.m.",
    60: "8:25 a.m. to 8:29 a.m.",
    61: "8:30 a.m. to 8:34 a.m.",
    62: "8:35 a.m. to 8:39 a.m.",
    63: "8:40 a.m. to 8:44 a.m.",
    64: "8:45 a.m. to 8:49 a.m.",
    65: "8:50 a.m. to 8:54 a.m.",
    66: "8:55 a.m. to 8:59 a.m.",
    67: "9:00 a.m. to 9:04 a.m.",
    68: "9:05 a.m. to 9:09 a.m.",
    69: "9:10 a.m. to 9:14 a.m.",
    70: "9:15 a.m. to 9:19 a.m.",
    71: "9:20 a.m. to 9:24 a.m.",
    72: "9:25 a.m. to 9:29 a.m.",
    73: "9:30 a.m. to 9:34 a.m.",
    74: "9:35 a.m. to 9:39 a.m.",
    75: "9:40 a.m. to 9:44 a.m.",
    76: "9:45 a.m. to 9:49 a.m.",
    77: "9:50 a.m. to 9:54 a.m.",
    78: "9:55 a.m. to 9:59 a.m.",
    79: "10:00 a.m. to 10:09 a.m.",
    80: "10:10 a.m. to 10:19 a.m.",
    81: "10:20 a.m. to 10:29 a.m.",
    82: "10:30 a.m. to 10:39 a.m.",
    83: "10:40 a.m. to 10:49 a.m.",
    84: "10:50 a.m. to 10:59 a.m.",
    85: "11:00 a.m. to 11:09 a.m.",
    86: "11:10 a.m. to 11:19 a.m.",
    87: "11:20 a.m. to 11:29 a.m.",
    88: "11:30 a.m. to 11:39 a.m.",
    89: "11:40 a.m. to 11:49 a.m.",
    90: "11:50 a.m. to 11:59 a.m.",
    91: "12:00 p.m. to 12:09 p.m.",
    92: "12:10 p.m. to 12:19 p.m.",
    93: "12:20 p.m. to 12:29 p.m.",
    94: "12:30 p.m. to 12:39 p.m.",
    95: "12:40 p.m. to 12:49 p.m.",
    96: "12:50 p.m. to 12:59 p.m.",
    97: "1:00 p.m. to 1:09 p.m.",
    98: "1:10 p.m. to 1:19 p.m.",
    99: "1:20 p.m. to 1:29 p.m.",
    100: "1:30 p.m. to 1:39 p.m.",
    101: "1:40 p.m. to 1:49 p.m.",
    102: "1:50 p.m. to 1:59 p.m.",
    103: "2:00 p.m. to 2:09 p.m.",
    104: "2:10 p.m. to 2:19 p.m.",
    105: "2:20 p.m. to 2:29 p.m.",
    106: "2:30 p.m. to 2:39 p.m.",
    107: "2:40 p.m. to 2:49 p.m.",
    108: "2:50 p.m. to 2:59 p.m.",
    109: "3:00 p.m. to 3:09 p.m.",
    110: "3:10 p.m. to 3:19 p.m.",
    111: "3:20 p.m. to 3:29 p.m.",
    112: "3:30 p.m. to 3:39 p.m.",
    113: "3:40 p.m. to 3:49 p.m.",
    114: "3:50 p.m. to 3:59 p.m.",
    115: "4:00 p.m. to 4:09 p.m.",
    116: "4:10 p.m. to 4:19 p.m.",
    117: "4:20 p.m. to 4:29 p.m.",
    118: "4:30 p.m. to 4:39 p.m.",
    119: "4:40 p.m. to 4:49 p.m.",
    120: "4:50 p.m. to 4:59 p.m.",
    121: "5:00 p.m. to 5:09 p.m.",
    122: "5:10 p.m. to 5:19 p.m.",
    123: "5:20 p.m. to 5:29 p.m.",
    124: "5:30 p.m. to 5:39 p.m.",
    125: "5:40 p.m. to 5:49 p.m.",
    126: "5:50 p.m. to 5:59 p.m.",
    127: "6:00 p.m. to 6:09 p.m.",
    128: "6:10 p.m. to 6:19 p.m.",
    129: "6:20 p.m. to 6:29 p.m.",
    130: "6:30 p.m. to 6:39 p.m.",
    131: "6:40 p.m. to 6:49 p.m.",
    132: "6:50 p.m. to 6:59 p.m.",
    133: "7:00 p.m. to 7:29 p.m.",
    134: "7:30 p.m. to 7:59 p.m.",
    135: "8:00 p.m. to 8:29 p.m.",
    136: "8:30 p.m. to 8:59 p.m.",
    137: "9:00 p.m. to 9:09 p.m.",
    138: "9:10 p.m. to 9:19 p.m.",
    139: "9:20 p.m. to 9:29 p.m.",
    140: "9:30 p.m. to 9:39 p.m.",
    141: "9:40 p.m. to 9:49 p.m.",
    142: "9:50 p.m. to 9:59 p.m.",
    143: "10:00 p.m. to 10:09 p.m.",
    144: "10:10 p.m. to 10:19 p.m.",
    145: "10:20 p.m. to 10:29 p.m.",
    146: "10:30 p.m. to 10:39 p.m.",
    147: "10:40 p.m. to 10:49 p.m.",
    148: "10:50 p.m. to 10:59 p.m.",
    149: "11:00 p.m. to 11:29 p.m.",
    150: "11:30 p.m. to 11:59 p.m."
}


ethnicity_mapping = {
  10: "Comanche alone",
  11: "Creek alone",
  12: "Crow alone",
  13: "Hopi alone",
  14: "Iroquois alone",
  15: "Lumbee alone",
  16: "Mexican American Indian alone",
  17: "Navajo alone",
  18: "Pima alone",
  19: "Potawatomi alone",
  20: "Pueblo alone",
  21: "Puget Sound Salish alone",
  22: "Seminole alone",
  23: "Sioux alone",
  24: "South American Indian alone",
  25: "Tohono O'Odham alone",
  26: "Yaqui alone",
  27: "Other specified American Indian tribes alone",
  28: "All other specified American Indian tribe combinations",
  29: "American Indian, tribe not specified",
  30: "Alaskan Athabascan alone",
  31: "Tlingit-Haida alone",
  32: "Inupiat alone",
  33: "Yup’ik alone",
  34: "Aleut alone",
  35: "Other Alaska Native",
  36: "Other American Indian and Alaska Native specified",
  37: "American Indian and Alaska Native, not specified",
  38: "Asian Indian alone",
  39: "Bangladeshi alone",
  40: "Bhutanese alone",
  41: "Burmese alone",
  42: "Cambodian alone",
  43: "Chinese, except Taiwanese, alone",
  44: "Taiwanese alone",
  45: "Filipino alone",
  46: "Hmong alone",
  47: "Indonesian alone",
  48: "Japanese alone",
  49: "Korean alone",
  50: "Laotian alone",
  51: "Malaysian alone",
  52: "Mongolian alone",
  53: "Nepalese alone",
  54: "Pakistani alone",
  55: "Sri Lankan alone",
  56: "Thai alone",
  57: "Vietnamese alone",
  58: "Other Asian alone",
  59: "All combinations of Asian races only",
  60: "Native Hawaiian alone",
  61: "Samoan alone",
  62: "Tongan alone",
  63: "Guamanian or Chamorro alone",
  64: "Marshallese alone",
  65: "Fijian alone",
  66: "Other Native Hawaiian and Other Pacific Islander",
  67: "Some Other Race alone",
  68: "Two or More Races",
  1: "White alone",
  2: "Black or African American alone",
  3: "Apache alone",
  4: "Blackfeet alone",
  5: "Cherokee alone",
  6: "Cheyenne alone",
  7: "Chickasaw alone",
  8: "Chippewa alone",
  9: "Choctaw alone"
}

degree_field_mapping = {
  1100: "GENERAL AGRICULTURE",
  1101: "AGRICULTURE PRODUCTION AND MANAGEMENT",
  1102: "AGRICULTURAL ECONOMICS",
  1103: "ANIMAL SCIENCES",
  1104: "FOOD SCIENCE",
  1105: "PLANT SCIENCE AND AGRONOMY",
  1106: "SOIL SCIENCE",
  1199: "MISCELLANEOUS AGRICULTURE",
  1301: "ENVIRONMENTAL SCIENCE",
  1302: "FORESTRY",
  1303: "NATURAL RESOURCES MANAGEMENT",
  1401: "ARCHITECTURE",
  1501: "AREA ETHNIC AND CIVILIZATION STUDIES",
  1901: "COMMUNICATIONS",
  1902: "JOURNALISM",
  1903: "MASS MEDIA",
  1904: "ADVERTISING AND PUBLIC RELATIONS",
  2001: "COMMUNICATION TECHNOLOGIES",
  2100: "COMPUTER AND INFORMATION SYSTEMS",
  2101: "COMPUTER PROGRAMMING AND DATA PROCESSING",
  2102: "COMPUTER SCIENCE",
  2105: "INFORMATION SCIENCES",
  2106: "COMPUTER ADMINISTRATION MANAGEMENT AND SECURITY",
  2107: "COMPUTER NETWORKING AND TELECOMMUNICATIONS",
  2201: "COSMETOLOGY SERVICES AND CULINARY ARTS",
  2300: "GENERAL EDUCATION",
  2301: "EDUCATIONAL ADMINISTRATION AND SUPERVISION",
  2303: "SCHOOL STUDENT COUNSELING",
  2304: "ELEMENTARY EDUCATION",
  2305: "MATHEMATICS TEACHER EDUCATION",
  2306: "PHYSICAL AND HEALTH EDUCATION TEACHING",
  2307: "EARLY CHILDHOOD EDUCATION",
  2308: "SCIENCE AND COMPUTER TEACHER EDUCATION",
  2309: "SECONDARY TEACHER EDUCATION",
  2310: "SPECIAL NEEDS EDUCATION",
  2311: "SOCIAL SCIENCE OR HISTORY TEACHER EDUCATION",
  2312: "TEACHER EDUCATION: MULTIPLE LEVELS",
  2313: "LANGUAGE AND DRAMA EDUCATION",
  2314: "ART AND MUSIC EDUCATION",
  2399: "MISCELLANEOUS EDUCATION",
  2400: "GENERAL ENGINEERING",
  2401: "AEROSPACE ENGINEERING",
  2402: "BIOLOGICAL ENGINEERING",
  2403: "ARCHITECTURAL ENGINEERING",
  2404: "BIOMEDICAL ENGINEERING",
  2405: "CHEMICAL ENGINEERING",
  2406: "CIVIL ENGINEERING",
  2407: "COMPUTER ENGINEERING",
  2408: "ELECTRICAL ENGINEERING",
  2409: "ENGINEERING MECHANICS PHYSICS AND SCIENCE",
  2410: "ENVIRONMENTAL ENGINEERING",
  2411: "GEOLOGICAL AND GEOPHYSICAL ENGINEERING",
  2412: "INDUSTRIAL AND MANUFACTURING ENGINEERING",
  2413: "MATERIALS ENGINEERING AND MATERIALS SCIENCE",
  2414: "MECHANICAL ENGINEERING",
  2415: "METALLURGICAL ENGINEERING",
  2416: "MINING AND MINERAL ENGINEERING",
  2417: "NAVAL ARCHITECTURE AND MARINE ENGINEERING",
  2418: "NUCLEAR ENGINEERING",
  2419: "PETROLEUM ENGINEERING",
  2499: "MISCELLANEOUS ENGINEERING",
  2500: "ENGINEERING TECHNOLOGIES",
  2501: "ENGINEERING AND INDUSTRIAL MANAGEMENT",
  2502: "ELECTRICAL ENGINEERING TECHNOLOGY",
  2503: "INDUSTRIAL PRODUCTION TECHNOLOGIES",
  2504: "MECHANICAL ENGINEERING RELATED TECHNOLOGIES",
  2599: "MISCELLANEOUS ENGINEERING TECHNOLOGIES",
  2601: "LINGUISTICS AND COMPARATIVE LANGUAGE AND LITERATURE",
  2602: "FRENCH GERMAN LATIN AND OTHER COMMON FOREIGN LANGUAGE STUDIES",
  2603: "OTHER FOREIGN LANGUAGES",
  2901: "FAMILY AND CONSUMER SCIENCES",
  3201: "COURT REPORTING",
  3202: "PRE-LAW AND LEGAL STUDIES",
  3301: "ENGLISH LANGUAGE AND LITERATURE",
  3302: "COMPOSITION AND RHETORIC",
  3401: "LIBERAL ARTS",
  3402: "HUMANITIES",
  3501: "LIBRARY SCIENCE",
  3600: "BIOLOGY",
  3601: "BIOCHEMICAL SCIENCES",
  3602: "BOTANY",
  3603: "MOLECULAR BIOLOGY",
  3604: "ECOLOGY",
  3605: "GENETICS",
  3606: "MICROBIOLOGY",
  3607: "PHARMACOLOGY",
  3608: "PHYSIOLOGY",
  3609: "ZOOLOGY",
  3611: "NEUROSCIENCE",
  3699: "MISCELLANEOUS BIOLOGY",
  3700: "MATHEMATICS",
  3701: "APPLIED MATHEMATICS",
  3702: "STATISTICS AND DECISION SCIENCE",
  3801: "MILITARY TECHNOLOGIES",
  4000: "MULTI/INTERDISCIPLINARY STUDIES",
  4001: "INTERCULTURAL AND INTERNATIONAL STUDIES",
  4002: "NUTRITION SCIENCES",
  4005: "MATHEMATICS AND COMPUTER SCIENCE",
  4006: "COGNITIVE SCIENCE AND BIOPSYCHOLOGY",
  4007: "INTERDISCIPLINARY SOCIAL SCIENCES",
  4101: "PHYSICAL FITNESS PARKS RECREATION AND LEISURE",
  4801: "PHILOSOPHY AND RELIGIOUS STUDIES",
  4901: "THEOLOGY AND RELIGIOUS VOCATIONS",
  5000: "PHYSICAL SCIENCES",
  5001: "ASTRONOMY AND ASTROPHYSICS",
  5002: "ATMOSPHERIC SCIENCES AND METEOROLOGY",
  5003: "CHEMISTRY",
  5004: "GEOLOGY AND EARTH SCIENCE",
  5005: "GEOSCIENCES",
  5006: "OCEANOGRAPHY",
  5007: "PHYSICS",
  5008: "MATERIALS SCIENCE",
  5098: "MULTI-DISCIPLINARY OR GENERAL SCIENCE",
  5102: "NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES",
  5200: "PSYCHOLOGY",
  5201: "EDUCATIONAL PSYCHOLOGY",
  5202: "CLINICAL PSYCHOLOGY",
  5203: "COUNSELING PSYCHOLOGY",
  5205: "INDUSTRIAL AND ORGANIZATIONAL PSYCHOLOGY",
  5206: "SOCIAL PSYCHOLOGY",
  5299: "MISCELLANEOUS PSYCHOLOGY",
  5301: "CRIMINAL JUSTICE AND FIRE PROTECTION",
  5401: "PUBLIC ADMINISTRATION",
  5402: "PUBLIC POLICY",
  5403: "HUMAN SERVICES AND COMMUNITY ORGANIZATION",
  5404: "SOCIAL WORK",
  5500: "GENERAL SOCIAL SCIENCES",
  5501: "ECONOMICS",
  5502: "ANTHROPOLOGY AND ARCHEOLOGY",
  5503: "CRIMINOLOGY",
  5504: "GEOGRAPHY",
  5505: "INTERNATIONAL RELATIONS",
  5506: "POLITICAL SCIENCE AND GOVERNMENT",
  5507: "SOCIOLOGY",
  5599: "MISCELLANEOUS SOCIAL SCIENCES",
  5601: "CONSTRUCTION SERVICES",
  5701: "ELECTRICAL, MECHANICAL, AND PRECISION TECHNOLOGIES AND PRODUCTION",
  5901: "TRANSPORTATION SCIENCES AND TECHNOLOGIES",
  6000: "FINE ARTS",
  6001: "DRAMA AND THEATER ARTS",
  6002: "MUSIC",
  6003: "VISUAL AND PERFORMING ARTS",
  6004: "COMMERCIAL ART AND GRAPHIC DESIGN",
  6005: "FILM VIDEO AND PHOTOGRAPHIC ARTS",
  6006: "ART HISTORY AND CRITICISM",
  6007: "STUDIO ARTS",
  6099: "MISCELLANEOUS FINE ARTS",
  6100: "GENERAL MEDICAL AND HEALTH SERVICES",
  6102: "COMMUNICATION DISORDERS SCIENCES AND SERVICES",
  6103: "HEALTH AND MEDICAL ADMINISTRATIVE SERVICES",
  6104: "MEDICAL ASSISTING SERVICES",
  6105: "MEDICAL TECHNOLOGIES TECHNICIANS",
  6106: "HEALTH AND MEDICAL PREPARATORY PROGRAMS",
  6107: "NURSING",
  6108: "PHARMACY PHARMACEUTICAL SCIENCES AND ADMINISTRATION",
  6109: "TREATMENT THERAPY PROFESSIONS",
  6110: "COMMUNITY AND PUBLIC HEALTH",
  6199: "MISCELLANEOUS HEALTH MEDICAL PROFESSIONS",
  6200: "GENERAL BUSINESS",
  6201: "ACCOUNTING",
  6202: "ACTUARIAL SCIENCE",
  6203: "BUSINESS MANAGEMENT AND ADMINISTRATION",
  6204: "OPERATIONS LOGISTICS AND E-COMMERCE",
  6205: "BUSINESS ECONOMICS",
  6206: "MARKETING AND MARKETING RESEARCH",
  6207: "FINANCE",
  6209: "HUMAN RESOURCES AND PERSONNEL MANAGEMENT",
  6210: "INTERNATIONAL BUSINESS",
  6211: "HOSPITALITY MANAGEMENT",
  6212: "MANAGEMENT INFORMATION SYSTEMS AND STATISTICS",
  6299: "MISCELLANEOUS BUSINESS & MEDICAL ADMINISTRATION",
  6402: "HISTORY",
  6403: "UNITED STATES HISTORY",
  'bbbb': "N/A (less than bachelor's degree)"
}


