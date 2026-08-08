import glob
import re

# 1. Translate remaining HTML files
translations = {
    "Entre em Contact": "Contact Us",
    "Sobre Nós": "About Us",
    "Sobre": "About",
    "Navegação": "Navigation",
    "Almoço:": "Lunch:",
    "Petiscaria:": "Appetizers:",
    "Feijoada Especial:": "Special Feijoada:",
    "Sextas de 11h às 16h": "Fridays 11am to 4pm",
    "11h às 16h": "11am to 4pm",
    "18h30 à 00h": "6:30pm to 12am",
    "3 itens": "3 items", # specific to the cart floating bar
    "Ver Carrinho": "View Cart",
    "Buscar pratos...": "Search dishes...",
    "Carrinho": "Cart",
    "Perfil": "Profile",
    "Pedidos": "Orders",
    "Abrir chat": "Open chat",
    "Total:": "Total:",
    "Endereço de Entrega": "Delivery Address",
    "Rua das Flores, 123": "123 Flower Street",
    "Apto 45": "Apt 45",
    "Centro": "Downtown",
    "Petrópolis, RJ": "Petrópolis, RJ",
    "Resumo": "Summary",
    "Cancelar": "Cancel",
    "Confirmar": "Confirm",
    "Adicionado ao carrinho!": "Added to cart!",
    "Item adicionado com sucesso.": "Item successfully added.",
    "Avaliações": "Reviews",
    "avaliacoes": "reviews",
    "avaliações": "reviews",
    "Por quilo": "Per kilo",
    "por quilo": "per kilo",
    "Comida de verdade": "Real food",
    "O lugar perfeito": "The perfect place",
    "para comer bem e reunir os amigos.": "to eat well and gather with friends.",
    "Petiscaria à noite": "Evening appetizers",
    "Nenhuma nova notificação": "No new notifications",
    "Online agora": "Online now",
    "Assistente Cafe Trieste": "Cafe Trieste Assistant",
    "Olá! Bem-vindo ao Cafe Trieste. Como posso ajudar você hoje?": "Hello! Welcome to Cafe Trieste. How can I help you today?",
    "Digite sua mensagem...": "Type your message...",
    "Enviar": "Send"
}

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply translations
    for pt, en in translations.items():
        html = html.replace(pt, en)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Remove profile icon from menu page header
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'r', encoding='utf-8') as f:
    menu_html = f.read()

# The profile icon looks like:
# <a href="profile.html" class="icon-btn" aria-label="Profile">
#     <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
# </a>

profile_icon_pattern = r'<a href="profile\.html" class="icon-btn"[^>]*>[\s\S]*?</svg>\s*</a>'
menu_html = re.sub(profile_icon_pattern, '', menu_html)

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'w', encoding='utf-8') as f:
    f.write(menu_html)


# 3. Fix payment card color in profile page to be white
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\profile.html', 'r', encoding='utf-8') as f:
    profile_html = f.read()

# I had set it to `border: 2px solid rgba(212, 175, 55, 0.15); background: #1A1A1A;`
# Now change it to white background and dark text for contrast
profile_html = profile_html.replace('border: 2px solid rgba(212, 175, 55, 0.15); background: #1A1A1A;',
                                    'border: 2px solid #ddd; background: white; color: #161616;')
# Ensure inner spans also become dark if they were white
profile_html = profile_html.replace('<span style="font-size: 0.85rem; color: white;">Terminado em 4321</span>',
                                    '<span style="font-size: 0.85rem; color: #555;">Ending in 4321</span>')
profile_html = profile_html.replace('<span style="font-size: 0.85rem; color: white;">Chave cadastrada</span>',
                                    '<span style="font-size: 0.85rem; color: #555;">Registered key</span>')

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\profile.html', 'w', encoding='utf-8') as f:
    f.write(profile_html)

print("Remaining translations applied, Profile icon removed from menu header, and payment cards made white.")
