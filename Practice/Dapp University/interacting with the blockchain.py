from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b'
web3 = Web3(Web3.HTTPProvider(infura_url))

latest_block = web3.eth.blockNumber
print(latest_block)
print('======================================================================')
print(web3.eth.getBlock(latest_block))

print('=======================\n======================\n=======================')

block_hash = '0x0e735dd6d5bada767996a899046d74f0799f374a7c40a4cff9d634620688d66b'
print(web3.eth.getTransactionByBlock(block_hash))