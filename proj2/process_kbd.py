import os


lang = 'kbd'

original = []
pred = []
tags = []
with open(f'{lang}_nonn.txt', 'r', encoding='utf-8') as f:
    for line in f:
        pred.append(line)
        
with open(f'dataset/{lang}.test.tsv', 'r', encoding='utf-8') as f:
    for line in f:
        tok, tag =  line.split(u'\t')
        original.append(tok)
        tags.append(tag)
        

# process by known mistakes
removed = ['к', 'х']
for i in range(len(pred)): 
    o = original[i]
    p = pred[i]
    if o[-2:] == 'уэ':
        # rule 1
        for r in removed:
            if r in o[-5:-2]:
                parts = p.split('уэ')
                # remove э
                pred[i] = parts[0] + 'y' + parts[1]
                
                print("p: ", p)
                print("new: ", str(parts[0] + 'y' + parts[1]))
                
    elif o[-2:] == 'ду':
        # rule 2
        if tags[i] == 'N;NOM;SG' and p[len(o)] == 'э': 
            
            pred[i] = p[:len(0)]+p[len(o)+1:] # get rid of extra 
            print("p: ", p)
            print("new*: ", pred[i])
    elif o[-2:] == 'дж': 
        # rule 3
        if p[len(o)] != 'э':
            print("p: ", p)
            print("new: ", p.insert(len(0), 'э'))
            pred[i] = p.insert(len(0), 'э')
            break
            
            
with open(f'{lang}.txt', 'w', encoding='utf-8') as f:
    for p in pred:
        f.write(p)
        
        
# diff -U 0 kbd.txt kbd_nonn.txt | grep -c ^@
