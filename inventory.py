class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f'Added {item.name} to inventory.')

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f'Removed {item.name} from inventory.')

    def get_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return item
        return None

    def display_items(self):
        if not self.items:
            print("No items in inventory.")
        else:
            print("Items in inventory:")
            for item in self.items:
                print(f'- {item.name}')

    def is_empty(self):
        return len(self.items) == 0
