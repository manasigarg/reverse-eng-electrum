
from okanelabs.crypt.btc.serialize.base58 import Base58
from okanelabs.crypt.core.hash.sha256 import SHA256
import binascii

# 1 - Take a private key
raw = 82295637717710356959985575716131249482690360273799844241244085665208347300813
raw_hex = str(hex(raw)).replace("0x","")
print(raw_hex)

# 2 - Add a 0x80 byte in front of it for mainnet addresses or 0xef for testnet addresses. Also add a 0x01 byte at the end if the private key will correspond to a compressed public key
prefixed_raw = "ef{}".format(raw_hex)
print(prefixed_raw)

# 3 - Perform SHA-256 hash on the extended key
prefixed_bytes = binascii.unhexlify(prefixed_raw)
hash_1 = SHA256(prefixed_bytes)

# 4 - Perform SHA-256 hash on result of SHA-256 has
hash_2 = SHA256(hash_1)
hash_2_hex = str(binascii.hexlify(hash_2)).replace("b'","").replace("'","")
print(hash_2_hex)

# 5 - Take the first 4 bytes of the second SHA-256 hash, this is the checksum
checksum = str(binascii.hexlify(hash_2[0:4])).replace("b'","").replace("'","")
print(checksum)

# 6 - Add the 4 checksum bytes from point 5 at the end of the extended key from point 2
checksum_address = "{}{}".format(prefixed_raw, checksum)
print(checksum_address)

# 7 - Convert the result from a byte string into a base58 string using Base58Check encoding. This is the Wallet Import Format
checksum_address_bytes = binascii.unhexlify(checksum_address)
base58check = Base58.encode_bytes(checksum_address_bytes)
print(base58check)