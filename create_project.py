import os
import argparse
from rich.console import Console 
from rich.prompt import Prompt, IntPrompt
from templates import get_index_html, get_styles_css, get_scripts_js, get_readme_md, get_git_gitignore
import utils

console = Console()

def main():
    parser = argparse.ArgumentParser(description='Setup a new web development project.')
    parser.add_argument('project_name', help='The name of the project')
    parser.add_argument('-t', '--template', type=int, choices=[1, 2 ,3], default=1,
                        help='Template choice: 1 for Basic, 2 for Intermediate, 3 for Advanced')
    
    args = parser.parse_args()

    project_name = args.project_name
    template_choice = args.template

    base_path = os.path.join(os.getcwd(), project_name)

    console.print(f"Creating project: [bold cyan]{project_name}[/bold cyan]", style="green")
    console.print(f"Using template: [bold yellow]{template_choice}[/bold yellow]", style="green")

    # Creating a namespace for templates to pass them around
    class Templates:
        get_index_html = staticmethod(get_index_html)
        get_styles_css = staticmethod(get_styles_css)
        get_scripts_js = staticmethod(get_scripts_js)
        get_readme_md = staticmethod(get_readme_md)
        get_git_gitignore = staticmethod(get_git_gitignore)

    utils.create_directory_structure(base_path, project_name, Templates)
    utils.initialize_git_repo(base_path, Templates)

    console.print(f"Project '{project_name}' created successfully at {base_path}", style="bold green")


if __name__ == '__main__':
    main()
