import os
from flask import Flask, render_template

app = Flask(__name__)

# Base directory where markdown files are stored
BASE_DIR = './docs'

# Helper function to get files and folders in the directory
def get_files_and_folders(directory):
    items = []
    for entry in os.scandir(directory):
        if entry.is_dir():
            items.append({
                'type': 'folder',
                'name': entry.name,
                'contents': get_files_and_folders(entry.path)
            })
        else:
            items.append({
                'type': 'file',
                'name': entry.name
            })
    return items

@app.route('/')
def index():
    # Get all files and folders under BASE_DIR
    files_and_folders = get_files_and_folders(BASE_DIR)
    return render_template("index.html", files_and_folders=files_and_folders)

@app.route('/view/<path:filename>')
def view_file(filename):
    try:
        # Get the full path to the file
        file_path = os.path.join(BASE_DIR, filename)
        with open(file_path, "r") as f:
            content = f.read()
        # Get all files and folders again to render the sidebar
        files_and_folders = get_files_and_folders(BASE_DIR)
        return render_template("index.html", content=content, filename=filename, files_and_folders=files_and_folders)
    except Exception as e:
        return f"Error loading file: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
