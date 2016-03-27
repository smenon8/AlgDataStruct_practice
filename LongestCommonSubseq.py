# LCS using dynamic programming recursive method

def lcs(seq1,seq2,m,n):
	if m == 0 or n == 0:
		return 0
	else:
		if seq1[m-1] == seq2[n-1]:
			return 1 + lcs(seq1,seq2,m-1,n-1)
		else:
			return (max(lcs(seq1,seq2,m-1,n),lcs(seq1,seq2,m,n-1)))
			
seq1 = ['a','c','t','g','g','a','c','t','a']	
seq2 = ['g','c','t','g','g','a','c','t','a']		

lcs(seq1,seq2,len(seq1),len(seq2))