import re

# Path to your text file (update this)
file_path = r'C:\Users\xid09254\Desktop\\access.log'

# Regular expression for IPv4 addresses
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Read file content
with open(file_path, 'r') as file:
    content = file.read()

# Find all IPv4 addresses
ipv4_addresses = re.findall(ipv4_pattern, content)

# Function to validate IP addresses (0-255 range)
def is_valid_ipv4(ip):
    parts = ip.split('.')
    return all(0 <= int(part) <= 255 for part in parts)

# Filter valid IPs and remove duplicates
valid_ipv4_addresses = [ip for ip in ipv4_addresses if is_valid_ipv4(ip)]
unique_ipv4_addresses = sorted(set(valid_ipv4_addresses))

# Print results
print("Unique IPv4 addresses found:")
for ip in unique_ipv4_addresses:
    print(ip)