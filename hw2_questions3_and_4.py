#input: 8 bit two's complement

def hex_2sComp_to_decimal(hex_val):
    #NOTE: This function is not case sensitive, I just preferred to stick with lower case
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    val_1 = hex_val[2]
    val_2 = hex_val[3]

    dec_val = 0

    for i in range(len(hex_vals)):
        if (val_1.lower() == hex_vals[i]):
            dec_val += 16*i
            break

    for i in range(len(hex_vals)):
        if (val_2.lower() == hex_vals[i]):
            dec_val += i
            break

    if (dec_val < 128):
        comp = ~dec_val + 1
    else:
        comp = 0xFF - dec_val + 1

    return comp

def decimal_to_hex(dec_val):
    #NOTE: This function is not case sensitive, I just preferred to stick with lower case
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

    if(dec_val < 0):
        #handles negative values by converting them to positive equivalent
        hex_val = 0xFF - abs(dec_val) + 1

    val_1 = dec_val // 16
    val_2 = dec_val % 16
    hex_val = "0x" + hex_vals[val_1] + hex_vals[val_2]

    return hex_val


#driver code below
print("\n\nEXAMPLE CONVERSION: ")
print("====================")

hex_val = "0x3c"
print("Hex (2s comp):\t", hex_val)

dec_val = hex_2sComp_to_decimal(hex_val)
print("Decimal:\t", dec_val)

hex_val = decimal_to_hex(dec_val)
print("Hex:\t\t", hex_val)

print("\nAND BACK THE OTHER WAY:")
print("========================")
hex_val = "0xc4"
print("Hex (2s comp):\t", hex_val)

dec_val = hex_2sComp_to_decimal(hex_val)
print("Decimal:\t", dec_val)

hex_val = decimal_to_hex(dec_val)
print("Hex:\t\t", hex_val)


print("\n\n0xFF+0x52+0x0A+0x1E=")

vals = ["0xff", "0x52", "0x0a", "0x1e"]

sum_prob4 = 0

for i in vals:
    sum_prob4 += hex_2sComp_to_decimal(i)

print(sum_prob4)
