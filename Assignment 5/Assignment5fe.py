from typing import Optional, Dict, List, Union

class Trie:
    def __init__(self) -> None:
        # Initialize the Trie node with optional value (int or str), children, and no endOfWord marker.
        self.value: Optional[Union[int, str]] = None
        self.children: Dict[str, 'Trie'] = {}

    def insert(self, path: List[str], date: str) -> None:
        """
        Insert a new node with the specified date value into the Trie.

        Args:
            path (List[str]): List of path components as keys.
            date (str): Date value to be associated with the path.

        Returns:
            None
        """
        node = self
        for component in path:
            # Traverse the Trie based on path components.
            if component not in node.children:
                node.children[component] = Trie()
            node = node.children[component]
        # Assign the date value to the final node.
        node.value = date

    def fetch(self, path: List[str]) -> Optional[Union[int, str]]:
        """
        Fetch the value associated with the specified path from the Trie.

        Args:
            path (List[str]): List of path components as keys.

        Returns:
            Optional[Union[int, str]]: The associated value or None if not found.
        """
        node = self
        for component in path:
            # Traverse the Trie based on path components.
            if component not in node.children:
                return None
            node = node.children[component]
        return node.value if node.value is not None else None

    def delete(self, path: List[str]) -> Optional[Union[int, str]]:
        """
        Delete the node associated with the specified path from the Trie.

        Args:
            path (List[str]): List of path components as keys.

        Returns:
            Optional[Union[int, str]]: The value associated with the deleted node or None if not found.
        """
        node = self
        parent_nodes = [self]  # Track parent nodes for potential removal.
        deleted_value = None

        for component in path:
            # Traverse the Trie based on path components.
            if component not in node.children:
                return None
            parent_nodes.append(node)
            node = node.children[component]

        if node.value is not None:
            deleted_value = node.value
            node.value = None

        # Check if the node has no children and is not the root, in which case we can remove it.
        if not node.children and parent_nodes[-1] is not self:
            parent_node = parent_nodes[-1]
            del parent_node.children[component]

        return deleted_value


# Test the code
print("")
print("Test 1")
t = Trie()
for word, val in zip(['alphabet', 'beta', 'gamma'], [1, 2, 3]):
    t.insert(word, val)

print(t.fetch('alpha'))    # None
print(t.fetch('beta'))     # 2
print(t.fetch('alphabet')) # 1
print(t.fetch('Gamma'))    # None
print(t.fetch('gamma'))    # 3

print("")
print("Test 2")
t = Trie()
t.insert('alpha', 10)
a = t.delete('alpha')  # a == 10
print(a)
print(t.fetch('alpha'))  # None

t.insert('alpha', 10)
t.insert('alphabet', 22)
a = t.delete('alpha')  # a = 10
print(a)
print(t.fetch('alphabet'))  # 22
print(t.fetch('alpha'))  # None

print("")
print("Test 3")
t = Trie()
path1 = ["/", "home", "/", "user", "/", "folder1", "/", "file1"]
path2 = ["/", "home", "/", "user", "/", "folder1", "/", "file2"]
path3 = ["/", "home", "/", "user", "/", "folder2", "/", "file3"]

t.insert(path1, "2022-09-22")
t.insert(path2, "2023-01-19")
t.insert(path3, "2021-04-01")

print(t.fetch(path1))            # "2022-09-22"
print(t.delete(path1))           # "2022-09-22"
print(t.fetch(path2))            # "2023-01-19"
print(t.fetch(path1))            # None
print(t.fetch(["/", "home"]))    # None
print(t.fetch(path3))            # "2021-04-01"

