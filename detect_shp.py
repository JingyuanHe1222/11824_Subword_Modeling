import numpy 

def evaluate(gold, pred):

  tp = 0
  fp = 0
  fn = 0

  for g, p in zip(gold, pred):
    g_bag = g.strip().split(" ")
    p_bag = p.strip().split(" ")

    tp += sum([1 for i in p_bag if i in g_bag])
    fp += sum([1 for i in p_bag if not i in g_bag])
    fn += sum([1 for i in g_bag if not i in p_bag])

  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  if precision == 0 or recall == 0:
    f1 = 0
  else:
    f1 = 2 / ((1/precision) + (1/recall))

  return {
      "f1": f1,
      "precision": precision,
      "recall": recall,
  }



last_one = ['a', 'n', 'r', 'i']
last_two = ['ki', 'ai', 'ni', 'bo', 'ra', 'we']
last_three = ['nin']
skip_three = ['to']
last_four = ['ribi', 'yoma']

def transform(word):

    if len(word) <= 4:
        return word
    if word[:-4] in last_four:
        word = word[:-4] + ' ' + word[-4:]
    elif word[:-3] in last_three:
        if word[-5:-3] not in skip_three:
            word = word[:-3] + ' ' + word[-3:]
    elif word[-2:] in last_two:
        last = ' ' + word[-2:]
        word = word[:-2]
        if word[-2:] in last_two:
            sec_last = ' ' + word[-2:]
            word = word[:-2]
            word = word + sec_last
        word = word + last
    elif word[-1:] in last_one:
        word = word[:-1] + ' ' + word[-1:]
    return word
  
  
  
def itr_transform(word):

    if len(word) <= 4:
        return word
    # len(word) >= 5
    stack = []
    idx = len(word) - 1
    while idx >= 0:
        if word[-4:] in last_four:
            # print("loop 4") ##
            stack.append(' ' + word[-4:])
            word = word[:-4]
            idx -= 4
        elif word[-3:] in last_three and word[-4] not in skip_three:
            # print("loop 3") ##
            stack.append(' ' + word[-3:])
            word = word[:-3] 
            idx -= 3
        elif word[-2:] in last_two:
            # print("loop 2") ##
            stack.append(' ' + word[-2:])
            word = word[:-2]
            idx -= 2
        elif word[-1:] in last_one:
            # print("loop 1") ##
            stack.append(' ' + word[-1])
            word = word[:-1]
            idx -= 1
        else:
            stack.append(word[-4:])
            word = word[:-4]
            idx -= 4 
        
    result = ""
    while len(stack) > 0:
        result += stack.pop()
    return result.strip()
  
  
  
split = 'shp'

words = []
with open(f'miniproj1-dataset/{split}.dev.src', 'r', encoding='utf-8') as f:
    for line in f:
        words.append(line.strip())

for i in range(len(words)):
    words[i] = itr_transform(words[i])
    

# with open("pred_{split}_rule.dev.tgt", 'w', encoding='utf-8') as f:
#     for word in words:
#         f.write(word)
#         f.write('\n')


truth = []
with open(f'miniproj1-dataset/{split}.dev.tgt', 'r', encoding='utf-8') as f:
    for line in f:
        truth.append(line.strip())
        
print("ruled: \n", evaluate(truth, words))
