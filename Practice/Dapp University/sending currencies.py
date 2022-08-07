from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))
#print(web3.isConnected())

sender = '0xE874aa09b5AB43884c4de75000c9C78903A098eC'
reciever = '0x15f3Bc3665D9561fb85Ccb55C57E1c33EF20d6A6'

sender_privateKey = '787c5266ed378b4f1560e77cb982c1ed7ed12ff5f55de2fe7c7cb40a7e3de1cd'

nonce = web3.eth.getTransactionCount(sender)

tx ={
    'nonce': nonce,
    'to': reciever,
    'value': web3.toWei(30, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei(50, 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, sender_privateKey)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
