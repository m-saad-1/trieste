import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove any remaining negative margins and standardize mobile height to 80px
css = re.sub(r'height:\s*80px\s*!important;\s*margin-top:\s*-20px\s*!important;\s*margin-bottom:\s*-20px\s*!important;', 'height: 80px !important;', css)
css = re.sub(r'height:\s*120px\s*!important;', 'height: 80px !important;', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Standardized mobile logo size and removed leftover negative margins.")
