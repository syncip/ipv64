# How to install
```pip install ipv64```
or
```python -m pip install ipv64```

# How to run
Options:  
-d (domain name) and -uh (update hash) is required  
-w (discord webhook) is optional

## Windows
```python -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```

## Linux
```/usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```

### run with cron
#### check every minute
```* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```
#### check every 30 seconds
```* * * * * /usr/bin/python3 -m ipv64 -d YOUR_DOMAIN.ipv64.net -uh YOUR_UPDATE_HASH -d DISCORD_WEBHOOK```

# Help
```python -m ipv64 -h```

```usage: ipv64.py [-h] -d DOMAIN -uh HASH [-w WEBHOOK]

Update the IP for a domain on ipv64.net

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        The domain to update
  -uh HASH, --hash HASH
                        Your DynDNS Updatehash
  -w WEBHOOK, --webhook WEBHOOK
                        The webhook url for discord notifications```
