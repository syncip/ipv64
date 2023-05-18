import requests

# =========================================
# Send Message on Update
# =========================================


# =========================================
# Discord
# =========================================
def discord(webhook_url, msg):
    payload = {
        "content": msg,
        "username": "ipv64 Updater",
        "avatar_url": "https://ipv64.net/img/ipv64_logo.svg"
    }
    
    re = requests.post(webhook_url, json=payload)
    status = re.status_code
    
    return status
    

# =========================================
# ntfy
# =========================================
def ntfy(webhook_url, msg):
    head = {
        "Title": "ipv64 Updater",
        "Tags": "information_source"
    }
    re = requests.post(webhook_url,data=msg.encode(encoding='utf-8'), headers=head)
    status = re.status_code

    return status
# =========================================
# gotify
# =========================================


# =========================================
# pushover
# =========================================