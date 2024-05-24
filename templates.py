def get_index_html(project_name):
    return f'''<!DOCTYPE html>
    <html>
    <head>
    <title>{project_name}</title>
    <link rel="stylesheet" type="text/css" href="css/styles.css">
    </head>
    <body>

    <script src="js/script.js"></script>
    </body>
    <html>'''

def get_styles_css():
    return '/* Add your styles here */'

def get_scripts_js():
    return '// Add your scripts here'

def get_readme_md(project_name):
    return f'# {project_name}\n\nProject description goes here.'

def get_git_gitignore():
    return f'''nodemodules/
    dist/
    .env
    '''