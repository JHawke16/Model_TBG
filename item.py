class Item:
    def __init__(self, name, use_function, value):
        self.name = name
        self.use_function = use_function
        self.value = value

    def use(self, target):
        self.use_function(target)
