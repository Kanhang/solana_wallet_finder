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