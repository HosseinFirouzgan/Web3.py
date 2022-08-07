from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/d701c5328251487a9d23387a63bccf1b"
my_web3 = Web3(Web3.HTTPProvider(infura_url))
print(my_web3.isConnected())

the_last_block = my_web3.eth.blockNumber
print(the_last_block)
dapp_uni_balance = my_web3.eth.getBalance("0x39C7BC5496f4eaaa1fF75d88E079C22f0519E7b9")
#if we print this it will in Wei 

uni_balance_eth = my_web3.fromWei(dapp_uni_balance, "ether")
print(uni_balance_eth)