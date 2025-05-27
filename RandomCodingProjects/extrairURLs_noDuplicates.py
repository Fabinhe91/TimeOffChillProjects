import re
from urllib.parse import urlparse

# Path to your file
file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'

# Read file content
with open(file_path, 'r') as file:
    content = file.read()

# Regex to find full URLs
url_pattern = r'https?://[^\s/$.?#].[^\s]*'
full_urls = re.findall(url_pattern, content)

# Extract base URLs (scheme + netloc)
base_urls = []
for url in full_urls:
    parsed = urlparse(url)
    if parsed.scheme and parsed.netloc:
        base_urls.append(f"{parsed.scheme}://{parsed.netloc}")

# Remove duplicates and sort
unique_base_urls = sorted(set(base_urls))

# Print the results
print("Unique base URLs found:")
for base in unique_base_urls:
    print(base)