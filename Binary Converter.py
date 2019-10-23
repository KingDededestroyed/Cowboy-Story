binaryName = """010100110110010101110100
             0110100000010000001001010
             0110111101101110011001010111011"""
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
print(decode_binary_string(binaryName))
