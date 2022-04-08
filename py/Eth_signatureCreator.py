from flask import Flask, jsonify, request
import bitcoin, hashlib, binascii, base58
import eth_keys, eth_utils, binascii, os
import json

privKey = eth_keys.keys.PrivateKey(binascii.unhexlify('97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
pubKey = privKey.public_key
pubKeyCompressed = '0' + str(2 + int(pubKey) % 2) + str(pubKey)[2:66]
address = pubKey.to_checksum_address()
msg = b'exercise-cryptography' 
msgHash = eth_utils.keccak(msg)
signature = privKey.sign_msg(msg)

print('Signature:', signature)
print('Message:', msg)
