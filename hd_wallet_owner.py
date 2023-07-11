from pycardano import HDWallet, PaymentVerificationKey, Address, ExtendedSigningKey, Network

with open("./owner.mnemonic", "r") as f:
    MNEMONIC_24: str = f.read()

network = Network.TESTNET

hd_wallet = HDWallet.from_mnemonic(MNEMONIC_24)

hd_wallet_spend = hd_wallet.derive_from_path("m/1852'/1815'/0'/0/0")
spend_public_key = hd_wallet_spend.public_key
spend_vk = PaymentVerificationKey.from_primitive(spend_public_key)

hd_wallet_stake = hd_wallet.derive_from_path("m/1852'/1815'/0'/2/0")
stake_public_key = hd_wallet_stake.public_key
stake_vk = PaymentVerificationKey.from_primitive(stake_public_key)

extended_signing_key = ExtendedSigningKey.from_hdwallet(hd_wallet_spend)
owner_addr = Address(spend_vk.hash(), stake_vk.hash(), network)

print(owner_addr)
