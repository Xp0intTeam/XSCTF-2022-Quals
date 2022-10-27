import base64
import base92

with open('encode.txt') as f:
    origin_code = f.read()
    round = 0
    #print origin_code
    while True:
        try:
            res = base64.b64decode(origin_code)
            origin_code = res
            round = round + 1
            print round
        except:
            print base92.decode(res)
            break

