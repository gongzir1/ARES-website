with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace description color name
html = html.replace('highlighted in <span class="has-text-danger has-text-weight-bold">red</span>', 'highlighted in <span class="has-text-info has-text-weight-bold">blue</span>')

# Replace the red danger classes with blue info classes
html = html.replace('has-text-danger', 'has-text-info')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
