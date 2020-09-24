from web3 import Web3

from simple_interface import SimpleContractInterface


ABI = [
    {
        'inputs': [{'internalType': 'address', 'name': 'account', 'type': 'address'}],
        'name': 'balanceOf',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'decimals',
        'outputs': [{'internalType': 'uint8', 'name': '', 'type': 'uint8'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'symbol',
        'outputs': [{'internalType': 'string', 'name': '', 'type': 'string'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [],
        'name': 'totalSupply',
        'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}],
        'stateMutability': 'view', 'type': 'function', 'constant': True
    },
    {
        'inputs': [
            {'internalType': 'address', 'name': 'recipient', 'type': 'address'},
            {'internalType': 'uint256', 'name': 'amount', 'type': 'uint256'}],
        'name': 'transfer',
        'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
        'stateMutability': 'nonpayable', 'type': 'function'
    }
]


w3 = Web3(Web3.HTTPProvider("https://cloudflare-eth.com"))

# Creating the first account, if you don't have one
account = w3.eth.account.create()
print("Addr : %s" % account.address)
print(" PK  : %s" % account.privateKey.hex())  # You can Import this in your Metamask
print("ETH  : %f" % w3.fromWei(w3.eth.getBalance(account.address), "ether"))


dai_token_addr = "0x6B175474E89094C44Da98b954EedeAC495271d0F"  # DAI
contract = SimpleContractInterface(w3, account.privateKey.hex(), dai_token_addr, ABI)

print("DAI  : %s" % contract.call("balanceOf", account.address))

# Dummy Transfer from account to account, but no ETH for gas =/
try:
    receipt = contract.transact("transfer", account.address, 1 * (10**contract.call("decimals")))
except ValueError as e:
    print("ERROR:", e)
