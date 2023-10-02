# Assignment 5
# By: Nils William Dunlop & Francisco Alejandro Erazo Piza

from typing import Optional, Dict, Any, List


class Trie:
    def __init__(self) -> None:
        # Initialize node attributes
        self.value: Optional[Any] = None
        self.endOfWord: bool = False
        self.active: bool = True
        self.children: Dict[str, Trie] = {}

    def insert(self, path: List[str], val: str) -> None:
        """The insert method traverses the Trie according to the given path list
           and inserts the word with the associated value"""
        current = self
        for part in path:
            # If the current part is not a child of the current node create a new Trie node for this part
            if part not in current.children:
                current.children[part] = Trie()
            # Move to the child node representing the current part
            current = current.children[part]
        # Mark the last node as the end of a word and set its value
        current.endOfWord = True
        current.value = val

    def fetch(self, path: List[str]) -> Optional[str]:
        """The fetch method traverses the Trie based on the given path list and
           retrieves the value of the word if it exists in the Trie."""
        current = self
        for part in path:
            # If the part is not found in the current node’s children the word does not exist in the Trie
            if part not in current.children:
                return None
            # Move to the next node in the path
            current = current.children[part]
        # Return the value of the last node if it marks the end of a word
        return current.value if current.endOfWord else None

    def delete(self, path: List[str]) -> Optional[str]:
        """The delete method deletes a word represented by the path list from the Trie.
           It returns the value of the deleted word if the word exists, else returns None."""
        # Stack to hold traversed nodes and their parts
        stack = [(self, '')]
        current = self
        for part in path:
            # If the part is not found in the current node’s children the word does not exist in the Trie
            if part not in current.children:
                return None
            current = current.children[part]
            # Add each traversed node and its part to the stack
            stack.append((current, part))
        if not current.endOfWord:
            # The given path does not correspond to a word in the Trie
            return None
        deleted_value = current.value
        # Mark the last node as inactive and remove its value
        current.endOfWord = False
        current.value = None

        # Traverse back and remove inactive nodes and update the 'active' status
        while stack:
            node, part = stack.pop()
            if not any(child.active for child in node.children.values()) and not node.endOfWord:
                # Avoid deleting the root node.
                if stack:
                    parent, _ = stack[-1]
                    del parent.children[part]
                    node.active = False
        return deleted_value


# Example Usage:
print("Test 1")
t = Trie()
for word, val in zip(['alphabet', 'beta', 'gamma'], [1, 2, 3]):
    t.insert(word, val)
print(t.fetch('alpha'))  # None
print(t.fetch('beta'))  # 2
print(t.fetch('alphabet'))  # 1
print(t.fetch('Gamma'))  # None
print(t.fetch('gamma'))  # 3

print("\nTest 2")
t = Trie()
t.insert('alpha', 10)
a = t.delete('alpha')
print(a)  # a = 10
print(t.fetch('alpha'))  # None

t.insert('alpha', 10)
t.insert('alphabet', 22)
a = t.delete('alpha')
print(a)  # a = 10
print(t.fetch('alphabet'))  # 22
print(t.fetch('alpha'))  # None

print("\nTest 3")
t = Trie()
path1 = ["/", "home", "/", "user", "/", "folder1", "/", "file1"]
path2 = ["/", "home", "/", "user", "/", "folder1", "/", "file2"]
path3 = ["/", "home", "/", "user", "/", "folder2", "/", "file3"]

t.insert(path1, "2022-09-22")
t.insert(path2, "2023-01-19")
t.insert(path3, "2021-04-01")

print(t.fetch(path1))  # 2022-09-22
print(t.delete(path1))  # 2022-09-22
print(t.fetch(path2))  # 2023-01-19
print(t.fetch(path1))  # None
print(t.fetch(["/", "home"]))  # None
print(t.fetch(path3))  # 2021-04-01
