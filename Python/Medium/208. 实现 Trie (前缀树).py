class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        r = self.root
        for c in word:
            if c not in r.next:
                r.next[c] = TrieNode()
            r = r.next[c]
        r.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        r = self.root
        for c in word:
            if c not in r.next:
                return False
            r = r.next[c]
        return r.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        r = self.root
        for c in prefix:
            if c not in r.next:
                return False
            r = r.next[c]
        return True


class TrieNode:

    def __init__(self):
        self.isEnd = False
        self.next = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)