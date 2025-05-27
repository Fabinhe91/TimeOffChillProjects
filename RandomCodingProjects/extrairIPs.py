import re

# Path to your text file
file_path = 'C:\\Users\\xid09254\\Desktop\\access.log'

# Regular expression for IPv4 addresses
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

with open(file_path, 'r') as file:
    content = file.read()

# Find all IPv4 addresses
ipv4_addresses = re.findall(ipv4_pattern, content)

# Optional: Filter out invalid IPs (like 999.999.999.999)
def is_valid_ipv4(ip):
    parts = ip.split('.')
    return all(0 <= int(part) <= 255 for part in parts)

#valid_ipv4_addresses = [ip for ip in ipv4_addresses if is_valid_ipv4(ip)]

#print("Found IPv4 addresses:")
#for ip in valid_ipv4_addresses:
#    print(ip)
unique_ipv4_addresses = sorted(set(valid_ipv4_addresses))

print("Unique IPv4 addresses:")
for ip in unique_ipv4_addresses:
    print(ip)