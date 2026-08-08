import glob
import re

# 1. Add the profile icon back to pages/menu.html
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'r', encoding='utf-8') as f:
    menu_html = f.read()

profile_icon = """<a href="profile.html" class="icon-btn" aria-label="Profile">
                    <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                </a>
                <button class="mobile-menu-btn" """

# Currently in menu.html: 
# </a>\n                \n                <button class="mobile-menu-btn"
menu_html = menu_html.replace('</a>\n                \n                <button class="mobile-menu-btn" ', '</a>\n                ' + profile_icon)
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\pages\menu.html', 'w', encoding='utf-8') as f:
    f.write(menu_html)


# 2. Fix the CSS mobile hide
with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I translated aria-label="Perfil" to "Profile", so the CSS broke.
css = css.replace('.nav-right a[aria-label="Perfil"] { display: none !important; }',
                  '.nav-right a[aria-label="Profile"] { display: none !important; }')

with open(r'd:\WEB_DEVELOPMENT\Cafe_Trieste\assets\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Profile icon correctly hidden on mobile via CSS, and restored for desktop.")
