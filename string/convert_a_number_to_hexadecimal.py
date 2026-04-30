dec_to_hex = {
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}
output = []
switch = False
if num < 0:
    switch = True
while num > 16:
    temp = num % 16
    if temp in dec_to_hex.keys():
        output.append(dec_to_hex[temp])
    else:
        output.append(temp)
    num = num // 16

temp = num % 16
if temp in dec_to_hex.keys():
    output.append(dec_to_hex[temp])
else:
    output.append(temp)
return output[::-1]
    
