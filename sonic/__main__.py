import os 
import sys 
import argparse 
import yaml
import click
import time
from colorama import Fore, Style

BASE_DIR = os.path.dirname(__file__)

filemap = yaml.load(open(os.path.join(BASE_DIR, "filemap.yaml")), Loader = yaml.FullLoader)["filemap"]

skeleton_dir =  os.path.join(BASE_DIR, "skeleton")

# ap = argparse.ArgumentParser()

# # ap.add_argument("-n", "--name", required = True, help = "Enter app name i.e todoapp")
# # ap.add_argument("-e", "--env", required = False, default = False, help = "Do you want to create a virtual environment ?")

# args = vars(ap.parse_args())

class Generator:
    def __init__(self, name):
        self.name = name

    @staticmethod 
    def create_dir(name):
        try:
            os.makedirs(name)
        except OSError as err:
            raise err
            sys.exit()

    @staticmethod
    def load_file_content(path):
        file_path = os.path.join(skeleton_dir, path)
        content = ""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except (Exception, OSError) as err:
            raise err
            sys.exit() 
        
        return content

    @staticmethod 
    def create_virtual_environment():
        print("[PROCESS] :- Creating Virtual Environment ......")
        try:
            os.system("python -m venv env")
            if not os.path.isdir("env"):
                os.system("python3 -m venv env")
            print("[DONE] : Created Virtual environment.")
            print("""TO GET STARTED :- \n 
            (1). Change working directory to app \n

            (2). Activate the virtual environment i.e \n
                $ source activate env/bin/activate (for ubuntu) \n

            (3). Install the requirements i.e. \n
                $ pip install -r requirements.txt \n

            (4). Run the app server i.e. \n
                $ python3 main.py \n
            Voila !
            """)
        except Exception as err:
            print(err)

    def init_app(self):
        self.create_dir(self.name)
        os.chdir(self.name)
        # if args["env"]:
        #     self.create_virtual_environment()
        
    
    def create_dirs(self):
        for dirname in filemap["dirs"]:
            self.create_dir(dirname)

    def create_files(self):
        for file in filemap["dir_files"]:
            with open(file, "w") as f:
                filedata = self.load_file_content(file) 
                f.write(filedata)

        for file in filemap["local_files"]:
            with open(file, "w") as f:
                filedata = self.load_file_content(file) 
                f.write(filedata)

@click.group()
@click.version_option("1.0.0")
def main():
    """SONIC GENERATOR :- A FastAPI project directory generator"""
    pass

@main.command()
@click.argument('name', required=True)
def generate(**kwargs):
    name = kwargs.get("name")
    g = Generator(name)
    start = time.time()
    g.init_app()
    g.create_dirs()
    g.create_files()
    end = time.time()
    click.echo(f"{Fore.GREEN}App generated in {(end - start)} seconds, Voila !{Style.RESET_ALL}")
    click.echo("To Run the app :- ")
    click.echo("")
    click.echo(f"{Fore.GREEN}${Style.RESET_ALL} cd <app-name>")
    click.echo(f"{Fore.GREEN}${Style.RESET_ALL} python main.py")
    click.echo("")
    click.echo(f"{Fore.GREEN}---------------------------------------------------{Style.RESET_ALL}")
    click.echo(f"{Fore.GREEN}Thanks for using Sonic Generator, Build something amazing.{Style.RESET_ALL}")
    
if __name__ == "__main__":
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Please enter app name i.e generate <app-name>")
    main()
