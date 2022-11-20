# How it is working
1. The libary checks at every run the ipv64 name server (195.201.223.103) for the ip of the given domain.  
2. Next we check at [ipv4.ipapi.de](https://ipv4.ipapi.de) and [ipv6.ipapi.de](https://ipv6.ipapi.de) for your current IPv4 and IPv6.
3. If the IPs are not the same (and not None -> e.g. there is no IPv6 or IPv4), the libary runs a GET request at ipv64.net to update your IP in the A or/and AAAA record.

# How to install
The libary is avilable at [pypi.org](https://pypi.org/project/pip/)

```pip install ipv64```
or
```python -m pip install ipv64```

# How to update
```pip install ipv64 --upgrade```
or
```python -m pip install ipv64 --upgrade```

# How to run
## INFO
The Script did __NOT__ run in a loop, you need to run it manually.

## Windows
Update A and AAAA record if possible  
```python -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```

## Linux
Update A and AAAA record if possible  
```/usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```

### run with cron
#### check every minute
```* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```
#### check every 30 seconds
```
* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK
* * * * * sleep 30; /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK
```

# Help
```python ipv64.py --help
usage: ipv64.py [-h] -d DOMAIN -uh HASH [-p PREFIX] [-w WEBHOOK] [-4] [-6]

Update the IP for a domain on ipv64.net

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        The domain to update
  -uh HASH, --hash HASH
                        Your DynDNS update hash
  -p PREFIX, --prefix PREFIX
                        The prefix for the domain
  -w WEBHOOK, --webhook WEBHOOK
                        The webhook url for discord notifications
  -4, --ipv4            Update only the A record
  -6, --ipv6            Update only the AAAA record```
