import hashlib
# your flag is flag{md5(secret).hexdigest()}

def string2bits(s):
    return [int(b) for b in s]

def bits2string(bs):
    s = [str(b) for b in bs]
    return ''.join(s)

if __name__ == '__main__':
    initState = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    outputState = string2bits('1010100001001011101000000100100001101011010100101011010101011010100100001110010010110111010111110000000000011011001110100011000111110100110011011011100111000000001100001000001011010011011010110110111100110101001110001001001000001110111011110001111001111111')
    states = initState + outputState

    ms = MatrixSpace(GF(2), 128, 128)
    mv = []
    for i in range(128):
        mv += states[i : i + 128]
    m = ms(mv)

    vs = MatrixSpace(GF(2), 128, 1)
    vv = outputState[0:128]
    v = vs(vv)

    secret = m.inverse() * v
    flag = ''
    for i in range(128):
        flag += str(secret[i][0])
    print(flag)

    h = hashlib.md5()
    h.update(flag.encode())
    flag = 'flag{' + h.hexdigest() + '}'
    print(flag)

