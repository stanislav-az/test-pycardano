from pycardano import (
    HDWallet,
    PaymentVerificationKey,
    VerificationKey,
    Address,
    ExtendedSigningKey,
    Network,
)

with open("./node.mnemonic", "r") as f:
    MNEMONIC_24: str = f.read()

network = Network.TESTNET

hd_wallet = HDWallet.from_mnemonic(MNEMONIC_24)

# Generate node keys (for signing oracle feed)
# using purpose 4343 (m / purpose' / coin_type' / account' / role / index)
node_hdwallet = hd_wallet.derive_from_path("m/4343'/1815'/0'/0/0")
node_feed_sk = ExtendedSigningKey.from_hdwallet(node_hdwallet)
node_feed_vk: VerificationKey = VerificationKey.from_primitive(
    node_hdwallet.public_key[:32]
)
print(f"node feed vk cbor hex: {node_feed_vk.to_cbor_hex()}")
node_feed_vkh = node_feed_vk.hash()
print(f"node feed vkh: {node_feed_vkh.payload.hex()}")

# Generate payment keys (for funds management)
payment_hdwallet = hd_wallet.derive_from_path("m/1852'/1815'/0'/0/0")
node_payment_sk = ExtendedSigningKey.from_hdwallet(payment_hdwallet)
node_payment_vk = PaymentVerificationKey.from_primitive(
    payment_hdwallet.public_key[:32]
)
node_payment_vkh = node_payment_vk.hash()
print(f"node payment vkh: {node_payment_vkh.payload.hex()}")
node_addr = Address(node_payment_vkh, network=network)
print(node_addr)
