#!/usr/bin/python
# Reference for Trie: https://www.geeksforgeeks.org/trie-insert-and-search/
import json
from editdistance import EditDistance

class Trie:
    def __init__(self):
        self.root = {}
        self.end_word = '$'
    
    def get_tree(self):
        beautiful_format = json.dumps(self.root,indent=4)
        print(beautiful_format)

    def insert(self,word):
        current_node = self.root
        for letter in word:
            current_node = current_node.setdefault(letter,{})
        current_node[self.end_word] = self.end_word
    
    def search(self,word):
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return self.end_word in current_node
    
    def startsWith(self, prefix):
        current_node = self.root
        for letter in prefix:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True

def task4(dictionary, raw):
	"""
	TODO:
		implement your optimized edit distance function for task 4 here
		dictionary : path of dictionary.txt file 
		raw: path of raw.txt file
		return : a list of min_distance of each word in the raw.txt 
		compared with words in the dictonary 
	example return result : [0,1,0,2]
	"""
	mis_words = []
	with open(raw) as f:
		for word in f:
			mis_words.append(word.strip())
	
	dict_words = []
	with open(dictionary) as f:
		for word in f:
			dict_words.append(word.strip())
	
	editDistance = EditDistance()
	trie = Trie()
	for word in dict_words:
		trie.insert(word)
	
	min_dist = []
	for word in mis_words:
		if trie.search(word):
			min_dist.append(0)
			continue
		else:
			terminated = False
			for i in range(len(word)):
				if trie.startsWith(word[:i+1]):
					pass
				else:
					terminated = True
				
				if terminated:
					if i == 0:
						word_dist = []
						for dict_word in dict_words:
							word_dist.append(editDistance.calculateOSADistance(word,dict_word))
						min_dist.append(min(word_dist))
						break
					else:
						sub_str = word[:i]
						for dict_word in dict_words:
							if dict_word.startswith(sub_str):
								min_dist.append(editDistance.calculateOSADistance(word,dict_word))
								break
	
	return min_dist





