def checkMathExpr(expr):
	count = 0

	for i in expr:
		if count < -1:
			return False

		if i == '(':
			count += 1

		if i == ')':
			count -= 1

	if count == 0:
		return True
	else:
		return False

mathExpr = '((((((abccccsdfsdffsd)('

print(checkMathExpr(list(mathExpr)))