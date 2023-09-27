from typing import Optional, Dict, Any


class Trie:
    def __init__(self) -> None:
        self.value: Optional[Any] = None
        self.endOfWord: bool = False
        self.active: bool = True
        self.children: Dict[str, Trie] = {}

    def insert(self, path: str, val: int) -> None:
        current = self
        for letter in path:
            if letter not in current.children:
                current.children[letter] = Trie()
            current = current.children[letter]
        current.endOfWord = True
        current.value = val

    def fetch(self, path: str) -> Optional[int]:
        current = self
        for letter in path:
            if letter not in current.children:
                return None
            current = current.children[letter]

        if current.endOfWord:
            return current.value
        else:
            return None

    def delete(self, path: str) -> Optional[int]:
        # Stack to track the traversed nodes
        stack = [(self, '')]

        current = self
        for letter in path:
            if letter not in current.children:
                return None
            current = current.children[letter]
            # Add current node and the letter to the stack
            stack.append((current, letter))

        # If word not in Trie, return None
        if not current.endOfWord:
            return None

        # If the word exists, return value and mark it as inactive
        deleted_value = current.value
        current.endOfWord = False
        current.value = None

        # Traverse back to delete nodes that is not part of any active word
        while stack:
            node, letter = stack.pop()
            if not any(child.active for child in node.children.values()) and not node.endOfWord:
                # Check if this is not the root node
                if stack:
                    parent, _ = stack[-1]
                    del parent.children[letter]
                    # Mark the node as inactive
                    node.active = False

        return deleted_value


# First test case
# t = Trie()
# for word, val in zip(["alphabet", "beta", "gamma"], [1, 2, 3]):
#     t.insert(word, val)
#
# print(t.fetch("alpha"))
# print(t.fetch("beta"))
# print(t.fetch("alphabet"))
# print(t.fetch("Gamma"))
# print(t.fetch("gamma"))

# Second test case
t = Trie()
t.insert("alpha", 10)
a = t.delete("alpha")
print(a)  # 10
print(t.fetch("alpha"))  # None

t.insert("alpha", 10)
t.insert("alphabet", 22)
b = t.delete("alpha")
print(b)  # 10
print(t.fetch("alphabet"))  # 22
print(t.fetch("alpha"))  # None
