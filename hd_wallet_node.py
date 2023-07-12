from pycardano import (
    HDWallet,
    PaymentVerificationKey,
    Address,
    ExtendedSigningKey,
    Network,
)

with open("./node.mnemonic", "r") as f:
    MNEMONIC_24: str = f.read()

network = Network.TESTNET

hd_wallet = HDWallet.from_mnemonic(MNEMONIC_24)

hd_wallet_spend = hd_wallet.derive_from_path("m/1852'/1815'/0'/0/0")
spend_public_key = hd_wallet_spend.public_key
spend_vk = PaymentVerificationKey.from_primitive(spend_public_key)
node_pub_key_hash = spend_vk.hash()

extended_signing_key = ExtendedSigningKey.from_hdwallet(hd_wallet_spend)
node_addr = Address(node_pub_key_hash, network=network)

print(node_addr)
print(node_pub_key_hash)
