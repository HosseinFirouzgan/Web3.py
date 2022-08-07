from web3 import Web3
import json


infura_url = "https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b"
web3 = Web3(Web3.HTTPProvider(infura_url))

abi = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"transferAndCall","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_subtractedValue","type":"uint256"}],"name":"decreaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_addedValue","type":"uint256"}],"name":"increaseApproval","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"},{"indexed":false,"name":"data","type":"bytes"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]')
address = '0x514910771AF9Ca656af840dff83E8264EcF986CA'
contract = web3.eth.contract(abi=abi, address=address)

name = contract.functions.name().call()
symbol = contract.functions.symbol().call()
total_supply = contract.functions.totalSupply().call()
print("The name of the token is {}, The symbol is {} and the total supply is {} ".format(name, symbol,web3.fromWei(total_supply, 'ether')))

#top three holders
first_address = web3.toChecksumAddress('0x98c63b7b319dfbdf3d811530f2ab9dfe4983af9d')
first_holder = contract.functions.balanceOf(first_address).call()
second_address = web3.toChecksumAddress('0x75398564ce69b7498da10a11ab06fd8ff549001c')
second_holder = contract.functions.balanceOf(second_address).call()
#we found the checksummed address for third holder
third_holder = contract.functions.balanceOf('0x75398564ce69B7498dA10a11ab06Fd8fF549001c').call()

print('You can see the balances of the top three holders')
print('The balance of the top holder is {} '.format(web3.fromWei(first_holder, 'ether')))
print('The balance of the second holder is {} '.format(web3.fromWei(second_holder, 'ether')))
print('The balance of the third holder is {} '.format(web3.fromWei(third_holder, 'ether')))
