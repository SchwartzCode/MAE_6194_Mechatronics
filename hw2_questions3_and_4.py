#input: 8 bit two's complement

def hex_2sComp_to_decimal(hex_val):
    
    if (int(hex_val, 16) < 128):
        dec_val = int(hex_val, 16)
        comp = ~dec_val + 1
    else:
        comp = 0xFF - int(hex_val, 16) + 1
        
    #print("Hex in:\t", hex_val, "comp:\t", comp) #debugging
    return comp

def decimal_to_hex(dec_val, nBits):

    hex_val = hex((dec_val + (1 << nBits)) % (1 << nBits))

    #print("~~ Dec:\t", dec_val, "Hex:\t", hex_val) #debugging
    return hex_val

print("\n\nEXAMPLE CONVERSION: ")
print("====================")

hex_val = "0x3c"
print("Hex (2s comp):\t", hex_val)

dec_val = hex_2sComp_to_decimal(hex_val)
print("Decimal:\t", dec_val)

hex_val = decimal_to_hex(dec_val, 8)
print("Hex:\t\t", hex_val)

print("\nAND BACK THE OTHER WAY:")
print("========================")
hex_val = "0xc4"
print("Hex (2s comp):\t", hex_val)

dec_val = hex_2sComp_to_decimal(hex_val)
print("Decimal:\t", dec_val)

hex_val = decimal_to_hex(dec_val, 8)
print("Hex:\t\t", hex_val)


print("\n\n0xFF+0x52+0x0A+0x1E=")

vals = ["0xFF", "0x52", "0x0A", "0x1E"]

sum_prob4 = 0

for i in vals:
    sum_prob4 += hex_2sComp_to_decimal(i)

print(sum_prob4)

