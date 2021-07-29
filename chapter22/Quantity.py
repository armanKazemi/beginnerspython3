class Quantity:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other.value, dict):
            self.value.update(other.value)
            return Quantity(self.value)

        if isinstance(other.value, str) & (isinstance(self.value, int) or isinstance(self.value, float)):
            return Quantity(str(self.value) + other.value)
        elif isinstance(self.value, str) & (isinstance(other.value, int) or isinstance(other.value, float)):
            return Quantity(self.value + str(other.value))

        new_value = self.value + other.value
        return Quantity(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Quantity(new_value)

    def __mul__(self, other):
        if isinstance(other, int):
            new_value = self.value * other
        else:
            new_value = self.value * other.value
        return Quantity(new_value)

    def __pow__(self, other):
        new_value = self.value ** other.value
        return Quantity(new_value)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_value = self.value / other
        else:
            new_value = self.value / other.value
        return Quantity(new_value)

    def __floordiv__(self, other):
        new_value = self.value // other.value
        return Quantity(new_value)

    def __mod__(self, other):
        new_value = self.value % other.value
        return Quantity(new_value)

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __str__(self):
        return 'Quantity[' + str(self.value) + ']'


def main():
    q1 = Quantity(5)
    q2 = Quantity(10)
    print('q1 =', q1, ', q2 =', q2)

    q3 = q1 + q2
    print('q3 =', q3)
    print('q2 - q1 =', q2 - q1)

    print('q1 * q2 =', q1 * q2)
    print('q1 / q2 =', q1 / q2)

    print('q1 < q2: ', q1 < q2)
    print('q3 > q2: ', q3 > q2)
    print('q3 == q1: ', q3 == q1)

    print('q1 * 2', q1 * 2)
    print('q2 / 2', q2 / 2)

    p1 = Quantity('aa')
    p2 = Quantity('ddd')
    print('p1 + p2:', p1 + p2)

    d1 = {'0': 0,
          '1': 1}
    d2 = {'2': 2,
          '3': 3}
    dq1 = Quantity(d1)
    dq2 = Quantity(d2)
    print('dq1 + dq2:', dq1 + dq2)

    print('p1 + q1:', p1 + q1)


if __name__ == '__main__':
    main()
