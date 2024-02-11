# Outline for Mini-Project 1

### File Structure

- detect_shp.py: rule-based tokenizer for shp
        - transform: last pattern segmentation
        - itr_transform: iterative segmentation on the whole word 

- detect_tar.py: rule-based tokenizer for tar
        - transform: last pattern segmentation
        - itr_transform: iterative segmentation on the whole word 

- Morphological_Segmentation.ipynb: baseline models provided by the course staff

- evaluation.py: evaluation codes adpated from Morphological_Segmentation.ipynb

- fine-tune.ipynb: fine-tuning codes for byt5 on top of rule-based transformation 

- fine-tune-byt5.ipynb: fine-tuning codes for byt5 

- ./outputs
    - the logs and outputs of each experiments