from apple import Apple
from typing import List

class Tree:
    def __init__(self, *apples: Apple) -> None:
        self.apples: List(Apple) = []
        for arg in apples:
            self.apples.append(arg)
        
    def grow(self):
        for apple in self.apples:
            apple.grow()

    def print(self):
        for apple in self.apples:
            print(f"Apple {apple.id}: {apple.stage}")

    def isGrown(self):
        for apple in self.apples:
            if not apple.isRed():
                return False
            else: return True
    
    def give_crop(self):
            self.apples.clear()


if __name__ == "__main__":
    apple1 = Apple(1)
    apple2 = Apple(2)
    apple3 = Apple(3)
    tree = Tree(apple1, apple2, apple3)
    tree.print()
    tree.grow()
    tree.print()
    print(tree.isGrown())
    tree.give_crop()
    tree.grow()
    tree.print()
    print(tree.isGrown())
    tree.give_crop()

