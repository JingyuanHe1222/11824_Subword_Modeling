

#!/bin/bash


python inflection.py --datapath custom_data \
    --L1 adyghe \
    --L2 kabardian \
    --mode test \
    --setting original \
    --outputpath outputs/ \
    --use_att_reg \
    --use_tag_att_reg