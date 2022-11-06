import requests
from nslookup import Nslookup
from datetime import datetime as dt
import time

domain_name = "hm80.ipv64.net"
update_key = "RHt5YieXOgQVlE3WZpMCDBA2"
check_time = 30

def get_ip():
    try:
        ipv4 = requests.get('https://ipv4.ipapi.de').text
    except:
        print(dt.now(), ':\t', "Error: Could not get IPv4")
        ipv4 = False
    try:
        ipv6 = requests.get('https://ipv6.ipapi.de').text
    except:
        print(dt.now(), ':\t', "Error: Could not get IPv6")
        ipv6 = False
    
    return [ipv4, ipv6]

def nslookup():
    dns_query = Nslookup()
    dns_query = Nslookup(dns_servers=["2a01:4f8:c2c:559c::1", "195.201.223.103"], tcp=True)
    ips_record4 = dns_query.dns_lookup(domain_name)
    ips_record6 = dns_query.dns_lookup6(domain_name)
    
    ip4 = ips_record4.answer[0]
    ip6 = ips_record6.answer[0]

    return [ip4, ip6]

def update(ipv4, ipv6, nsipv4, nsipv6, update_key, domain_name):
    if ipv4 == nsipv4 and ipv4 != False:
        print(dt.now(), ':\t', f"INFO: IPv4 ({ipv4}) is up to date")
    else:
        # update ipv4 with get request
        if ipv4 != False:
            try:
                r = requests.get(f"https://ipv64.net/update.php?key={update_key}&domain={domain_name}&ip={ipv4}")
                if r.status_code == 200:
                    print(dt.now(), ':\t', f"INFO: IPv4 ({ipv4}) updated")
            except:
                print(dt.now(), ':\t', "ERROR: Could not update IPv4")
        

    if ipv6 == nsipv6 and ipv6 != False:
        print(dt.now(), ':\t', f"INFO: IPv6 ({ipv6}) is up to date")
    else:
        if ipv6 != False:
            try:
                r = requests.get(f"https://ipv64.net/update.php?key={update_key}&domain={domain_name}&ip6={ipv6}")
                if r.status_code == 200:
                    print(dt.now(), ':\t', f"INFO: IPv6 ({ipv6}) updated")
            except:
                print(dt.now(), ':\t', "ERROR: Could not update IPv6")
        

def main():
    while True:
        ipv4, ipv6 = get_ip()
        nsipv4, nsipv6 = nslookup()
        update(ipv4, ipv6, nsipv4, nsipv6, update_key, domain_name)
        
        time.sleep(check_time)

if __name__ == "__main__":
    main()