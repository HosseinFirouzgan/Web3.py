from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b'
web3 = Web3(Web3.HTTPProvider(infura_url))

#print(web3.isConnected())
latest_block = web3.eth.blockNumber
#print(latest_block)
#print('=====================================\n===================================\n======================')
#print(web3.eth.getBlock(latest_block))
#print('=====================================\n===================================\n======================')
#print(web3.eth.getBlock(latest_block - 50))

block_hash = '0xabc60ae92a1d616950a46b1706056b9121680f603784e4d536145af1b32797c4'
print(web3.eth.getTransactionByBlock(block_hash, 70))
