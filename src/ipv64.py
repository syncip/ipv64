import requests
from datetime import datetime as dt
import socket
import logging
import json

# API KEY
api_key = "iw6OhcD2V1paymdjqvX3BrNs07eFfTC4"

# version
version = "0.4.0"

# request User-Agent
global headers
headers = {
    'User-Agent': 'ipv64-updater/' + str(version),
}

# logging
#loglevel = logging.DEBUG
loglevel = logging.INFO
logging.basicConfig(filename='ipv64.log', encoding='utf-8', level=loglevel, format='%(asctime)s: %(message)s')

# =========================================
# get the current IP of the host
# =========================================
def get_ip():
    ipv4, ipv6 = False, False
    
    # Websites to check for current ip
    websites4 = ["https://ipv4.ipapi.de", "https://ip4.anysrc.net/plain", "https://ipv4.icanhazip.com/"]
    websites6 = ["https://ipv6.ipapi.de", "https://ip6.anysrc.net/plain", "https://ipv6.icanhazip.com/"]

    # timeout in seconds
    timeout = 10

    # Get the current IPv4
    for website in websites4:
        try:
            request4 = requests.get(website, headers=headers, timeout=timeout)
            # if website statuscode = 200 (ok) then break the loop and take the given ip
            if request4.status_code == 200:
                ipv4 = request4.text.replace(" ", "").replace("\n", "")
                logging.info(f"IPv4 from {website}: {ipv4}")
                break
        except:
            ipv4 = False

    # Get the current IPv6
    for website in websites6:
        try:
            request6 = requests.get(website, headers=headers, timeout=timeout)
            # if website statuscode = 200 (ok) then break the loop and take the given ip
            if request6.status_code == 200:
                ipv6 = request6.text.replace(" ", "").replace("\n", "")
                logging.info(f"IPv4 from {website}: {ipv6}")
                break
        except:
            ipv6 = False

    return ipv4, ipv6

# =========================================
# Get the current ip of the domain
# =========================================
def get_domain_details(api_key, domain_check=True):
    api_website = f"https://ipv64.net/api.php?apikey={api_key}&get_domains"
    result = []

    request = requests.get(api_website)
    status = request.status_code
    json_data = request.json()

    # log if website is not reachable
    if status != 200:
        logging.WARNING("ipv64 API not reachable")
        exit()

    # get all the doamains of the account
    if json_data["info"] == "success":
        domains = json_data["subdomains"].keys()
        # check all given domains
        for domain in domains:
            # check if domain is know
            if domain in domain_check:
                # get all records for found domain
                records = json_data["subdomains"][domain]["records"]

                # check all records for the found domain
                for record in records:
                    logging.info(f"record: {record}")
                    
                    record_id = record["record_id"]
                    record_type = record["type"]
                    record_content = record["content"]
                    record_praefix = record["praefix"]

                    # add dict to list for working as json
                    record_data = {"record_id": str(record_id), "domain": str(domain), "type": str(record_type), "content": str(record_content), "praefix": str(record_praefix)}
                    result.append(record_data)
    
    return result
       

#current_ipv4, current_ipv6 = get_ip()
ips = json.dumps(get_domain_details(api_key, ["cloudflare.ipv64.net"]))