orig_word = input()

vowels = ['A','E','I','O','U']

kevin_words = []
stuart_words = []
kevin_dict = {}
kevin_score = 0
stuart_dict = {}
stuart_score = 0

for i in range(0,len(orig_word)):
	if orig_word[i] in vowels:
		for j in range(i,len(orig_word)):
			kevin_words.append(''.join(orig_word[i:j+1]))
	else:
		for j in range(i,len(orig_word)):
			stuart_words.append(''.join(orig_word[i:j+1]))
			
kevin_uniq_words = set(kevin_words)

for item in kevin_uniq_words:
	for item1 in kevin_words:
		if item == item1:
			if item in kevin_dict:
				kevin_dict[item] += 1
			else:
				kevin_dict[item] = 1
				
for item in kevin_dict:
	kevin_score += kevin_dict[item]
	
stuart_uniq_words = set(stuart_words)

for item in stuart_uniq_words:
	for item1 in stuart_words:
		if item == item1:
			if item in stuart_dict:
				stuart_dict[item] += 1
			else:
				stuart_dict[item] = 1
				
for item in stuart_dict:
	stuart_score += stuart_dict[item]
	
if stuart_score > kevin_score:
	print("Stuart", stuart_score)
elif kevin_score > stuart_score:
	print("Kevin", kevin_score)
else:
	print("Draw")