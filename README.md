# geth_net

ACCOUNTS :

0xA063A1b332aD5f069926703c284DF6A935f641AD
0x20f95e59b28fe3e9e52974156e6fAAD9a2194c97
0x381af0A41B0a78a4EC95323e9f3038bEc9ad5Ebb

NETWORK : 

network Chain ID : 89654


NODE 1:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30350 --miner.gasprice 0 --miner.gastarget 470000000000 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0xA063A1b332aD5f069926703c284DF6A935f641AD" --password password.txt

enode://b712d85f5f89272699e102f71eaf41df9426242798fb16d5071340490479f6b04f24299409f0aae2dd46108c6f0c011ec093adfb90ee66504a56d5540c3611ba@127.0.0.1:30350

NODE 2:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30351 --miner.gasprice 0 --miner.gastarget 470000000000 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0x20f95e59b28fe3e9e52974156e6fAAD9a2194c97" --password password.txt

enode://a2dd81faad4d984a407cc0e601ec069ab78d8bf4352239e1fbdad672451527c986c7d7cc7def4f2d25385df48fd845742c3f02c92aa5c481245cb4b3b9f3e806@127.0.0.1:30351

NODE 3:

geth --nousb --datadir=$pwd --syncmode 'full' --port 30352 --miner.gasprice 0 --miner.gastarget 470000000000 --http --http.addr 'localhost' --http.port 8545 --http.api admin,eth,miner,net,txpool,personal,web3 --mine --allow-insecure-unlock --unlock "0x381af0A41B0a78a4EC95323e9f3038bEc9ad5Ebb" --password password.txt

enode://98b7772f3f8b9f5e92c063c990f6593308a2cbe6e8b30fd1444efb46174a0ab6823c7730240482cdff59fb8dd304bd974ff08fce4e7e618fe4dbb49ef4ae6b96@127.0.0.1:30352