import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the header logo huge and properly position it.
# The desktop height is 220px. 
def fix_desktop_logo(m):
    return """.header-logo {
    height: 220px;
    width: auto;
    display: block;
    max-width: 100%;
    position: relative;
    z-index: 105;
    transform: translateY(-5px);
}"""
css = re.sub(r'\.header-logo\s*\{[^}]*height:\s*180px;[^}]*\}', fix_desktop_logo, css)

# Mobile overrides
mobile_fixes = """
@media (max-width: 1024px) {
    .navbar {
        height: 60px;
    }
    .nav-left {
        padding-left: 120px; /* Space for mobile logo */
        gap: 0.5rem;
    }
    .logo {
        top: 5px;
        left: 1rem;
    }
    .header-logo {
        height: 140px !important;
    }
}
"""

if "padding-left: 120px;" not in css:
    css += mobile_fixes

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Applied robust logo positioning")
