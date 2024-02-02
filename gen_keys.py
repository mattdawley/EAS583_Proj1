from web3 import Web3
import eth_account
import os

def get_keys(challenge,keyId = 0, filename = "eth_mnemonic.txt"):
    """
    Generate a stable private key
    challenge - byte string
    keyId (integer) - which key to use
    filename - filename to read and store mnemonics

    Each mnemonic is stored on a separate line
    If fewer than (keyId+1) mnemonics have been generated, generate a new one and return that
    """

    private_key = "46e2623ed463a8523bbc9aea7c1e732fe9768ae9d1c4b5026fc7196252055a42"
    wallet_address = "0x99ECb0aBBa20B98Cf096496841241ed5e8a90883"

    w3 = Web3()
    w3.eth.default_account = wallet_address
    eth_addr = w3.eth.account.from_key(private_key)

    msg = eth_account.messages.encode_defunct(challenge)
    sig = eth_addr.sign_message(msg, private_key)

    assert eth_account.Account.recover_message(msg,signature=sig.signature.hex()) == eth_addr, f"Failed to sign message properly"

    #return sig, acct #acct contains the private key
    return sig, eth_addr

if __name__ == "__main__":
    for i in range(4):
        challenge = os.urandom(64)
        sig, addr= get_keys(challenge=challenge,keyId=i)
        print( addr )
