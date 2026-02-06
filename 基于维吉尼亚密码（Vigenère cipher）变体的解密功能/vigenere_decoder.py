def decode(encrypted_str, key_str):
    # 将密钥字符串转换为字节偏移量（相对于'a'）
    key_bytes = [ord(c) - ord('a') for c in key_str]
    key_length = len(key_bytes)

    # 初始化结果字符列表
    decoded_chars = []

    # 遍历加密字符串的每个字符
    for i, char in enumerate(encrypted_str):
        if char == '_' or char == '{' or char == '}':
            # 特殊字符直接添加到结果列表中
            decoded_chars.append(char)
        elif 'a' <= char <= 'z':
            # 解密逻辑
            offset = key_bytes[i % key_length]
            original_char = chr(((ord(char) - ord('a') - offset) % 26) + ord('a'))
            decoded_chars.append(original_char)
        else:
            # 如果遇到非小写字母且非特殊字符，则可能表示加密过程被中断了
            # 这里我们简单地忽略它，或者可以抛出一个异常
            pass

            # 将结果列表转换为字符串
    decoded_str = ''.join(decoded_chars)

    # 注意：这里我们没有“预期结果”来比较，因为解码的目的是还原原始字符串
    # 所以我们直接返回解码后的字符串
    return decoded_str


# 示例
key_str = "aptxcony"  # 替换为你的密钥字符串
encrypted_str = "fatd{sm_cgrmvc_ylvhokhuk_gxsgffc_wtec}"  # 替换为加密后的字符串

# 调用解码函数并打印结果
decoded_str = decode(encrypted_str, key_str)
print(decoded_str)  # 这将打印出解码后的原始字符串（如果加密过程没有中断的话）
