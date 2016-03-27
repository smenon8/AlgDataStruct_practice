text = input()

l = text.split(" ")
l_new = []
for word in l:
	if word.isalnum() and word[0].isalpha():
		word = word[0].upper()+word[1:]
		l_new.append(word)
	else:
		l_new.append(word)
print(' '.join(l_new))