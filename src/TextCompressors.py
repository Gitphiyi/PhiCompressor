from Node import Node
import heapq
import os

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

def Huffman_Compression(text: str, file_name: str):
    """ 
        Writes string into a binary file. The first byte of the binary file is how many bits are actually valid.
    """
    n = len(text)
    assert n >= 2, "File is too small to use huffman encoding"
    freq = {}
    # First pass to determine character frequency
    for c in text:
        if c not in freq.keys():
            freq[c] = 1
        else:
            freq[c] += 1
    heap = [Node(let=c, val=v) for c,v in freq.items() ]
    heapq.heapify(heap)
    
    #Build Binary Tree from heap
    l = heapq.heappop(heap)
    r = heapq.heappop(heap)
    root = None
    while len(heap) > 0:
        root = Node(let=l.let+r.let, val=l.val+r.val, l=l, r=r)
        heapq.heappush(heap, root)
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
    root = Node(let=l.let+r.let, val=l.val+r.val, l=l, r=r) #probably doesn't need if statement since guaranteed to have l and r populated

    #Build binary code mapping for each letter
    bin_map = {}
    def build_map(root, bin_code: str):
        if root == None:
            return 
        if len(root.let) == 1:
            bin_map[root.let] = bin_code 
        build_map(root.l, bin_code+"0")
        build_map(root.r, bin_code+"1")
    build_map(root, "")
    print(bin_map)
    
    #encode the file into a binary file
    file_path = os.path.join("texts/", f"{file_name}.bin")
    bin_str = ""
    for c in text:
        bin_str += bin_map[c]
    temp = len(bin_str) // 8
    num_bits = (temp+1) * 8 - len(bin_str)  # denote which bytes are useless at the end of a byte [0,8)
    bin_str += num_bits * "0" #pad it with 0's so the string can be put into bytes

    len_bits = num_bits.to_bytes(1, 'big', signed=False)
    content = bytearray()
    for i in range(0, len(bin_str), 8):
        content.append(int(bin_str[i:i+8], 2))
    with open(file_path, 'wb') as f:
        f.write(len_bits)
        f.write(content)