def RLE_Decompression(compression: list):
    res = ""
    for tup in compression:
        if tup == "\n":
            res += tup 
            continue
        c, occ = tup[0], tup[1]
        res += c*occ
    return res
