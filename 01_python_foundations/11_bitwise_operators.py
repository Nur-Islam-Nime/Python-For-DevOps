
# *******************************
    #  Bitwise Operators
# *******************************

# Useful in flags or permission bits
x = 0b1100  # 12 in binary
y = 0b1010  # 10 in binary

'''
Bitwise AND (&)
Rule:
1 & 1 = 1
Everything else is 0
'''
print("Bitwise AND:", x & y)   # 1000 (8)

'''
Bitwise OR (|)
Rule:
1 | 0 = 1, 0 | 1 = 1, 1 | 1 = 1
Only 0 | 0 = 0

'''
print("Bitwise OR:", x | y)    # 1110 (14)

'''
Bitwise XOR (^)
Rule:
1 ^ 1 = 0
0 ^ 0 = 0
1 ^ 0 = 1
0 ^ 1 = 1
'''

print("Bitwise XOR:", x ^ y)   # 0110 (6)

'''
Bitwise NOT (~)
Rule:
It inverts the bits:
1 → 0
0 → 1
But Python stores numbers in 2’s complement, so ~x = -(x + 1)

'''

print("Bitwise NOT:", ~x)      # -13
print("Left Shift:", x << 1)   # 11000 (24)
print("Right Shift:", x >> 1)  # 0110 (6)
