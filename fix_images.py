with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

count = text.count('"images/')
print(f'Found {count} occurrences of "images/')

if count > 0:
    text = text.replace('"images/', '"Images/')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('Replaced with "Images/')
