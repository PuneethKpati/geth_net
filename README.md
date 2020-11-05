# geth_net

ACCOUNTS :

0xA063A1b332aD5f069926703c284DF6A935f641AD
0x20f95e59b28fe3e9e52974156e6fAAD9a2194c97
0x381af0A41B0a78a4EC95323e9f3038bEc9ad5Ebb

NETWORK : 

network Chain ID : 89654


NODE 1:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30350 --miner.gasprice 0 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0xA063A1b332aD5f069926703c284DF6A935f641AD" --password password.txt


NODE 2:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30351 --miner.gasprice 0 --miner.gastarget 470000000000 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0x20f95e59b28fe3e9e52974156e6fAAD9a2194c97" --password password.txt


NODE 3:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30352 --miner.gasprice 0 --miner.gastarget 470000000000 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0x381af0A41B0a78a4EC95323e9f3038bEc9ad5Ebb" --password password.txt