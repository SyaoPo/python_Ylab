
class CyclicIterator:
  
    def __init__(self, iterable):
        self.iterable = list(iterable)

    def __iter__(self):
        self.elem = -1
        return self

    def __next__(self):
        if self.elem < len(self.iterable) - 1:
            self.elem += 1
            return self.iterable[self.elem]
        else:
            self.elem = 0
            return self.iterable[self.elem]


def main():
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)


if __name__ == "__main__":
