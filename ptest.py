
import wexpect
import sys
import time
#input 11 words phrase
phrase = 'police mind bunker stock hub milk rose present depend truly body'
cmd = 'solana-keygen pubkey prompt://'

def iterateWordsList():
    with open('wordslist.txt') as f:
        lines = f.readlines()
    for x in range(0, 12):
        for line in lines:
            print(line.strip())
            automate_cli(line.strip(), x)
            time.sleep(1)

def automate_cli(word, index):
    # Replace 'your_command' with the command-line program you want to interact with
    program = wexpect.spawn(cmd, encoding='utf-8', use_pty=True)
    program.logfile = sys.stdout
    # Set up expected prompts and responses
    seedPrompt = "[pubkey recovery] seed phrase: "
    errorPrompt = "Error: Can't get mnemonic from seed phrases"
    successPrompt = "[pubkey recovery] If this seed phrase has an associated passphrase, enter it now. Otherwise, press ENTER to continue: "
    newLine = '\n'
    phrase_arr = phrase.split()
    phrase_arr.insert(index, word)
    seedphrase = ' '.join(phrase_arr) + newLine
    print (seedphrase)
    try:
        program.expect_exact(seedPrompt)  # Wait for the specific prompt
        program.sendline(seedphrase)  # Send the response
        i = program.expect_exact([errorPrompt, successPrompt])
        if i == 0:
            print ('error')
            program.expect(wexpect.EOF)  # Wait for the program to complete
        elif i == 1:
            f = open("answer.txt", "a")
            LOG_FILE = open("logfile.txt", "a")
            f.write(seedphrase)
            f.close()
            program.sendline('\n')
            program.expect(wexpect.EOF)
            public_key = program.before.strip() + '\n'
            LOG_FILE.write(public_key)
            LOG_FILE.close()

    except wexpect.exceptions.TIMEOUT:
        print("Timeout waiting for a prompt!")
    finally:
        program.close()

if __name__ == "__main__":
    iterateWordsList()



# print('ja')
# child = wexpect.spawn(cmd)
# child.expect('[pubkey recovery] seed phrase:')
# child.sendline(test)
# child.expect('enter')
# child.sendline('\n')
# # Print the output
# print(child.before)
