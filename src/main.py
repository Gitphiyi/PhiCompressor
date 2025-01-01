import TextCompressors as TC
import TextDecoders as TD

file = open("texts/small.txt", "r")

st = TC.parse_file(file)
#ans = TextCompressors.RLE_Compression(st)
#print(TextDecoders.RLE_Decompression(ans))
ans = TC.Huffman_Compression(st)
