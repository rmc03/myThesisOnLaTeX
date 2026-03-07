files = [
    'd:/Universidad/Tesis/Thesis_template fix/Chapter1.tex',
    'd:/Universidad/Tesis/Thesis_template fix/Chapter2.tex',
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content.replace('\\begin{figure}[!htbp]', '\\begin{figure}[H]')
    new_content = new_content.replace('\\begin{figure}[htbp]', '\\begin{figure}[H]')
    new_content = new_content.replace('\\begin{table}[!htbp]', '\\begin{table}[H]')
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Fixed: ' + fpath.split('/')[-1])
