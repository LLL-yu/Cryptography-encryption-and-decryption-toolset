import hashlib
import itertools

# 目标 MD5 值
target_md5 = "23213b6f905655aaf0510c9054e4b14719d07c2c17c08d826a5f9139d8c234f9"

# 从 "AAAA" 到 "ZZZZ" 的所有组合
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 爆破
for chars in itertools.product(charset, repeat=4):
    pwd = ''.join(chars)
    sha256_hash = hashlib.sha256(pwd.encode()).hexdigest()
    if sha256_hash == target_md5:
        result = pwd
        break
else:
    result = None

print(result)

def xor_decrypt(encrypted_hex, key):
    # 将16进制字符串转换为字节数组
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    
    # 将密钥转换为字节
    key_bytes = bytes(key, 'utf-8')
    
    # 解密：通过循环异或恢复原始数据
    decrypted_bytes = bytearray()
    for i in range(len(encrypted_bytes)):
        decrypted_bytes.append(encrypted_bytes[i] ^ key_bytes[i % len(key_bytes)])
    
    # 将解密后的字节转换回字符串
    decrypted_str = decrypted_bytes.decode('utf-8')
    return decrypted_str

# 示例加密数据与密钥
encrypted_hex = "001844410F285959100B5B312E"
key = "Sherlock"

# 解密
decrypted_result = xor_decrypt(encrypted_hex, key)
print("Decrypted result:", decrypted_result)

def step1(s):
    return s.encode('utf-16le').hex()

def step2(hex_string):
    # Remove padding "00"
    clean = "".join([hex_string[i:i+2] for i in range(0, len(hex_string), 4)])
    print("Clean:", clean)
    sb2_sb = []
    i = 0
    while i < len(clean):
        c1 = clean[i]
        c2 = clean[i+1]
        if i + 4 < len(clean) and clean[i+2:i+4] == '21' and c2 not in '34567':
            sb2_sb.append(c2)
            sb2_sb.append(c1)
            i += 4
        else:
            sb2_sb.append(c1)
            sb2_sb.append(c2)
            i += 2

    sb2_sb = ''.join(sb2_sb)

    # 把 sb2_sb 分开为 sb2 和 sb
    length = len(sb2_sb)
    half = (length // 2)
    sb2 = sb2_sb[:half]
    sb = sb2_sb[half:]
    print('sb2:', sb2)
    print('sb:', sb)
    # 构造原始 str（模拟 for 循环的 sb2 + sb 过程的反向）
    result = []
    i = 0
    i2 = 0
    i3 = 0
    s2_idx = 0
    s_idx = 0
    while i < length:
        i += 1
        if i % 2 == 0:
            # 来自 sb2
            ch = sb2[s2_idx]
            s2_idx += 1
            if (i3 == 1 or (i3 - 1) % 3 == 0) and ch == '3':
                result.append('0')
            else:
                result.append(ch)
            i3 += 1
        else:
            if s_idx >=  len(sb):
                break
            # 来自 sb
            ch = sb[s_idx]
            s_idx += 1
            if (i2 == 0 or i2 % 3 == 0) and ch == '3':
                result.append('0')
            else:
                result.append(ch)
            i2 += 1

    return ''.join(result)

def encrypt(s):
    i,i2,i3 = 0,0,0
    sb,sb2,sb3 = [],[],[]
    while i < len(s):
        ch = s[i]
        i += 1
        if i % 2 == 0:
            if ((i3==1 or (i3-1)%3==0) and ch=='0'):
                sb2.append('3')
            else:
                sb2.append(ch)
            i3 += 1
        else:
            if ((i2==0 or i2%3==0) and ch=='0'):
                sb.append('3')
            else:
                sb.append(ch)
            i2 += 1
    print(sb)
    print(sb2)
    for i in sb:
        sb2.append(i)
    # print(sb2)
    
    for i in range(0,len(sb2),2):
        ch1 = sb2[i]
        ch2 = sb2[i+1]
        if (ch1 not in '34567'):
            sb3.append(ch2)
            sb3.append(ch1)
            sb3.append("2")
            sb3.append("1")
        else:
            sb3.append(ch1)
            sb3.append(ch2)
        # print(f"step {i} :",sb3,f"ch1 : {ch1}",f"ch2 : {ch2}")
    return "".join(sb3)

# print(encrypt("061062063064065066067068"))
result = step2(step1(decrypted_result))
# result = step2("63006200210034006300660038003100630036003500630076")
print(result)
for i in range(0,len(result),3):
    ch = result[i:i+3]
    print(chr(int(ch,16)),end='')