import Node

def parse_file(file):
    line = file.readline()
    st = line
    for line in file:
        st += line
    return st

def RLE_Compression(text: str):
    n = len(text)
    if n == 1:
        return {(text[0], 1)}
    res = []
    prev = text[0]
    cnt = 1
    
    for i in range(1,n):
        c = text[i]
        if c == '\n':
            res.append( (prev, cnt) ) if prev != None else None
            res.append( ("\n") )
            prev = None 
            cnt = 0
        else:
            if prev == None:
                prev = c
                cnt = 1
            elif prev == c:
                cnt += 1
            else: 
                res.append( (prev, cnt) )
                prev = c 
                cnt = 1
    #Don't need to check anything at the end of the file because all text files end with \n 
    return res

def Huffman_Compression(text: str):
    n = len(text)
    assert n != 0, "File is empty"
    freq = {}
    # First pass to determine character frequency
    for c in text:
        if c not in freq.keys():
            freq[c] = 1
        else:
            freq[c] += 1
    freq = list(freq.items())
    freq.sort(key = lambda x: x[1])
    
    #Build Binary Tree from list
    print(freq)
