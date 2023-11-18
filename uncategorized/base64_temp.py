import base64
base64_table = {
    0:	'A',
    1:	'B',
    2:	'C',
    3:	'D',
    4:	'E',
    5:	'F',
    6:	'G',
    7:	'H',
    8:	'I',
    9:	'J',
    10:	'K',
    11:	'L',
    12:	'M',
    13:	'N',
    14:	'O',
    15:	'P',
    16:	'Q',
    17:	'R',
    18:	'S',
    19:	'T',
    20:	'U',
    21:	'V',
    22:	'W',
    23:	'X',
    24:	'Y',
    25:	'Z',
    26:	'a',
    27:	'b',
    28:	'c',
    29:	'd',
    30:	'e',
    31:	'f',
    32:	'g',
    33:	'h',
    34:	'i',
    35:	'j',
    36:	'k',
    37:	'l',
    38:	'm',
    39:	'n',
    40:	'o',
    41:	'p',
    42:	'q',
    43:	'r',
    44:	's',
    45:	't',
    46:	'u',
    47:	'v',
    48:	'w',
    49:	'x',
    50:	'y',
    51:	'z',
    52:	'0',
    53:	'1',
    54:	'2',
    55:	'3',
    56:	'4',
    57:	'5',
    58:	'6',
    59:	'7',
    60:	'8',
    61:	'9',
    62:	'+',
    63: '/'
}

def encode(str):
    binStr = ''
    for x in str:
        binary = format(ord(x),'b')
        rem = 8-len(binary)
        binary = rem * '0' + binary
        binStr += binary

    cache = {}
    rem = len(binStr) % 6
    binStr += (6-rem) * "0"
    b64str = ""

    for i in range(0,len(binStr)-6+1,6):
        currStr = binStr[i:i+6]
        if currStr in cache:
            b64str += base64_table[cache[currStr]]
        else:
            total = 0
            for j, c in enumerate(reversed(list(currStr))):
                if c == '1':
                    total += (2**j)

            cache[currStr] = total
            
            b64str += base64_table[total]

    return b64str + ((6-rem)//2) * '='

input = "Hello world"
print('  '+encode(input))
print(base64.b64encode(input.encode('ascii')))

"""
convert to binary string maintaining groups of 8

group by 6 (last group padded with 0's)

convert each 6 into a value using table above

add = if 00 was padded
add == if 0000 was padded

"""

