import requests
from datetime import datetime as dt
import socket
import logging
import json
import time

# =========================================
# SETTINGS
# =========================================
APIKEY = "KEY"
DOMAINNAME = "DOMAIN"
DNSTYPE = "AAAA"

# =========================================
# version
# =========================================
version = "0.5.0"

# request User-Agent
global headers, timeout
headers = {
    'User-Agent': 'ipv64-updater/' + str(version),
}
timeout = 10


# logging
#loglevel = logging.DEBUG
loglevel = logging.INFO
logging.basicConfig(filename='ipv64.log', encoding='utf-8', level=loglevel, format='%(asctime)s: %(message)s')

# =========================================
# get the current IP of the host
# =========================================
def get_ip(type):
    ipv4, ipv6 = False, False
    
    # Websites to check for current ip
    websites4 = ["https://ipv4.ipapi.de", "https://ip4.anysrc.net/plain", "https://ipv4.icanhazip.com/"]
    websites6 = ["https://ipv6.ipapi.de", "https://ip6.anysrc.net/plain", "https://ipv6.icanhazip.com/"]

    # Get the current IPv4
    if type == "A":
        for website in websites4:
            try:
                request4 = requests.get(website, headers=headers, timeout=timeout)
                # if website statuscode = 200 (ok) then break the loop and take the given ip
                if request4.status_code == 200:
                    ip = request4.text.replace(" ", "").replace("\n", "")
                    logging.info(f"IPv4 from {website}: {ipv4}")
                    break
            except:
                ip = False

    # Get the current IPv6
    elif type == "AAAA":
        for website in websites6:
            try:
                request6 = requests.get(website, headers=headers, timeout=timeout)
                # if website statuscode = 200 (ok) then break the loop and take the given ip
                if request6.status_code == 200:
                    ip = request6.text.replace(" ", "").replace("\n", "")
                    logging.info(f"IPv6 from {website}: {ipv6}")
                    break
            except:
                ip = False
    else:
        logging.warning("error while machine ip lookup: exit")
        exit()


    return ip

# =========================================
# Get the current ip of the domain
# =========================================
def get_domain_details(domain, type):

    limit = 3
    i = 0
    ip = False

    # retry x time, until exit
    while ip == False and i <= limit:
        # ipapi.de to get nameserver data as json data
        api_website = f"https://ipapi.de/nslookup.php?domain={domain}&type={type}&version={version}"

        request = requests.get(api_website, headers=headers, timeout=timeout)
        status = request.status_code
        
        # log if website is not reachable
        if status != 200:
            logging.warning(f"nslookup error: statuscode error {status} exit")
            exit()

        json_data = request.json()

        # if response is empty
        if json_data == []:
            i += 1
            logging.warning(f"nslookup type {type}: error while nslookup - no data found for domain {domain}")
            time.sleep(3)
            break
        else:
            try:
                if type == "A":
                    ip = json_data[0]['ip']
                elif type == "AAAA":
                    ip = json_data[0]['ipv6']
                else:
                    ip = False
            except:
                ip = False
                logging.warning(f"nslookup type {type}: error while nslookup exit")
                exit()
            
        if ip != False:
            logging.info(f"nslookup type {type}: {domain}: {ip}")

    return ip

# =========================================
# UPDATER
# =========================================
def update_ipv64(machine_ip, domain_ip, domain, apikey, type):

    # check if machine has a valid ip for the dns type
    if machine_ip == False:
        logging.warning(f"updater: machine has no ip: please choose other DNS type")
        exit()

    # check if the right key is given
    if len(apikey) > 24:
        logging.warning(f"updater: wrong key, use the account update token")
        exit()

    # check if type is A or AAAA
    if type == "A":
        ipv64_updater = f"https://ipv64.net/update.php?key={apikey}&domain={domain}&ip={machine_ip}"
    elif type == "AAAA":
        ipv64_updater = f"https://ipv64.net/update.php?key={apikey}&domain={domain}&ip6={machine_ip}"

    # check if ips are not the same
    if machine_ip == domain_ip:
        logging.info(f"updater: no update required")
        status = None
    else:    
        request = requests.get(ipv64_updater, headers=headers, timeout=timeout)
        status = request.status_code

        if status != 200:
            logging.warning(f"updater: statuscode error {status}")
            status = False
            exit()

        if status == 200:
            logging.warning(f"updater: {status} update successfull")
            status = True

# =========================================
# MAIN PART
# =========================================

# current machine ip
machine_ip = get_ip(DNSTYPE)
print(machine_ip)

# current domain ip
domain_ip = get_domain_details(DOMAINNAME, DNSTYPE)
print(domain_ip)

# update
update = update_ipv64(machine_ip, domain_ip, DOMAINNAME, APIKEY, DNSTYPE)

print(update)