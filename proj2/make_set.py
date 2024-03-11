import os

lang='kbd'


data = []
with open(f'dataset/{lang}.test.tsv', 'r', encoding='utf-8') as f:
    for line in f:
        fooled = line.split('\t')
        fooled.insert(1, fooled[0])
        data.append('\t'.join(fooled))
        # break

with open(f'dataset/{lang}.test.fool.tsv', 'w', encoding='utf-8') as f:
    for d in data:
        f.write(d)