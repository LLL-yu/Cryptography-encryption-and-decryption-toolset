# 给定参数
p = 473398607161
q = 4511491
e = 19

# 计算欧拉函数φ(n)
phi = (p - 1) * (q - 1)

# 计算d的模逆元（需满足e*d ≡1 mod φ(n)）
d = pow(e, -1, phi)

# 计算flag值
flag = d + 9

print(f"flag{{{flag}}}")
# 给定参数
p = 473398607161
q = 4511491
e = 19

# 计算欧拉函数φ(n)
phi = (p - 1) * (q - 1)

# 计算d的模逆元（需满足e*d ≡1 mod φ(n)）
d = pow(e, -1, phi)

# 计算flag值
flag = d + 1

print(f"flag{{{flag}}}")
