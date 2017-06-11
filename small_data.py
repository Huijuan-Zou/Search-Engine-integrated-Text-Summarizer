import helper
import os

data = helper.read_data_from_file('data.p')
d = helper.read_data_from_file('out.pickle')

f = open('headlines.txt', 'w+')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

cnt = 0
vocab = {}

for i in d['headline']:
    if is_ascii(i) == False:
        continue
    for w in i.split():
        if w not in vocab and w in data['word2idx'] and data['word2idx'][w] < data['vocab_size']:
            vocab[w] = data['embedding'][data['word2idx'][w]]
    f.write(i)
    f.write('\n')
    cnt += 1
    if cnt > 69100:
        break

helper.dump_data_to_file(vocab, 'vocab.p')
f.close()