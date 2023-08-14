class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.order = []

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end = True
        self.order.append(word)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def collectWordsPrefix(self, prefix):
        prefix_node = self.search(prefix)

        if prefix_node:
            collected = [word for word in self.order if word.startswith(prefix)]
            return collected
        else:
            return []


