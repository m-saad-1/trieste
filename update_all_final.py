import glob
import re

def update_css():
    css_path = 'assets/css/style.css'
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()

    # Desktop logo: 95px -> 115px
    css = css.replace('.header-logo {\n    height: 95px;', '.header-logo {\n    height: 115px;')
    
    # Mobile logo: 65px -> 80px, 70px -> 85px
    css = css.replace('.header-logo {\n        height: 65px !important;', '.header-logo {\n        height: 80px !important;')
    css = css.replace('.header-logo {\n        height: 70px !important;', '.header-logo {\n        height: 85px !important;')

    # Fix gap issue by making mobile-menu-btn the same size as icon-btn (40x40)
    css += """
.mobile-menu-btn {
    width: 40px !important;
    height: 40px !important;
    align-items: center !important;
    justify-content: center !important;
}
@media (max-width: 991px) {
    .mobile-menu-btn {
        display: flex !important;
    }
}
"""

    # Stick tabs to top
    css += """
.category-circles-wrapper {
    position: sticky !important;
    top: 75px !important;
    z-index: 95 !important;
    background: var(--clr-background) !important;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    margin-top: -10px !important;
}
@media (max-width: 991px) {
    .category-circles-wrapper {
        top: 60px !important;
    }
}
"""
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css)

def update_html():
    # Remove Offer 3 and Offer 4 from index.html only!
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    offer3 = '''                <a href="pages/offers.html" style="display: block; text-decoration: none;">
                    <div class="hero-image-frame" style="border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                        <img loading="lazy" decoding="async" src="./assets/images/offer (3).png" alt="Oferta 3" class="hero-full-img" style="width: 100%; display: block; object-fit: cover;">
                    </div>
                </a>\n'''
    offer4 = '''                <a href="pages/offers.html" style="display: block; text-decoration: none;">
                    <div class="hero-image-frame" style="border-radius: 20px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
                        <img loading="lazy" decoding="async" src="./assets/images/offer (4).png" alt="Oferta 4" class="hero-full-img" style="width: 100%; display: block; object-fit: cover;">
                    </div>
                </a>\n'''
                
    html = html.replace(offer3, '')
    html = html.replace(offer4, '')
    
    # footer logo increase
    html = html.replace('style="height: 110px; width: auto;"', 'style="height: 140px; width: auto;"')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
    for p in glob.glob('pages/*.html'):
        with open(p, 'r', encoding='utf-8') as f:
            p_html = f.read()
        p_html = p_html.replace('style="height: 110px; width: auto;"', 'style="height: 140px; width: auto;"')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(p_html)

update_css()
update_html()
print("done")
