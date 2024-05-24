import os
import subprocess
from rich.console import Console

console = Console()

def create_directory_structure(base_path, project_name, templates):
    directories = ['css','js','img']

    # Create base directory
    os.makedirs(base_path, exist_ok=True)
    console.print(f"[bold green]Created directory:[/bold green] {base_path}")

    # Create subdirectories
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        console.print(f"[bold green]Created subdirectory:[/bold green] {dir_path}")

    # Create file with dynamic content
    files = {
        'index.html': templates.get_index_html(project_name),
        'css/styles.css': templates.get_styles_css(),
        'js/scripts.js': templates.get_scripts_js(),
        'README.md': templates.get_readme_md(project_name)
    }

    for file_name, content in files.items():
        file_path = os.path.join(base_path, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
        console.print(f"[bold green]Created file:[/bold green] {file_path}")

def initialize_git_repo(base_path, templates):
        # Initialize git repository
        subprocess.run(['git', 'init', base_path], check=True)
        console.print(f"[bold green]Initialized git repository in:[/bold green] {base_path}")

        # Create .gitignore file
        gitignore_contents = templates.get_git_gitignore()

        with open(os.path.join(base_path, '.gitignore'), 'w') as file:
            file.write(gitignore_contents)
        console.print(f"[bold green]Created .gitignore file in:[/bold green] {base_path}")