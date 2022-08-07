from web3 import Web3
import json

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

address = web3.toChecksumAddress('0x1cF740C91e630befdc11aF3fe4B0a6A0c81aA7c0')
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
contract = web3.eth.contract(address=address, abi=abi)
web3.eth.defaultAccount = web3.eth.accounts[0]
#print(web3.isConnected())
print(contract.functions.greet().call())
tx_hash = contract.functions.setGreeting('Yo Yo cool!').transact()
web3.eth.waitForTransactionReceipt(tx_hash)
print('Update successful\nNew greeting: {}\nTreansaction hash: {}'.format(
    contract.functions.greet().call(), web3.toHex(tx_hash)
))