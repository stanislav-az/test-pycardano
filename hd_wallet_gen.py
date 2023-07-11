from pycardano import HDWallet

# generate 24-words mnemonic
new_mnemonic = HDWallet.generate_mnemonic()

with open("./user.mnemonic", "w") as f:
    f.write(new_mnemonic)
