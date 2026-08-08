import json

def generate_menu_html():
    with open('assets/data/menu.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    html = '<div class="category-circles-wrapper">\n'
    for i, category in enumerate(data['categories']):
        cat_id = category['name'].replace(' ', '-').replace('&', 'and').lower()
        active = ' active' if i == 0 else ''
        html += f'    <a href="#{cat_id}" class="category-circle-btn{active}" style="text-decoration:none;">\n'
        html += f'        <span class="circle-label" style="padding: 10px;">{category["name"]}</span>\n'
        html += f'    </a>\n'
    html += '</div>\n\n'
    
    for category in data['categories']:
        cat_id = category['name'].replace(' ', '-').replace('&', 'and').lower()
        html += f'<div id="{cat_id}" style="display: flex; justify-content: space-between; align-items: center; margin: 1.5rem 0 1rem; scroll-margin-top: 100px;">\n'
        html += f'    <h3 style="font-size: 1.15rem; font-weight: 700; color: var(--clr-text-primary); margin: 0;">{category["name"]}</h3>\n'
        html += f'</div>\n'
        if 'description' in category:
            html += f'<p style="color: var(--clr-text-secondary); margin-bottom: 1rem;">{category["description"]}</p>\n'
            
        html += f'<div class="menu-grid">\n'
        for item in category['items']:
            html += f'    <div class="product-card">\n'
            if 'image' in item:
                html += f'        <div class="card-image">\n'
                html += f'            <img src="{item["image"]}" alt="{item["name"]}" loading="lazy">\n'
                html += f'        </div>\n'
            html += f'        <div class="card-content" style="padding-top: 1rem;">\n'
            html += f'            <div class="card-header"><h3>{item["name"]}</h3></div>\n'
            if 'description' in item:
                html += f'            <p class="card-desc">{item["description"]}</p>\n'
            html += f'            <div class="card-footer" style="margin-top: 1rem;">\n'
            html += f'                <span class="price">Rs {item["price"]}</span>\n'
            html += f'                <button class="btn btn-primary" style="padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600;">Adicionar</button>\n'
            html += f'            </div>\n'
            html += f'        </div>\n'
            html += f'    </div>\n'
        html += f'</div>\n\n'
        
    with open('menu_generated.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    generate_menu_html()
