#!/usr/bin/python

class EditDistance():
	
	def __init__(self):
		"""
		Do not change this
		"""
	
	def calculateLevenshteinDistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their Levenshtein Distance for task 1 
			return an integer which is the distance

        Hint:
	 	This approach uses dynamic programming. Key idea is if we compute the distance 
	 	between the prefix of the first string and the prefix of the second string, 
	 	find the distance between the two full strings using the distance between the last
	 	computed prefix values. Store the distances in a matrix to incrementally
	 	solve the problem, one character at a time.

	 	You are free to use other approaches to the problem.
		Pseudocode:
		Create a 2D distance table with:
			rows = length of str1 +1
			col = length of str2 +1

		for i goes from 1 to number of rows in table:
			for j goes from 1 to number of col in table:
				1. Compute delete_cost

				2. Compute insertion_cost

				3. Compute substitute_cost

				Store minimum of the 3 costs at the table[i][j] location.

		return table[row][col]

		"""
		m = len(str1)
		n = len(str2)

		if m == 0:
			return n
		if n == 0:
			return m

		memo = [[0 for i in range(n+1)] for j in range(m+1)]
		# base case
		for i in range(1,m+1):
			memo[i][0] = i
		for j in range(1,n+1):
			memo[0][j] = j

		# dynamic programming
		for i in range(1,m+1):
			for j in range(1,n+1):
				if str1[i-1] == str2[j-1]:
					memo[i][j] = memo[i-1][j-1]
				else:
					memo[i][j] = min(
						memo[i-1][j] + 1,
						memo[i][j-1] + 1,
						memo[i-1][j-1] + 1
					)
		return memo[m][n]

		
	def calculateOSADistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their OSA Distance for task 2 
			return an integer which is the distance

		Hint: Use the Pseudocode provided in calculateLevenshteinDistance and 
		add an additional check to compute the transpose distance. Update 
		the table[i][j] location's value accordingly.

		"""
		m = len(str1)
		n = len(str2)

		if m == 0:
			return n
		if n == 0:
			return m

		memo = [[0 for i in range(n+1)] for j in range(m+1)]
		# base case
		for i in range(1,m+1):
			memo[i][0] = i
		for j in range(1,n+1):
			memo[0][j] = j

		# dynamic programming
		for i in range(1,m+1):
			for j in range(1,n+1):
				if str1[i-1] == str2[j-1]:
					memo[i][j] = memo[i-1][j-1]
				else:
					memo[i][j] = min(
						memo[i-1][j] + 1,
						memo[i][j-1] + 1,
						memo[i-1][j-1] + 1
					)
				if i > 1 and j > 1 and str1[i-1] == str2[j-2] and str1[i-2] == str2[j-1]:
					memo[i][j] = min(
						memo[i][j],
						memo[i-2][j-2] + 1
					)
		return memo[i][j]

		
	def calculateDLDistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their DL Distance for task 3 
			return an integer which is the distance

		Pseudocode:
		Create a 2D distance table with:
			rows = length of str1 +1
			columns = length of str2 +1

		Create an alphabet_map:
			A dictionary of unique characters of str1 & str2:
				key: unique character
				value: Number of unique characters seen before the 'key'
			Eg. str1 = 'abc', str2 = 'man'
			alphabet_map = {'a':0, 'b': 1, 'c': 2, 'm':3, 'n': 4}

		Create distance1 = list of 0s of length as number entries in alphabet_map

		for i goes from 1 to number of rows in table:
			Reset distance2 to 0
			for j goes from 1 to number of cols in table:
				k = distance1[alphabet_map[str2[j - 1]]]
				l = distance2
				1. Compute delete_cost

				2. Compute insertion_cost

				3. Compute substitute_cost
					Additionally, if substitute is possible
						Set distance2 to j

				4. Compute transposition_cost
					Sum of the following: 
					a. table[k - 1][l - 1]
					b. (i - k - 1)
					c. (j - l - 1)
					d. 1

				Store minimum of the 4 costs at the table[i][j] location.

			Set distance1[alphabet_map[str1[i - 1]]] to i

		return table[row][col]

		"""
		m = len(str1)
		n = len(str2)

		if m == 0:
			return n
		if n == 0:
			return m

		memo = [[0 for i in range(n+1)] for j in range(m+1)]
		# base case
		for i in range(1,m+1):
			memo[i][0] = i
		for j in range(1,n+1):
			memo[0][j] = j

		alphabet_map = {}
		letters = []
		duplicated_num = 0
		for idx,letter in enumerate(list(str1+str2)):
			if letter not in letters:
				letters.append(letter)
				alphabet_map[letter] = idx - duplicated_num
			else:
				duplicated_num += 1
		
		distance1 = [0 for i in letters]

		for i in range(1,m+1):
			distance2 = 0
			for j in range(1,n+1):
				k = distance1[alphabet_map[str2[j-1]]]
				l = distance2
				
				if str1[i-1] == str2[j-1]:
					memo[i][j] = memo[i-1][j-1]
				else:
					distance2 = j
					memo[i][j] = min(
						memo[i-1][j-1] + 1,
						memo[i-1][j] + 1,
						memo[i][j-1] + 1,
						memo[k-1][l-1] + i - k + j - l - 1
					)

			distance1[alphabet_map[str1[i-1]]] = i
		return memo[m][n]		

