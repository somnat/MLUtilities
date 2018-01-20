import numpy as np
from datetime import datetime

word_vecs = {}
csv_header = "word"
for x in range(1, 301):
    csv_header = csv_header + " V" + str(x)
csv_header = csv_header + "\n"
with open("vectors.bin", "rb") as source, open('vectors.csv', 'w') as dest:
    dest.write(csv_header)
    header = source.readline()

    vocab_size, layer1_size = map(int, header.split())
    binary_len = np.dtype('float32').itemsize * layer1_size
    for line in range(vocab_size):
        word = []
        if line%10000==0:
            print (datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ": " + str(line))        
        while True:
            ch = source.read(1)
            if ch == b' ':
                word = ''.join(word)  
                break
            if ch != '\n':
                """print(ch.decode('cp437'))"""
                word.append(ch.decode('cp437'))
        values = np.fromstring(source.read(binary_len), dtype='float32')
        dest.write(word + ' ' +  ' '.join(map(str, values))  + "\n")
