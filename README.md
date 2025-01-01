# PhiCompressor

## RLE Compression
A simple algorithm where you count the number (n) of consecutive characters (c) and represent it as a tuple (c,n)

## Huffman Encoding
Algorithm that takes all characters in a text file and maps it to a probability distribution for each character. Then take a second pass that constructs a binary search tree where the depth of the tree is the length of the encoding of each character. Then another pass is done on every character which concatenates all the encodings into a binary file. Decoding is simple as all the encodings are prefix free (No encoding is a prefix of another). Thus you can simply loop through the encoding and when you hit a string of binary digits that match an encoding you can decode it into a character. Huffman encoder creates the optimal 
https://www.youtube.com/watch?v=B3y0RsVCyrw 
