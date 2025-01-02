import TextCompressors as TC
import TextDecoders as TD

file_name= "text"
file = open(f"texts/{file_name}.txt", "r")


st = TC.parse_file(file)
#ans = TextCompressors.RLE_Compression(st)
#print(TextDecoders.RLE_Decompression(ans))
TC.Huffman_Compression(st, file_name)

bin_file = open(f"texts/{file_name}.bin", "rb")
TD.Huffman_Decompression(bin_file)
