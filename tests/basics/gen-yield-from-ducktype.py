class MyGen:

    def __init__(self):
        self.v = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.v += 1
        if self.v > 5:
            raise StopIteration
        return self.v

def gen():
    yield from MyGen()

def gen2():
    yield from gen()

print(list(gen()))
print(list(gen2()))


class Incrementer:

    def __iter__(self):
        return self

    def __next__(self):
        return self.send(None)

    def send(self, val):
        if val is None:
            return "Incrementer initialized"
        return val + 1

def gen3():
    yield from Incrementer()

g = gen3()
print(next(g))
print(g.send(5))
print(g.send(100))
