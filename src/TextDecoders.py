def RLE_Decompression(compression: list):
    res = ""
    for tup in compression:
        if tup == "\n":
            res += tup 
            continue
        c, occ = tup[0], tup[1]
        res += c*occ
    return res

def Huffman_Decompression(file):
    data = file.read()
    bit_string = ''.join(format(byte, '08b') for byte in data)
    for i in range(0, len(bit_string), 8):
        print(bit_string[i:i+8])