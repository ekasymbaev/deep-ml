def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	ROW = len(a)
	COL = len(a[0])
	VecRow = len(b)
	res = []
	
	if COL != VecRow:
		return -1
	
	for row in a:
		curSum = 0
		for i in range(COL):
			curSum += row[i]*b[i]

		res.append(curSum)
		
	return res
	

	
	

	