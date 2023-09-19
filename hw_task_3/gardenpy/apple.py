class Apple:
    __stages = ['flower', 'green', 'red']
    __stage_id = 0
    def __init__(self, id) -> None:
        self.id = id
        self.stage = self.__stages[self.__stage_id]

    def grow(self):        
        if self.__stage_id < len(self.__stages)-1:
            self.__stage_id += 1
            self.stage = self.__stages[self.__stage_id]

    def isRed(self):
        if self.stage == self.__stages[-1]:
            return True
        else: return False


if __name__ == "__main__":
    apple = Apple(1)
    print(apple.stage)
    apple.grow()
    print(apple.stage)
    print(apple.isRed())
    apple.grow()
    print(apple.stage)
    apple.grow()
    print(apple.stage)
    print(apple.isRed())




