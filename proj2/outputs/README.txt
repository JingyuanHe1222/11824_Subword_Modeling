Project 2: Reinflection & Paradigm Completion

The goal of this project is to generate the inflectional forms of verbs for Karbardian (kbd), Swahili (sic), and Mixtec (sty) from roots + inflectional information. Scores will be based on exact match accuracy. Files are formatted in the following way, based on the unimorph standard:

[ROOT] ([CORRECT]) [INFLECTION]

For this project the baselines can be found here: https://colab.research.google.com/drive/1nskoaUtxGfzk4GWqVJQUG2DSA-XsmSon?usp=sharing

The scores to beat are as follows:

	Non-Neural	Neural 
kbd 	88.5 		67.6
swc 	72.3 		0.95
xty 	73.5 		79.8 

Please name your files as {lang}.txt - i.e. ‘kbd.txt’ - for submission to the autograder. Your submissions will be a list of generated forms, separated by newlines. 