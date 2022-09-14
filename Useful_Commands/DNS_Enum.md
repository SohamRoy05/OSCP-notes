# DNS Enumeration

## Tips:
 1. If you see the **Apache Default Page**, it means there is some misconfiguration or there is vhosting going on.
 	For the latter case, include the domain name along with ip address in the */etc/host* file to map to the correct 
 	domain.


## nslookup

 1. >>nslookup
 2. >>server 192.214.31.3
 3. >>set q=X
 4. >>witrap.com
 5. >>exit

* X is:
  NS: Name servers
  MX: Mail Exchanger
  A: IPv4
  AAAA: IPv6
  CNAME: Alias of the domain
  PTR: Reverse lookups


## dig
 
* **Zone transfer** : `dig axfr cronos.htb @dnsserver`

## Host

* Host can be used dns lookup.
* `host -l <domain name> <server> ` command can be used to list all records for the domain name by quering the given server. 
  This is similar to zone transfer.

