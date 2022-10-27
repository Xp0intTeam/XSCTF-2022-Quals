import base92
import base64

true_flag = "flag{d0_y0u_l1ke_base92_!??!_by_Sh3n}"
flag = base92.encode(true_flag)
#print (base92.encode(true_flag))

for i in range(20):
    f = base64.b64encode(flag)
    flag = f
with open("encode.txt",'w') as f:
    f.write(flag)
