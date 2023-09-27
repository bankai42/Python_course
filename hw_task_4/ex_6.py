import re

class Data:
    def __init__(self, path) -> None:
        self.path = path
        self.text_data = []

    def read_data(self):
        with open(self.path, 'r') as f:            
            self.text_data = f.readlines()

    def find_pattern(self, pattern):
        result = []
        for line in self.text_data:
            result = result + re.findall(pattern, line)
        return result

if __name__ == "__main__":
    data = Data("hw_task_4\data.txt")
    data.read_data()
    print(data.text_data)
    pat = r'\d'
    numbers = data.find_pattern(pat)
    print(numbers)


