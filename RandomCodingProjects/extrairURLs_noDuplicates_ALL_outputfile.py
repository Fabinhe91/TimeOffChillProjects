import re

# Input file path
file_path = r'C:\\Users\\xid09254\\Desktop\\access.log'

# Output file path (same directory, or change if needed)
output_path = r'C:\\Users\\xid09254\\Desktop\\extracted_urls.txt'

# Read content
with open(file_path, 'r') as file:
    content = file.read()

# Regex to catch full URLs and bare domains with paths
url_pattern = r'\b(?:https?://|www\.)[^\s<>"]+|(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(?:/[^\s]*)?'

# Extract and deduplicate
all_urls = re.findall(url_pattern, content)
unique_urls = sorted(set(all_urls))

# Write to output file
with open(output_path, 'w') as out_file:
    for url in unique_urls:
        out_file.write(url + '\n')

print(f"✅ URLs saved to {output_path}")