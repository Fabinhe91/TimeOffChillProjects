import re
from collections import defaultdict

# File path
file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'
output_path = r'C:\\Users\\xid09254\\Desktop\\ip_to_urls.txt'

# Patterns
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
url_pattern = r'(?:https?://|www\.)[^\s"]+|(?:GET|POST|PUT|DELETE)\s(/[^\s"]+)'

# Store mappings
ip_to_urls = defaultdict(set)

with open(file_path, 'r') as file:
    for line in file:
        ip_match = re.search(ip_pattern, line)
        url_match = re.search(url_pattern, line)
        
        if ip_match and url_match:
            ip = ip_match.group()
            raw_url = url_match.group()
            
            # Extract URL part from method-style lines like "GET /index.html"
            url = raw_url if raw_url.startswith('http') else raw_url.split()[1] if ' ' in raw_url else raw_url
            
            ip_to_urls[ip].add(url)

# Write to output
with open(output_path, 'w') as out_file:
    for ip, urls in sorted(ip_to_urls.items()):
        out_file.write(f"{ip}:\n")
        for url in sorted(urls):
            out_file.write(f"  - {url}\n")
        out_file.write("\n")

print(f"✅ IP-to-URL mappings saved to {output_path}")
