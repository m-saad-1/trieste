import glob
import re

# 1. Make the Home and Menu search bar identical
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'r', encoding='utf-8') as f:
    menu_html = f.read()

# Replace the customized search bar with the exact one from index.html
menu_search_pattern = r'<div class="mobile-search-bar"[^>]*>[\s\S]*?<div class="search-input-wrapper">([\s\S]*?)</div>\s*</div>\s*</div>'
replacement_search = r"""<div class="mobile-search-bar">
            <div class="search-input-wrapper">
\1
            </div>
        </div>"""

menu_html = re.sub(menu_search_pattern, replacement_search, menu_html)

# Also fix remaining untranslated Portuguese tabs/words if any missed
menu_html = menu_html.replace('Pedidos', 'Orders')
menu_html = menu_html.replace('Perfil', 'Profile')
menu_html = menu_html.replace('Nenhuma nova notificação', 'No new notifications')
menu_html = menu_html.replace('Assistente Cafe Trieste', 'Cafe Trieste Assistant')
menu_html = menu_html.replace('Online agora', 'Online now')
menu_html = menu_html.replace('Olá! Bem-vindo ao Cafe Trieste. Como posso ajudar você hoje?', 'Hello! Welcome to Cafe Trieste. How can I help you today?')
menu_html = menu_html.replace('Digite sua mensagem...', 'Type your message...')

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'w', encoding='utf-8') as f:
    f.write(menu_html)


# 2. Fix the payment card colors in profile.html
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\profile.html', 'r', encoding='utf-8') as f:
    profile_html = f.read()

profile_html = profile_html.replace('border: 2px solid #ddd;', 'border: 2px solid rgba(212, 175, 55, 0.15); background: #1A1A1A;')
# And ensure hover states for them don't look weird if they exist, but they are inline so it's fine.
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\profile.html', 'w', encoding='utf-8') as f:
    f.write(profile_html)


# 3. Sticky category tabs
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make category circles wrapper sticky
css += """
/* Sticky Tabs Fix */
.category-circles-wrapper, .category-tabs {
    position: sticky;
    top: 60px; /* Below the header */
    z-index: 100;
    background: var(--clr-background);
    padding: 1rem 0;
    margin-top: -1rem; /* Adjust spacing */
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.mobile-search-bar {
    position: sticky;
    top: 60px;
    z-index: 99;
}
"""

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Search bar aligned, Payment cards fixed, Tabs made sticky.")
