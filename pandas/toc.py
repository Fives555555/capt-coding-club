import json, urllib.parse

def generate_toc(notebook_path):
    with open(notebook_path) as f:
        nb = json.load(f)
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            for line in cell['source']:
                line = line.strip()
                if line.startswith('#'):
                    level = line.count('#')
                    title = line.lstrip('#').strip()
                    url = urllib.parse.quote(title.replace(' ', '-'))
                    print('  ' * (level-1) + f'- {title} ')

generate_toc('07-pandas-plotting.ipynb')
