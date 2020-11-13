import json

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
            node = current_node[letter]
        return True