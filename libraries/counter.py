from collections import Counter
import re

context = re.findall(r'\w+', open('example.txt').read().lower())
words_count_dict = Counter(context)
not_useful_words = ['a','the','of','what','in', 'it', 'is', 'and', 'words', 'you', 'do', 'to', 'we']
for x in not_useful_words:
	if(words_count_dict.has_key(x)):
		words_count_dict.pop(x)
top_10_words = words_count_dict.most_common(10) 
context_words = []
for key,val in top_10_words:
	context_words.append(key)
print("--------this document context might be -------")
print("%s"%(','.join(context_words)))