import os

def create_folders():

    folders = [
        "reports",
        "images",
        "outputs",
        "docs"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)