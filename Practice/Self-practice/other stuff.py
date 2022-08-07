from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b'
web3 = Web3(Web3.HTTPProvider(infura_url))
#print(web3.isConnected())

example_block = web3.eth.get_block(14848356)
example_block_hash = example_block['hash']
#print(web3.toHex(example_block_hash))
latest_block = web3.eth.get_block('latest')
#print('This the info of the latest block :\n\n{}'.format(latest_block))

top_holder = web3.toChecksumAddress('0x00000000219ab540356cBB839Cbe05303d7705Fa')
top_holder_balance = web3.eth.get_balance(top_holder)
#print(web3.fromWei(top_holder_balance, 'ether'))

random_TxHash = '0x738627898f5e92b8efc7f0e9be1094fe95b57beb21773566a393b22715635395'
print(web3.eth.get_transaction(random_TxHash))