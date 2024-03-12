### Project 2


#### Workflow

- For this project, I don't have many novel ideas on building a new neural models. I tried derived some rules but they were not able to beat the very strong non-neural baseline. Therefore, I ended up reading papers and experiment with previous works in this task. 
- I first do hyper-parameter tuning on the neural model we have. As I realize that the loss is decreasing, I suspect that are potential for the tagtransformer model we are using as the neural baseline by improving the complexity of the model. I experimented with a HMM model, a larger dropout to improve generalization (as the test data are unseen), and larger number of transformer blocks. More layers actually lead to a higher accuracy for xty so I eneded up using this experimented model towards the submission for xty. For kbd and swc, the neural model did not work as well. 
- I read the paper "Pushing the Limits of Low-Resource Morphological Inflection", which proposed a two-step attention architecture and data hallucination as well as cross-lingual transfer to improve the performance of the model on low-resource languages. I experimented with the inflection model but failed to get the data hallucation part working due to corrupted libraries. Seemingly, the incorporation of adyghe as a cross-lingual transfer improve the dev accuracy of kabardian, but the improvement is not as high as in their paper. I think that's because we have a more difficult test set, with samples of unseen roots. Another thing that should be noted is that the combination of adyghe and armenian as source for cross-lingual transfer is reported to further improve the performance, but I got a slightly worse result compared to using adyghe along. I think that's probably because the distribution of morphological rules in kabardian could differ a lot in our dataset compared to theirs, making the model very sensitive to the high-resource language data. 
- I experimented with a trained Unimorph model, which had been trained on swc. The performance is high, possibly due to a considerable training data (while our dataset only has 2k lines for trianing) and I ended up using this towards the swc submission.  
- For kbd, I cannot get a validation accuracy abobve 0.8, which is bad compared to the non-neural baseline. I tried improving on the non-neural baseline by observing the mistakes made in the validation set. However, the rules are not always helpful. There are three rules I made in process_kbd.py: 1. the first rule could do harm to the correct predictions as it does not always apply; 2. the second rule and the third rule could help improve the validation set performance, but does not apply to any words in the test set as the test set does not contain such specific forms.

#### Structure
- /neural_transducer and /bash_files: baseline and modified neural models
- /unimorph_inflect and convert_inflect.py: unimorph model
- /outputs: all the sample outputs
- transfer*.py and make_set.py: utility files 
- run.sh: shell script for running the inflection models of cross-lingual transfer at [inflection](https://github.com/antonisa/inflection.git)



#### Collaboration 
- I talked to Yuwei about high-level project ideas and he suggested me to try the Unimorph model. 
- I talked to Zhicheng about the performance of our solutions with respect to the baseilne. 
- I went to Anjali's office hour and she suggested me to try to improve on the non-neural baseilne of kbd. 