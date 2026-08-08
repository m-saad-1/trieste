import glob
import re

html_files = glob.glob('pages/*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace inline white backgrounds with dark surface
    html = html.replace('background: white;', 'background: var(--clr-surface); border: 1px solid rgba(212, 175, 55, 0.15);')
    html = html.replace('background-color: white;', 'background-color: var(--clr-surface); border: 1px solid rgba(212, 175, 55, 0.15);')
    
    # Adjust inline box-shadows to be visible in dark mode
    html = html.replace('box-shadow: 0 4px 15px rgba(0,0,0,0.05)', 'box-shadow: 0 10px 30px rgba(0,0,0,0.5)')
    html = html.replace('box-shadow: 0 15px 40px rgba(0,0,0,0.08)', 'box-shadow: 0 15px 40px rgba(0,0,0,0.6)')
    html = html.replace('box-shadow: 0 4px 20px rgba(0,0,0,0.05)', 'box-shadow: 0 10px 30px rgba(0,0,0,0.5)')
    html = html.replace('box-shadow: 0 2px 10px rgba(0,0,0,0.02)', 'box-shadow: 0 5px 15px rgba(0,0,0,0.4)')
    
    # Check for text colors inside these cards (might be #333 or similar inline)
    html = re.sub(r'color:\s*#333(333)?;', 'color: var(--clr-text-primary);', html)
    html = re.sub(r'color:\s*#555(555)?;', 'color: #B0B0B0;', html)
    html = re.sub(r'color:\s*#777(777)?;', 'color: #999999;', html)
    
    # Also check border: 1px solid #ddd in selects/inputs
    html = html.replace('border: 1px solid #ddd;', 'border: 1px solid rgba(212, 175, 55, 0.15);')
    html = html.replace('border: 1px solid #eee;', 'border: 1px solid rgba(212, 175, 55, 0.15);')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated inline styles in all HTML files.")
