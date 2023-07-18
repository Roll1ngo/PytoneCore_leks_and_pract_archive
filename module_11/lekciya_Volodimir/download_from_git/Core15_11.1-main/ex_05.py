class Aquarium:
    def __init__(self, fishes):
        self.fishes = fishes
    
    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.fishes):
            f = self.fishes[self.current_index]
            self.current_index += 1
            return f
        raise StopIteration


aqua = Aquarium(["neon", "scalariya", "shark"])

for fish in aqua:
    print(fish)