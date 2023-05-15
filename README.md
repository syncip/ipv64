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
The Script is __NOT__ able to handle praefix - only the main domain can be updated

## Windows
Update A and AAAA record if possible  
```python -m ipv64 -d YOUR_DOMAIN.ipv64.net -k ACCOUNT_UPDATE_TOKEN -t TYPE```

## Linux
Update A and AAAA record if possible  
```/usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -k ACCOUNT_UPDATE_TOKEN -t TYPE```

### run with cron
#### check every minute with cron
```* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh ACCOUNT_UPDATE_TOKEN -d DISCORD_WEBHOOK```
#### check every 30 seconds with cron
```
* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -k ACCOUNT_UPDATE_TOKEN -t TYPE
* * * * * sleep 30; /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -k ACCOUNT_UPDATE_TOKEN -t TYPE
```

# Help
```python ipv64.py --help
usage: ipv64.py [-h] -d DOMAIN -k KEY -t TYPE

Update the IP for a domain on ipv64.net

options:
  -h, --help                  show this help message and exit
  -d DOMAIN, --domain DOMAIN  The domain to update (e.g. test.ipv64.net)
  -k KEY, --key KEY           Your ipv64 Account Update Token
  -t TYPE, --type TYPE        The Update Type (A or AAAA)```
