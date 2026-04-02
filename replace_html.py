import re

with open('orig.txt', 'r', encoding='utf-8') as f:
    orig = f.read().strip()
with open('recov.txt', 'r', encoding='utf-8') as f:
    recov = f.read().strip()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace inner html
html = re.sub(r'(<div id="text-original"[^>]*>)(.*?)(                                </div>\n                            </div>)', lambda m: m.group(1) + '\n                                    ' + orig + '\n' + m.group(3), html, flags=re.DOTALL)

html = re.sub(r'(<div id="text-recovered"[^>]*>)(.*?)(                                </div>\n                            </div>)', lambda m: m.group(1) + '\n                                    ' + recov + '\n' + m.group(3), html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
