value = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"
flag = ""

for char in value:
    at = ord(char);
    if at < 65 or at > 122 or at == 95:
        flag += chr(at);
    else:
        flag += chr(at - 3);

print(flag)