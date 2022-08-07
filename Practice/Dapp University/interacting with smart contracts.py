from web3 import Web3
import json

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

address = web3.toChecksumAddress('0x2E4E580a86CE0F7375d244d4d13037d267378C45')
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
contract = web3.eth.contract(address=address, abi=abi)

#print(web3.isConnected())
web3.eth.defaultAccount = web3.eth.accounts[0]

print(contract.functions.greet().call())
tx_hash = contract.functions.setGreeting('This is great!').transact()

web3.eth.waitForTransactionReceipt(tx_hash)

print('Update successful\nThis is the transaction hash {}\nThe new greeting is: {}'.format(web3.toHex(tx_hash), contract.functions.greet().call()))