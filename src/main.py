import os
import subprocess
import sys
from git import Repo

def rename(path):
    script = os.path.join(os.path.dirname(__file__), "rename.ps1")
    subprocess.run(["powershell", "-File", script, "-path", path], check = True)

def push(path, msg):
    repo = Repo(path)

    repo.git.add(A = True)
    repo.index.commit(msg)

    origin = repo.remote(name = "origin")
    origin.push()

def process(url, path, msg):
    if not os.path.exists(path):
        Repo.clone_from(url, path)
    rename(path)
    push(path, msg)

if __name__ == "__main__":
    process(*sys.argv[1:4])
