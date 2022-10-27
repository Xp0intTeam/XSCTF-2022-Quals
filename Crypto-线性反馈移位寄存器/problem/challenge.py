from secret import secret
for b in secret: assert(b == '0' or b == '1')
assert(len(secret) == 128)
# a 01 string with length 128
# your flag is flag{md5(secret).hexdigest()}

def string2bits(s):
    return [int(b) for b in s]

def bits2string(bs):
    s = [str(b) for b in bs]
    return ''.join(s)

def lfsr(state, mask):
    assert(len(state) == 128)
    assert(len(mask)  == 128)

    output = 0
    for i in range(128):
        output = output ^ (state[i] & mask[i])

    return output

if __name__ == '__main__':
    initState = [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
    mask = string2bits(secret)

    for i in range(256):
        state = initState[i:]
        output = lfsr(state, mask)
        initState += [output]

    outputState = bits2string(initState[128:])
    print('outputState =', outputState)
    #
    # outputState = 1010100001001011101000000100100001101011010100101011010101011010100100001110010010110111010111110000000000011011001110100011000111110100110011011011100111000000001100001000001011010011011010110110111100110101001110001001001000001110111011110001111001111111
    #

