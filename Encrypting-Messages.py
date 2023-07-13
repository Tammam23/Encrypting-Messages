from math import *


# The longer the message the better!
def flip_r(mToFlip, jump):
    l = list(mToFlip)
    if jump < round(len(mToFlip) / 3):
        for i in range(1, len(l), jump):
            l[i - 1], l[i] = l[i], l[i - 1]
        return flip_r(l, jump + 2)
    else:
        return ''.join(l)


def invert(mToInvert):
    em = ''
    center = 109.5

    for c in mToInvert:
        im = ord(c)
        d = floor(abs(im - center))
        if im < center:
            iem = im + 2 * d + 1
        else:
            iem = im - 2 * d - 1
        em += chr(iem)
    return em


def in_de_crypt(Message):
    return invert(flip_r(Message, 4))


Message = "-the brown fox jumps over the lazy dog-   0123456789! @Tammam_Alhadwah #Encryption xdxd :)".title()
# uncomment next line to encrypt/decrypt your messages-----------------------------------------------------
# Message = input("Enter encrypted/non-encrypted message: ")
em = in_de_crypt(Message)
print(f'Flipped: "{em}"')
print("----------------------")
print(f'Original: "{in_de_crypt(em)}"')