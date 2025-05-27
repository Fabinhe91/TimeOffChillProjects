import re
from collections import defaultdict

# File path
file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'
output_path = r'C:\\Users\\xid09254\\Desktop\\ip_to_urls.txt'
import re
from collections import defaultdict

file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'
output_path = r'C:\\Users\\xid09254\\Desktop\\ip_to_urls_v2.txt'

# Patterns
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
url_pattern = r'(?:https?://|www\.)[^\s"]+|(?:GET|POST|PUT|DELETE|CONNECT)\s([^\s"]+)'

ip_to_urls = defaultdict(set)

with open(file_path, 'r') as file:
    for line in file:
        ip_match = re.search(ip_pattern, line)
        url_match = re.search(url_pattern, line)
        
        if ip_match:
            ip = ip_match.group()
            if url_match:
                raw_url = url_match.group(1)
                ip_to_urls[ip].add(raw_url)
            else:
                ip_to_urls[ip]  # still store the IP even if no URL

# Output to file
with open(output_path, 'w') as out_file:
    for ip, urls in sorted(ip_to_urls.items()):
        cleaned_urls = sorted(u for u in urls if u)  # Filter out None or empty strings
        out_file.write(f"{ip}:\n")
        for url in cleaned_urls:
            out_file.write(f"  - {url}\n")
        out_file.write("\n")
if raw_url:
    ip_to_urls[ip].add(raw_url)

print(f"✅ Updated IP-to-URL mapping saved to {output_path}")