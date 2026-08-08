import re

def update_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    with open('menu_generated.html', 'r', encoding='utf-8') as f:
        new_menu_html = f.read()

    if file_path == 'pages/menu.html':
        new_menu_html = new_menu_html.replace('assets/images/', '../assets/images/')

    # We want to replace the content inside <section class="menu" id="cardapio">\n    <div class="container"> ... <div style="text-align: center; margin-top: 3rem;"> (for index) or end of container
    
    # Let's find the start of the category circles wrapper and the end of the last menu grid
    # A robust way is to use regex.
    pattern = re.compile(r'(<div class="category-circles-wrapper">.*?)(?=\s*</div>\s*(?:<div style="text-align: center;|</section>|</div>\s*</section>))', re.DOTALL)
    
    # For index.html, there is a <div style="text-align: center; ..."> after the categories.
    # For pages/menu.html, the container ends with </div>\s*</section>
    
    match = pattern.search(content)
    if match:
        old_section = match.group(1)
        new_content = content.replace(old_section, new_menu_html)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Could not find menu section in {file_path}")

update_html('pages/menu.html')
update_html('index.html')
