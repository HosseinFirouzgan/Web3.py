from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

#print(web3.isConnected())

sender = '0x15f3Bc3665D9561fb85Ccb55C57E1c33EF20d6A6'
reciever = '0x21E9856E393E32B51ACe57ed7909A0AEc7cdb918'

sender_private_key = '959e5cf714596bbcdb79972b3876559595200a5a7c4863774eebd860ff3b1e4f'

#get the nonce
nonce = web3.eth.getTransactionCount(sender)

#build the transaction
transaction = {
    'nonce': nonce,
    'to': reciever,
    'value': web3.toWei(5, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

#sign the transaction
signed_transaction = web3.eth.account.signTransaction(transaction, sender_private_key)

#send the transaction(which will return a hash)
transaction_hash = web3.eth.sendRawTransaction(signed_transaction.rawTransaction)

#get the transaction's hash
print(web3.toHex(transaction_hash))