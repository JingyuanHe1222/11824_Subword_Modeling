import unimorph_inflect
unimorph_inflect.download('swc')   # This downloads the English models, if you don't have them already

from unimorph_inflect import inflect

import os
from tqdm import tqdm

lang='swc'
file_name = f'dataset/{lang}.test.tsv'
output = []
with open(file_name, 'r', encoding="utf-8") as f:
    for line in tqdm(f):
        tok, tag = line.split('\t')
        output.append(inflect(tok, tag, language=lang))
        # break

# print(output)
output_name = f'dataset/{lang}.txt'
with open(output_name, 'w', encoding='utf-8') as f:
    for o in output:
        f.write(o[0] + '\n')
      