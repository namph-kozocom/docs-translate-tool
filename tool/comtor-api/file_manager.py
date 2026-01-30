import os

def find_markdown_files(root_folder):
    """
    Recursively find all 'index.md' files in the given directory.
    """
    md_files = []
    print(f"Scanning folder: {root_folder}")
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file == "index.md":
                md_files.append(os.path.join(root, file))
    return md_files

def read_file(file_path):
    """Read content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def save_file(original_path, lang_suffix, content):
    """
    Save the translated content to a new file.
    Example: index.md -> index.en.md
    """
    directory = os.path.dirname(original_path)
    filename = os.path.basename(original_path)
    name, ext = os.path.splitext(filename)
    
    new_filename = f"{name}.{lang_suffix}{ext}"
    new_path = os.path.join(directory, new_filename)
    
    try:
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Saved: {new_path}")
        return new_path
    except Exception as e:
        print(f"Error saving to {new_path}: {e}")
        return None
