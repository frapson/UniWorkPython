BinaryNumbers = [bin(i) for i in range(128)]

for decimal, binary in enumerate(BinaryNumbers, 0):
    print(decimal, '{:0>8}'.format(str(binary[2:])))
