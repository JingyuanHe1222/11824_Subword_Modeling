import os


file_name = 'outputs/orig.test.output'
preds = []
with open(file_name, 'r', encoding="utf-8") as f:
    for line in f:
        tokens = line.split('\t')
        preds.append(tokens[1])

new_name = file_name.split('.')[0]
with open(f'kbd.txt', 'w', encoding='utf-8') as f:
    for pred in preds:
        f.write(pred + "\n")
        