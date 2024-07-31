class Flower:
    def __init__(self, name, color, length, fresh_days, price, life_days):
        self.name = name
        self.color = color
        self.length = length
        self.fresh_days = fresh_days
        self.price = price
        self.life_days = life_days

    def __repr__(self):
        return (f"{self.name}(color: {self.color}, length: {self.length}cm, "
                f"freshness: {self.fresh_days} days, price: {self.price}$, life duration: {self.life_days} days)")


class Orchid(Flower):
    def __init__(self, color, length, fresh_days, price, life_days=10):
                super().__init__("Orchid", color, length, fresh_days, price, life_days)


class Rose(Flower):
    def __init__(self, color, length, fresh_days, price, life_days=5):
        super().__init__("Rose", color, length, fresh_days, price, life_days)


class Lily(Flower):
    def __init__(self, color, length, fresh_days, price, life_days=4):
        super().__init__("Lily", color, length, fresh_days, price, life_days)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flowers(self, flower):
        self.flowers.append(flower)

    def total_sum(self):
        return sum(flower.price for flower in self.flowers)

    def aver_life_dur(self):
        return int(sum(flower.life_days for flower in self.flowers) / len(self.flowers))

    def sort_by(self, attribute):
        self.flowers.sort(key=lambda flower: getattr(flower, attribute, None))

    def __str__(self):
        return "\n".join([str(flower) for flower in self.flowers])

    def search_by_color(self, color):
        return [flower for flower in self.flowers if flower.color == color]

    def __repr__(self):
        return f"Bouquet({self.flowers})"


orchid1 = Orchid(color="pink", length=30, fresh_days=9, price=10)
rose1 = Rose(color='red', length=32, fresh_days=8, price=8)
lily1 = Lily(color='white', length=29, fresh_days=3, price=7)
bouquet = Bouquet()
bouquet.add_flowers(orchid1)
bouquet.add_flowers(rose1)
bouquet.add_flowers(lily1)

print(f"The total cost of the bouquet is {bouquet.total_sum()}$")
print(f"The average life duration of the bouquet is {bouquet.aver_life_dur()} days")

bouquet.sort_by("price")
print("Bouquet sorted by price:")
print(bouquet)

print("\nSearch for flowers by color 'pink':")
print(bouquet.search_by_color('pink'))







