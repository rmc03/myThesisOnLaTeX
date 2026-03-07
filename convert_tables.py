import re

files = [
    'd:/Universidad/Tesis/Thesis_template fix/Chapter1.tex',
    'd:/Universidad/Tesis/Thesis_template fix/Chapter2.tex'
]

# We want to find blocks like:
# \begin{table}[H]
# ...
# \begin{tabular}{...}
# ...
# \end{tabular}
# \end{table}
# And replace with:
# \begin{longtable}{...}
# ...
# \end{longtable}
# But we must preserve the \caption and \label, moving them inside \begin{longtable}

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find table environments
    pattern = re.compile(r'\\begin\{table\}.*?(?=\\begin\{table\}|\\end\{document\}|$)', re.DOTALL)
    
    # We will just do a simpler state-machine approach
    lines = content.split('\n')
    out_lines = []
    
    in_table = False
    in_tabular = False
    table_lines = []
    
    for line in lines:
        if '\\begin{table}' in line:
            in_table = True
            table_lines = []
        elif '\\end{table}' in line and in_table:
            in_table = False
            
            # Process table_lines
            # Extract caption, label, centering, small, arraystretch, etc.
            caption = ""
            tabular_start = ""
            tabular_body = []
            pre_tabular = []
            
            # Find boundaries
            tab_start_idx = -1
            tab_end_idx = -1
            for i, tl in enumerate(table_lines):
                if '\\begin{tabular}' in tl:
                    tab_start_idx = i
                elif '\\end{tabular}' in tl:
                    tab_end_idx = i
                    
                if '\\caption' in tl:
                    caption = tl
            
            if tab_start_idx != -1 and tab_end_idx != -1:
                # We have a valid table to convert!
                # Extract the columns definition from \begin{tabular}{...}
                m = re.search(r'\\begin\{tabular\}(\{.*?\})', table_lines[tab_start_idx])
                cols = m.group(1) if m else "{|c|}"
                
                # Add pre-tabular stuff (like \small, \renewcommand) except \centering and \caption
                for i in range(tab_start_idx):
                    if '\\caption' not in table_lines[i] and '\\centering' not in table_lines[i] and '\\begin{table}' not in table_lines[i]:
                        if table_lines[i].strip():
                            out_lines.append(table_lines[i])
                
                # Start longtable
                out_lines.append(f'\\begin{{longtable}}{cols}')
                
                # Add caption if exists
                if caption:
                    out_lines.append(caption + r' \\')
                
                # Add body
                for i in range(tab_start_idx + 1, tab_end_idx):
                    out_lines.append(table_lines[i])
                    
                # End longtable
                out_lines.append('\\end{longtable}')
                
            else:
                # Not a standard tabular inside, just dump it back
                out_lines.append('\\begin{table}[H]')
                out_lines.extend(table_lines)
                out_lines.append('\\end{table}')
                
        elif in_table:
            table_lines.append(line)
        else:
            out_lines.append(line)
            
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out_lines))
    print(f'Converted {fpath}')
