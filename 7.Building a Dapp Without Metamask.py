from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b'
web3 = Web3(Web3.HTTPProvider(infura_url))

account = web3.eth.account.create()
account_address = account.address
print('The address: {}'.format(account_address))
account_privatekey = account.privateKey
print('The private key: {}'.format(web3.toHex(account_privatekey)))

keyVault = account.encrypt('hossein')
print('Account encrypted: {}'.format(keyVault))

#decrypting the account:
decrypted_account = web3.eth.account.decrypt(keyVault, 'hossein')

#now we can use this account to sign our transactions