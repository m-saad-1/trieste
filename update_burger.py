import glob
import re

def update_html_files():
    burger_svg = r'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>'
    burger_html = '''<div class="hamburger-lines">
                        <span class="line line1"></span>
                        <span class="line line2"></span>
                        <span class="line line3"></span>
                    </div>'''

    for path in glob.glob('*.html') + glob.glob('pages/*.html'):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Revert burger
        content = content.replace(burger_svg, burger_html)
        
        # Increase footer logo
        content = content.replace('style="height: 80px; width: auto;"', 'style="height: 110px; width: auto;"')

        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

def update_css():
    css_path = 'assets/css/style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # Increase header logo size
    css = re.sub(r'\.header-logo\s*\{\s*height:\s*70px;', '.header-logo {\n    height: 95px;', css)
    css = re.sub(r'\.header-logo\s*\{\s*height:\s*45px\s*!important;', '.header-logo {\n        height: 65px !important;', css)
    
    # Check if there are other heights like 50px
    css = re.sub(r'\.header-logo\s*\{\s*height:\s*50px\s*!important;', '.header-logo {\n        height: 70px !important;', css)

    # Add styling for burger lines
    burger_css = """
.hamburger-lines .line2 {
    width: 50%;
    align-self: flex-end;
}

.hamburger-lines .line3 {
    width: 75%;
    align-self: flex-end;
}

.mobile-menu-btn.open .line2,
.mobile-menu-btn.open .line3 {
    width: 100%;
}
"""
    if "align-self: flex-end;" not in css:
        css += burger_css

    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

update_html_files()
update_css()
print("Done updating")
