import re

# Path to your file
file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'

with open(file_path, 'r') as file:
    content = file.read()

# This regex grabs:
# - URLs starting with http or https
# - URLs without scheme (bare domains)
url_pattern = r'\b(?:https?://|www\.)[^\s<>"]+|(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?'

# Find all URLs/domains
all_urls = re.findall(url_pattern, content)

# Remove duplicates and sort
unique_urls = sorted(set(all_urls))

# Output
print("All URLs found:")
for url in unique_urls:
    print(url)