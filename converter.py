def decimal_to_binary(n):
    return bin(n)[2:]


def binary_to_decimal(binary):
    if not all(c in '01' for c in binary):
        return None
    return int(binary, 2)


def decimal_to_hex(n):
    return hex(n)[2:].upper()


def hex_to_decimal(h):
    try:
        return int(h, 16)
    except:
        return None


def binary_to_hex(binary):
    if not all(c in '01' for c in binary):
        return None
    return hex(int(binary, 2))[2:].upper()


def hex_to_binary(h):
    try:
        return bin(int(h, 16))[2:]
    except:
        return None