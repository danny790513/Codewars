# Instructions
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


# My solution
def rgb(r, g, b):
    def scale(n):
        if n not in range(0, 256):
            return 0 if n < 0 else 255
        return n
    return '{:02X}{:02X}{:02X}'.format(scale(r), scale(g), scale(b))


# Clever solution
# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# Clever solution
# def rgb(*args):
#     return ''.join(map(lambda x: '{:02X}'.format(min(max(0, x), 255)), args));
