I create this tool because one of friends told me he missed a word when he tries to write the seed phrase on his notebook.

You know blockchain is known to be secure from protecting your assets, but it is a disaster if you dont remember your secret phrase.

However, in some cases, if you only miss one word, it is still able to find it back. Probably 2 words are also possible, but i am creating a simple brute force solution to crack the all the possibilities if one word is missing. 

This is a useful tool to crack blockchain seed phrase under bip-39 standard on solana network without the need to show your seed phrase to some online 3rd party tool. 
The purpose of this tool is to find the seed phrase if one of word is missing from seed phrase.

Replace phrase variable to your seed phrase.
Run the ptest.py in cmd but not pycharm with entire python environment installed.
It will call solana api to see if it is valid seed phrase or not. This will generate all the valid seed phrase which could possibly contain
your valid one.

if it is valid , then it will output the public key to file called logfile.txt, put the valid seed phrase to answers.txt

then we call createJSON.py to generate JSON file containing a list of JSON file with the public addresses provided.
With the JSON  provided, we can run solana_wallet_balance.py to read the JSON file and output excel file with balance each address provided.

STEPS for environment of running solana_token_balance.py





This script fetches the balance of a specified Solana token for all addresses listed in a JSON file. It supports checking the native SOL balance as well as SPL token balances.

Requirements
Python 3.6+, Windows environment
This script cannot run on a virtual environment like pycharm. A full installed python environment is mandatory for python wexpect to run on the windows.
Setup
Clone the repository and navigate to the project directory.

Create a .env file with the following content:

RPC_URL=https://api.mainnet-beta.solana.com
TOKEN_CONTRACT=B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391
Replace the RPC_URL and TOKEN_CONTRACT values with your own. For tracking the native SOL balance, set TOKEN_CONTRACT to 0x0.

Create a solana_wallet.json file with the following content:

[
  {
    "isConnected": true,
    "address": "DHAzXyqVFqw31qX6Jhvm8o6QPBKy67dAYRjMiVMuG4tm",
    "balance": null,
    "isDisabled": false,
    "type": "SOL",
    "phrase": "-=--=-=-=-",
    "label": null,
    "ens": null,
    "group": ["Personal Group"]
  }
]
You can also generate a sample JSON file using the Makefile:

make example
Usage
To install dependencies and run the script:

make all
To install dependencies only:

make setup
To run the script only:

make run
To clean up generated Excel files:

make clean
To create a sample solana_wallet.json file:

make example
To display help information:

make help
Tracking Native SOL Token
To track the native SOL balance, set the TOKEN_CONTRACT variable in your .env file to 0x0:

RPC_URL=https://api.mainnet-beta.solana.com
TOKEN_CONTRACT=0x0
This will make the script query the native SOL balance for the given wallet addresses.

Tracking SPL Tokens
To track an SPL token balance, set the TOKEN_CONTRACT variable in your .env file to the mint address of the SPL token:

RPC_URL=https://api.mainnet-beta.solana.com
TOKEN_CONTRACT=B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391
Replace B6h248NJkAcBAkaCnji889a26tCiGXGN8cxhEJ4dX391 with the mint address of your desired SPL token.

Output
The script will save the wallet balances to an Excel file named solana_<TOKEN_CONTRACT>.xlsx.

