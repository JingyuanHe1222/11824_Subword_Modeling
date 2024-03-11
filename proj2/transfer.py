import os


file_name = 'kbd.decode.test.tsv'
preds = []
first = True
with open(file_name, 'r', encoding="utf-8") as f:
    for line in f:
        if first:
            first = False
            continue
        
        tokens = line.split('\t')
        preds.append(tokens[0].replace(' ', ''))

new_name = file_name.split('.')[0]
with open(f'{new_name}.txt', 'w', encoding='utf-8') as f:
    for pred in preds:
        f.write(pred + "\n")
        