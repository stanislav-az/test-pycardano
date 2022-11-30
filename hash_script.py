import cbor2
from pycardano import PlutusV2Script, plutus_script_hash

with open("./mint_script.plutus", "r") as f:
    script_hex = f.read()
    mint_script = cbor2.loads(bytes.fromhex(script_hex))

script_hash = plutus_script_hash(PlutusV2Script(mint_script))
