lines = open('pdf_text_extracted.txt', 'r', encoding='utf-8').read().splitlines()
orig = []
recov = []
cur = None
for line in lines:
    line = line.strip()
    if not line: continue
    if line.startswith('Original:'):
        cur = 'orig'
        orig.append(line.replace('Original:', '', 1).strip())
    elif line.startswith('Recovered:'):
        cur = 'recov'
        recov.append(line.replace('Recovered:', '', 1).strip())
    else:
        if cur == 'orig':
            orig[-1] += ' ' + line
        elif cur == 'recov':
            recov[-1] += ' ' + line

with open('orig.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(orig))
with open('recov.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(recov))
