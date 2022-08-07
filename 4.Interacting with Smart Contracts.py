from matplotlib.colors import to_hex
from web3 import Web3
import json

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

address = web3.toChecksumAddress('0x2761327ca657Dc89a1aA7d4Eea6cE7AFD605eB58')
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
contract = web3.eth.contract(address=address, abi=abi)

#we need to set a default account so that we can send the smart contract from that account
web3.eth.defaultAccount = web3.eth.accounts[0]

print(contract.functions.greet().call())
tx_hash = contract.functions.setGreeting('This is awesome!').transact()

#a contract does not take place instantly on the blockchain and it goes through a process 
#after the process is done a reciept is created and we can check for it to make sure the process is done
web3.eth.waitForTransactionReceipt(tx_hash)
print(web3.toHex(tx_hash))
print('update complete\nNew greeting: {}'.format(contract.functions.greet().call()))