import glob
import re

# 1. Translate HTML files
translations = {
    # Nav & Common
    "Início": "Home",
    "Cardápio": "Menu",
    "Ofertas": "Offers",
    "Galeria": "Gallery",
    "Contato": "Contact",
    "Localização": "Location",
    "Horário de Funcionamento": "Opening Hours",
    "Olá, seja bem-vindo!": "Hello, welcome!",
    "Peça Agora": "Order Now",
    "Restaurante por quilo no almoço e Petiscaria à noite. O ponto de encontro perfeito no Alto da Serra.": "Buffet lunch and evening appetizers. The perfect meeting point in Alto da Serra.",
    "Fechado": "Closed",
    "O Verdadeiro Sabor do Brasil": "The True Taste of Brazil",
    "Comida de verdade no almoço por quilo e a melhor petiscaria à noite no Alto da Serra. O lugar perfeito para comer bem e reunir os amigos.": "Real food for lunch and the best snacks at night in Alto da Serra. The perfect place to eat well and gather with friends.",
    "Todos os direitos reservados.": "All rights reserved.",
    "Horários": "Hours",
    
    # Cart / Orders
    "Seu Carrinho": "Your Cart",
    "Seu carrinho está vazio": "Your cart is empty",
    "Adicione itens do cardápio para começar seu pedido.": "Add items from the menu to start your order.",
    "Voltar ao Cardápio": "Back to Menu",
    "Resumo do Pedido": "Order Summary",
    "Subtotal": "Subtotal",
    "Taxa de Entrega": "Delivery Fee",
    "Grátis": "Free",
    "Finalizar Pedido": "Checkout",
    "Meus Pedidos": "My Orders",
    "Nenhum pedido encontrado": "No orders found",
    "Você ainda não fez nenhum pedido no HDM.": "You haven't made any orders yet.",
    "Fazer um Pedido": "Make an Order",
    
    # Profile
    "Dados Pessoais": "Personal Information",
    "Atualize suas informações e preferências.": "Update your information and preferences.",
    "Nome Completo": "Full Name",
    "E-mail": "Email",
    "Telefone": "Phone",
    "Data de Nascimento": "Date of Birth",
    "Salvar Alterações": "Save Changes",
    "Endereços": "Addresses",
    "Métodos de Pagamento": "Payment Methods",
    "Cartão de Crédito": "Credit Card",
    "Terminado em": "Ending in",
    "Chave cadastrada": "Registered key",
    "Configurações": "Settings",
    "Sair": "Logout",
    
    # Reservations
    "Reservas": "Reservations",
    "Fazer Reserva": "Make a Reservation",
    "Data": "Date",
    "Hora": "Time",
    "Pessoas": "People",
    "Confirmar Reserva": "Confirm Reservation",
    "Reserva Confirmada!": "Reservation Confirmed!",
    "Sua mesa foi reservada com sucesso. Enviamos os detalhes para o seu telefone.": "Your table has been successfully reserved. We sent the details to your phone.",
    "Entendido": "Understood",
    
    # Contact
    "Entre em Contato": "Contact Us",
    "Envie uma Mensagem": "Send a Message",
    "Nome": "Name",
    "Assunto": "Subject",
    "Mensagem": "Message",
    "Enviar Mensagem": "Send Message",
    "Dúvida": "Question",
    "Reclamação": "Complaint",
    "Elogio": "Compliment",
    "Outro": "Other",
    "Agradecemos seu contato. Responderemos em breve.": "Thank you for reaching out. We will respond shortly.",
    "Endereço": "Address",
    "Segunda a Sexta": "Monday to Friday",
    "Sábado e Domingo": "Saturday and Sunday",
    "Feriados": "Holidays",
    
    # General UI
    "Adicionar": "Add",
    "Ver Mais": "View More",
    "Ver Todos": "View All",
    "Fechar": "Close",
    "Novidades": "News",
    "Nossa Galeria": "Our Gallery",
    "Conheça nosso espaço e veja nossos pratos mais pedidos.": "Discover our space and see our most popular dishes.",
    "Mais Momentos": "More Moments",
    "Acompanhe nosso dia a dia no Instagram!": "Follow our daily life on Instagram!",
    "Siga no Insta": "Follow on Insta",
    "Especialidade": "Specialty",
    "Marcar todas como lidas": "Mark all as read",
    "Notificações": "Notifications",
    "Você não tem novas notificações": "You have no new notifications",
    "Buscar pratos ou categorias...": "Search dishes or categories...",
    "Buscar...": "Search...",
    "Todas": "All"
}

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Apply translations
    for pt, en in translations.items():
        html = html.replace(pt, en)
        # Also try lowercase for exact string matches like placeholders
        if pt.lower() != pt:
            html = html.replace(f'placeholder="{pt}"', f'placeholder="{en}"')
            html = html.replace(f'>{pt.lower()}<', f'>{en.lower()}<')

    # Fix menu page search bar background
    html = html.replace('background: var(--clr-surface); padding-top: 2rem;', 'background: var(--clr-background); padding-top: 2rem;')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Fix CSS for search bar inner input background
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I added !important to inputs globally earlier, which caused the inner input of the search wrapper to inherit the background.
# Let's explicitly make the search input transparent with !important.
if 'transparent !important;' not in css:
    css = css.replace('.search-input-wrapper input {\n    border: none;\n    background: transparent;', 
                      '.search-input-wrapper input {\n    border: none;\n    background: transparent !important;\n    background-color: transparent !important;')

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Language translated, Menu page background fixed, and Search Bar internal background removed.")
