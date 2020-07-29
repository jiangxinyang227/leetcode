class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["#"] = "#"  # 添加单词终止符
        print(self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            if char not in cur:
                return False
            cur = cur[char]
        if "#" in cur:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            if char not in cur:
                return False
            cur = cur[char]
        return True


trie = Trie()
trie.insert("code")
trie.insert("cook")
trie.insert("final")
trie.insert("fit")
trie.insert("fat")
trie.insert("cod")
