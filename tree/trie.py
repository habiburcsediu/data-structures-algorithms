class TrieNode:
    def __init__(self):
        self.children = {} # Dictionary for storing nodes
        self._is_end_of_word = False # Indicates the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _insert(self, word):
        """Helper function to insert a single word into the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If the char is not already a child, add a new TrieNode
                current.children[char] = TrieNode()
            current = current.children[char] # Traverse to the next child node
        current._is_end_of_word = True # Mark the end of the word

    def build_trie(self, words):
        """Build Trie by inserting each word from the given list of words"""

        for word in words:
            self._insert(word)

    def _dfs(self, current, path, result):
        """Helper function to perform DFS and collect words"""

        if current._is_end_of_word: # True: found a valid word, so append it to the result
            result.append(path)

        # Recursively explore all possible child
        for char, next_node in current.children.items():
            self._dfs(next_node, path + char, result)

    def display(self):
        """Return a list of all words stored in the Trie"""

        result = []
        # Start DFS from the root, path concatenates all characters of a word and result store word
        self._dfs(self.root, "", result)

        return result

    def add_word(self, word):
        """Add a new word to the Trie"""

        self._insert(word)

    def delete_word(self, word):
        """Delete a word from the Trie"""

        def _delete(current, word, index):
            if index == len(word): # Checking if word is found?
                if not current._is_end_of_word: # False: Not a word, it is a prefix of any other word
                    return False # Word not found

                """
                True: it is a valid word. Now checking if it has a child?
                If it has a child, meaning it is consider a prefix of any other word
                Can not delete it from memory, just marks False to the end of the word 
                """
                current._is_end_of_word = False
                return len(current.children) == 0 # If it has not a child, it must be deleted from memory

            char = word[index]
            if char not in current.children:
                return False # Word not found

            should_delete_child = _delete(current.children[char], word, index + 1)
            if should_delete_child:
                del current.children[char] # Delete from the memory
                return not current._is_end_of_word and len(current.children) == 0

            return False # As it is a prefix of a child, can not delete any node, so return False

        _delete(self.root, word, 0)

    def contains(self, word):
        """Check if the given word exists in the Trie"""

        current = self.root
        for char in word:
            if char not in current.children: # If char not found, meaning the given word is not stored in the Trie
                return False
            current = current.children[char]

        return current._is_end_of_word # True if this current node marks the end of a complete word

    def has_prefix(self, prefix):
        """Check if the given prefix exists in the Trie """

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True # Return True if all the characters of the given prefix exits

    def starts_with(self, prefix):
        """Return all words in the Trie that start with the given prefix"""

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._dfs(current, prefix, result) # Traverse the Trie from the prefix node to collect all complete words

        return result

# Example usage
trie = Trie()

words = ["apple", "app", "application", "bat", "banana"]

# Build the Trie from a list of words
trie.build_trie(words)
# Display all words stored in the Trie
print("Initial words:", trie.display())

# Add a new word in the Trie
trie.add_word("ball")
print("After adding `ball`:", trie.display())

# Delete a word from the Trie
trie.delete_word("banana")
print("After deleting `banana`:", trie.display())

# Checking if a word contains in the Trie
print("Contains `application`?", trie.contains("application"))

# Checking if the given prefix exists in the Trie
print("Has prefix `app`?>", trie.has_prefix("app"))

# Find all words that start with the given prefix
print("Words starting with `app`", trie.starts_with("app"))