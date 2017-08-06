class Parrot:
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage



if __name__ == '__main__':
    c = Parrot
    # c.voltage=10
    print(c.voltage)
    print(c.mro())