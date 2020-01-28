#input: 8 bit two's complement

def hex_to_decimal(hex_val):

    dec_val = int(hex_val, 16)
    comp = ~dec_val + 1

    return comp

def decimal_to_hex(dec_val, nBits):

    hex_val = hex((dec_val + (1 << nBits)) % (1 << nBits))


    return hex_val


print("EXAMPLE CONVERSION: ")

hex_val = "0x1C"
print("Hex (2s comp):\t", hex_val)

dec_val = hex_to_decimal(hex_val)
print("Decimal:\t", dec_val)


hex_val = decimal_to_hex(dec_val, 8)
print("Hex (again):\t", hex_val)

print("\n\n0xFF+0x52+0x0A+0x1E=")

vals = ["0xFF", "0x52", "0x0A", "0x1E"]

sum_2s_comp = 0
sum_normal = 0
for i in vals:
    sum_2s_comp += hex_to_decimal(i)
    sum_normal += int(i, 16)

print(sum_2s_comp, "\t(assuming two's complement)")
print(sum_normal, "\t(not assuming two's complement)")


#print('i', twos_comp(-100, 8))
