from flask import Flask, jsonify, request
import bitcoin, hashlib, binascii, base58
import eth_keys, eth_utils, binascii, os
import json

app =Flask(__name__)
@app.route('/crypto2/eth_sign', methods=["POST"])
def eth_sign():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["skey", "msg"]
    if not all(k in values for k in required):
        return "Missing values", 400

    privKey = eth_keys.keys.PrivateKey(binascii.unhexlify('97ddae0f3a25b92268175400149d65d6887b9cefaf28ea2c078e05cdc15a3c0a'))
    pubKey = privKey.public_key
    pubKeyCompressed = '0' + str(2 + int(pubKey) % 2) + str(pubKey)[2:66]
    address = pubKey.to_checksum_address()
    msg = b'Message for signing' 
    msgHash = eth_utils.keccak(msg)
    signature = privKey.sign_msg(msg)

    response = {"signature": (signature)}

    y = json.dumps(response)

    return y, 201





        

@app.route('/crypto2/eth_sign_to_addr', methods=["POST"])
def eth_sign_to_addr():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["signature", "msg"]
    if not all(k in values for k in required):
        return "Missing values", 400

    # TODO: Not Implemented Yet
	
    response = {"address": "TODO"}

    return json.dumps(response), 201

@app.route('/crypto2/eth_sign_verify', methods=["POST"])
def eth_sign_verify():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["address", "signature", "msg"]
    if not all(k in values for k in required):
        return "Missing values", 400

    # TODO: Not Implemented Yet
	
    response = {"valid": "TODO"}
	
    return json.dumps(response), 201

@app.route('/crypto2/btc_skey_to_addr', methods=["POST"])
def btc_skey_to_addr():
    values = request.get_json()
    if not values:
        return "Missing body", 400

    required = ["skey"]
    if not all(k in values for k in required):
        return "Missing values", 400

#def private_key_to_public_key(privKeyHex: str):
        #privateKey = int(privKeyHex, 16)
        #return bitcoin.fast_multiply(bitcoin.G, privateKey)

#def pubkey_to_address(pubKey: str, magic_byte = 0) -> str:
    #pubKeyBytes = binascii.unhexlify(pubKey)
    #sha256val = hashlib.sha256(pubKeyBytes).digest()
    #ripemd160val = hashlib.new('ripemd160', sha256val).digest()
    #return bitcoin.bin_to_b58check(ripemd160val, magic_byte)

    private_key = bitcoin.random_key()
    print("Private key (hex):", private_key) 

    public_key = private_key_to_public_key(private_key)
    print("Public key (x,y) coordinates:", public_key)

    compressed_public_key = bitcoin.compress(public_key)
    print("Public key (hex compressed):", compressed_public_key)

    address = pubkey_to_address(compressed_public_key)
    print("Compressed Bitcoin adress (base58check):", address)

    response = {"address": (address) }
    return json.dumps(response), 201
        
   
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

