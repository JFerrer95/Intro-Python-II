class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f'{player} picked up {self.name}')

    def on_drop(self, player):
        print(f'{player} dropped {self.name}')

