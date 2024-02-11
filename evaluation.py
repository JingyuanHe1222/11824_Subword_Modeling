import numpy as np
import os

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
  
  
split = 'shp'

# # the fine-tuned
# pred = []
# with open(f"outputs/byt5/pred_{split}.dev.tgt", 'r') as f:
#     for line in f:
#         by_pred.append(line)

# the combined
pred = []
with open(f"pred_{split}.dev.tgt", 'r') as f:
    for line in f:
        by_pred.append(line)

# # the rule-base
# pred = []
# with open(f"pred_{split}_rule.dev.tgt", 'r') as f:
#     for line in f:
#         pred.append(line)

# # the baseline
# pred = []
# with open(f"outputs/baseline/morfessor_{split}.dev.tgt", 'r') as f:
#     for line in f:
#         pred.append(line)

truth = []
with open(f'miniproj1-dataset/{split}.dev.tgt', 'r') as f:
    for line in f:
        truth.append(line.strip())


print("rule based: \n", evaluate(truth, pred))
# print("by_t5: \n", evaluate(truth, pred))

## tar
# rule based:
#  {'f1': 0.52046783625731, 'precision': 0.577922077922078, 'recall': 0.4734042553191489}
# by_t5:
#  {'f1': 0.7796610169491526, 'precision': 0.8313253012048193, 'recall': 0.7340425531914894}


## shp
# rule based:
#  {'f1': 0.52046783625731, 'precision': 0.577922077922078, 'recall': 0.4734042553191489}
# by_t5:
#  {'f1': 0.7796610169491526, 'precision': 0.8313253012048193, 'recall': 0.7340425531914894}