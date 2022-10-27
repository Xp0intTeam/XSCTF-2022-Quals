from pycipher import Caesar

class Bacon:
    TABLE = {'A':'AAAAA', 'B':'AAAAB', 'C':'AAABA', 'D':'AAABB', 'E':'AABAA', 'F':'AABAB', 'G':'AABBA', 'H':'AABBB', 'I':'ABAAA', 'J':'ABAAB', 'K':'ABABA', 'L':'ABABB', 'M':'ABBAA', 'N':'ABBAB', 'O':'ABBBA', 'P':'ABBBB', 'Q':'BAAAA', 'R':'BAAAB', 'S':'BAABA', 'T':'BAABB', 'U':'BABAA', 'V':'BABAB', 'W':'BABBA', 'X':'BABBB', 'Y':'BBAAA', 'Z':'BBAAB'}
    string = ""

    def __init__(self, _str):
        self.string = _str.upper()

    def enc(self):
        rslt = ""
        for x in self.string:
            if x not in self.TABLE.keys():
                raise ValueError
            rslt += self.TABLE[x]
        return rslt

    def dec(self):
        rslt = ""
        key_list = list(self.TABLE.keys())
        val_list = list(self.TABLE.values())
        if len(self.string) % 5 != 0:
            raise ValueError
        s = [self.string[i:i+5] for i in range(0, len(self.string), 5)]
        for x in s:
            rslt += key_list[val_list.index(x)]
        return rslt

s = "ABBABAABBAAAAABABABAABABBAAAAABAABBAAABAABBBABBAABABBABABAAABABBBAABAABABABBBAABBABAA"
# 培根密码
flag = Bacon(s).dec()
# 凯撒密码爆破
for i in range(26):
    print(i, Caesar(key=i).decipher(flag))