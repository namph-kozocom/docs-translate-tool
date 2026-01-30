import os

def find_markdown_files(root_folder, recursive=True):
    """
    Recursively find all 'index.md' files in the given directory that need translation.
    Skip if both target files (en/vi) already exist.
    """
    md_files = []
    print(f"Scanning folder: {root_folder}")
    
    if recursive:
        for root, dirs, files in os.walk(root_folder):
            if "index.md" in files:
                file_path = os.path.join(root, "index.md")
                if _needs_translation(file_path):
                    md_files.append(file_path)
    else:
        # Shallow scan
        file_path = os.path.join(root_folder, "index.md")
        if os.path.exists(file_path) and _needs_translation(file_path):
            md_files.append(file_path)
            
    return sorted(md_files)

def _needs_translation(file_path):
    """Check if translation files are missing."""
    parent = os.path.dirname(file_path)
    en_exists = os.path.exists(os.path.join(parent, "index.en.md"))
    vi_exists = os.path.exists(os.path.join(parent, "index.vi.md"))
    # If both exist, skip. If one missing, translate.
    return not (en_exists and vi_exists)

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
        # print(f"Saved: {new_path}")
        return new_path
    except Exception as e:
        print(f"Error saving to {new_path}: {e}")
        return None
