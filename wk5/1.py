import random as rd
import math
from binascii import hexlify, unhexlify

def gcd(a,b):
    """ Calculate the biggest common divisor """
    a,b = (b,a) if a < b else (a,b)
    while b:
        a,b = b,a % b
    return a

def egcd(a, b):
    """ http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b //a) * y, y)

def modinv(a, m):
    """ http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm """
    g, x, y = egcd(a, m)
    assert g == 1
    return x % m

def rsa_keygen(p, q):
    """ Generate public and private key for RSA encryption """
    n = p * q
    totient = (p - 1) * (q - 1)

    # Generate encryption key (public) with 1 < e < totient.
    for i in range(100, totient - 1):
        if (gcd(i, totient) == 1):
            e = i
            break

    # Generate the decryption (private) key from the public key.
    d = modinv(e, totient)

    # Return (e)ncryption en (d)ecryption keys together with the max length
    # of a chunk (n)
    return e, d, n

def encrypt(msg, pubkey, n):
    """ Encrypt a message using hex representation of a string. """

    # Calculate chunk size and correct for 0 indexed.
    chunksize = int(math.log(n, 256))
    outchunk = chunksize + 1
    outformat = '%%0%dx' % (outchunk * 2,)

    # Encode in utf-8 to make sure ascii values can fit in a single byte.
    bmsg = msg.encode('utf-8')
    result = []

    # Encrypt each chunk one by one.
    for start in range(0, len(bmsg), chunksize):

        # Fetch chunk
        chunk = bmsg[start:start + chunksize]

        # Prepend leading zero to get equally sized chunks
        chunk += b'\x00' * (chunksize - len(chunk))

        # Encode in hex representation
        plain = int(hexlify(chunk), 16)
        coded = pow(plain, pubkey, n)
        bcoded = unhexlify((outformat % coded).encode())

        result.append(bcoded)
    return b''.join(result)

def decrypt(bcipher, privkey, n):
    """ Decrypt a message using hex representation of a string. """

    # Calculate chunk size and correct for 0 indexed.
    chunksize = int(math.log(n, 256))
    outchunk = chunksize + 1
    outformat = '%%0%dx' % (chunksize * 2,)

    result = []

    # Decrypt each chunk one by one.
    for start in range(0, len(bcipher), outchunk):

        # Fetch chunk
        bcoded = bcipher[start: start + outchunk]

        # Decode in hex representation
        coded = int(hexlify(bcoded), 16)
        plain = pow(coded, privkey, n)
        chunk = unhexlify((outformat % plain).encode())
        result.append(chunk)

    # Remove all prepended zeros and decode from utf-8
    return b''.join(result).rstrip(b'\x00').decode('utf-8')

if __name__ == '__main__':
    p = 9929952359
    q = 9929953373
    e, d, n = rsa_keygen(p, q)
    encrypted = encrypt("Hello World", e, n)
    decrypted = decrypt(encrypted, d, n)
    print(decrypted)
