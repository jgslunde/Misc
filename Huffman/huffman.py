# Contains functions for zipping and unzipping text with the Huffman text compression algorithm.

def huffman_zip(text):
	# Takes a string of text (unicode compatible), and returns a dictionary with the
	# huffman-code of every character, and the huffman-code itself, as a string
	symbols_code = {}	# Dictionary with huffman code of each symbol.
	nodes_dic = {}		# Dictionary of nodes. keys will be a list of symbols in the same node of the huffman tree, and elements will be their combigned weight.
	for symbol in text:	# Makes every symbol into a node on the tree.
		if tuple(symbol) in nodes_dic:
			nodes_dic[tuple(symbol)] += 1
		else:
			nodes_dic[tuple(symbol)] = 1
			symbols_code[symbol] = ""

	if len(nodes_dic) == 1:	# Special case: only one letter(the while-loop doesn't cover this case)
		symbols_code = {text[0]:'0'}

	def queue(nodes_weight):# Takes the nodes dictionary and returns the keys(list of symbols) of the two nodes with lowest weight.
		next = [nodes_weight.keys()[0], nodes_weight.keys()[1]]
		for s in nodes_weight:
			if nodes_weight[s] < nodes_weight[next[0]] and tuple(s) != next[0] and tuple(s) != next[1]:
				next[0] = s
		for s in nodes_weight:
			if nodes_weight[s] < nodes_weight[next[1]] and tuple(s) != next[0] and tuple(s) != next[1]:
				next[1] = s
		return next

	while len(nodes_dic) > 1:# Combines nodes and adds code to the symbols their represent.
		next = queue(nodes_dic)
		for node in next[0]:
			symbols_code[node] = "0" + symbols_code[node]
		for node in next[1]:
			symbols_code[node] = "1" + symbols_code[node]
		nodes_dic[next[0] + next[1]] = nodes_dic[next[0]] + nodes_dic[next[1]]
		del nodes_dic[next[0]]	# Avoidng duplicates (when [H,E] is a key, we don't also want H and E seperately.
		del nodes_dic[next[1]]

	zipped = ""
	for letter in text:	# Converts the original input text to our generated code for each symbol.
		zipped += symbols_code[letter]

	return symbols_code, zipped

def huffman_unzip(symbols_code, zipped):
	# Takes the output dictionary and code from huffman_zip, and returns original text as a string.
	code_symbols = dict((v,k) for k,v in symbols_code.iteritems())	#Swaps keys and values in the dic.
	text = ""
	symbols = ""
	for symbol in zipped:	# We read the code until we find a sequence that fits with a coded symbol. Then repeat from where we left.
		symbols += symbol
		if symbols in code_symbols:
			text += code_symbols[symbols]
			symbols = ""
	return text
