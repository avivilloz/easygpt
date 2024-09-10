import os


def printnl(text: str):
    print(f"{text}\n")


def create_dir(dir_path):
    os.makedirs(dir_path, exist_ok=True)
