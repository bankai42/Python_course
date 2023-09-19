from apple import Apple
from tree import Tree
from typing import List

class Gardner:
    def __init__(self, name, *trees: Tree) -> None:
        self.name = name
        self.trees: List[Tree] = [tree for tree in trees]
        self.print()

    def print(self):
        for i, tree in enumerate(self.trees):
            print(f"----Tree {i}----")
            tree.print()

    def do_gardening(self):
        for tree in self.trees:
            tree.grow()
    
    def harvest_crop(self):
        for i, tree in enumerate(self.trees):
            if tree.isGrown():
                tree.give_crop()
                print(f"[+] Apples from Tree {i} are harvested. Tree is empty!")
            else: print(f"[-] Not all apples on Tree {i} are ripe! Try to harvest later.")


if __name__ == "__main__":
    apple1 = Apple(1)
    apple2 = Apple(2)
    apple3 = Apple(3)
    apple4 = Apple(4)
    tree1 = Tree(apple1, apple2, apple3)
    tree2 = Tree(apple4)
    gardner = Gardner('Bob', tree1, tree2)
    gardner.do_gardening()
    gardner.print()
    gardner.harvest_crop()
    gardner.do_gardening()
    gardner.print()
    gardner.harvest_crop()

