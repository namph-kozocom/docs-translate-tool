import sys
import os
import time
import argparse
from file_manager import find_markdown_files, read_file, save_file
from translator import SafeTranslator

def main():
    parser = argparse.ArgumentParser(description="Translate markdown files in a folder.")
    parser.add_argument("folder", help="Path to the folder containing index.md files")
    args = parser.parse_args()

    target_folder = args.folder
    if not os.path.exists(target_folder):
        print(f"Error: Folder '{target_folder}' does not exist.")
        sys.exit(1)

    # Initialize translator
    translator = SafeTranslator()
    
    start_time = time.time()

    # Find files
    files = find_markdown_files(target_folder)
    if not files:
        print("No index.md files found.")
        sys.exit(0)

    print(f"Found {len(files)} files to translate.")

    # Process each file
    for i, file_path in enumerate(files):
        print(f"\n[{i+1}/{len(files)}] Processing: {file_path}")
        
        content = read_file(file_path)
        if not content:
            continue

        # 1. Translate to English
        print(" -> Targeting English (en)...")
        en_content = translator.translate(content, dest='en', src='ja') # assuming source is Japanese based on context, or use 'auto'
        save_file(file_path, 'en', en_content)

        # 2. Translate to Vietnamese
        print(" -> Targeting Vietnamese (vi)...")
        vi_content = translator.translate(content, dest='vi', src='ja')
        save_file(file_path, 'vi', vi_content)
        
    end_time = time.time()
    duration = end_time - start_time
    
    print("\nAll done!")
    print("\n--- Translation Summary ---")
    print(f"Total Time:      {duration:.2f} seconds")
    print(f"Total Files:     {len(files)}")
    print(f"Total Chars:     {translator.total_chars_translated:,}")
    print(f"Estimated Cost:  $0.00 (Free)")
    print("---------------------------")

if __name__ == "__main__":
    main()
