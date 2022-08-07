from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# print(web3.isConnected())
# print(web3.eth.blockNumber)

sender = '0x5076E5c71Ba34F981B46D4870780fE0eafaB33ec'
reciever = '0x5ABFeDB1274E539551EDef4d535F80ca29cCB883'
senderPrivateKey = 'ebd3a2fb7c75b9330fdbb63e9d6bb52476c008e6e2dd7b6b41892f36f585bc4d'
nonce = web3.eth.getTransactionCount(sender)
tx = {
    'nonce': nonce,
    'to': reciever,
    'value': web3.toWei(90, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei')
}
signed_tx = web3.eth.account.signTransaction(tx, senderPrivateKey)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print('Successful\nHere is your transaction hash:\n{}'.format(web3.toHex(tx_hash)))