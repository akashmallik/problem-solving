class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def __repr__(self):
        return self.name

    def add_child(self, name: str) -> "Node":
        self.children.append(Node(name))
        return self

    def dfs(self, array: list) -> list:
        array.append(self.name)
        for child in self.children:
            child.dfs(array)

        return array


if __name__ == "__main__":
    graph = Node("A")
    graph.add_child("B").add_child("C").add_child("D")
    graph.children[0].add_child("E").add_child("F")
    graph.children[0].children[1].add_child("I").add_child("J")
    graph.children[2].add_child("G").add_child("H")
    graph.children[2].children[0].add_child("K")

    assert graph.dfs([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
