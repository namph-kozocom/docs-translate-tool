import os
import sys
import fire
from tqdm import tqdm
from file_manager import find_markdown_files, read_file, save_file
from translator import LLMTranslator

def main(folder, model="gpt-4o", verbose=False):
    """
    Comtor LLM Translation Tool.
    
    Args:
        folder (str): Path to the folder to scan for index.md files.
        model (str): Name of the LLM model to use (default: gpt-4o).
        verbose (bool): Print detailed logs.
    """
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        sys.exit(1)

    print(f"Initializing translator with model: {model}")
    translator = LLMTranslator(model=model)

    files = find_markdown_files(folder)
    if not files:
        print("No index.md files found needing translation.")
        sys.exit(0)

    print(f"Found {len(files)} files to translate.")

    pbar = tqdm(files, desc="Translating Files", unit="file")
    
    for file_path in pbar:
        relative_path = os.path.relpath(file_path, folder)
        pbar.set_postfix_str(f"Processing: {relative_path[:30]}...")
        
        content = read_file(file_path)
        if not content:
            continue

        # Translate to English
        en_content = translator.translate(content, target_lang='en')
        save_file(file_path, 'en', en_content)
        
        # Translate to Vietnamese
        vi_content = translator.translate(content, target_lang='vi')
        save_file(file_path, 'vi', vi_content)

    print("\nTranslation completed successfully!")
    
    # Print Token Usage Stats
    usage = translator.get_token_usage()
    print("\n--- Token Usage Summary ---")
    print(f"Total Input Tokens:  {usage['input']:,}")
    print(f"Total Output Tokens: {usage['output']:,}")
    print(f"Total Tokens Used:   {usage['total']:,}")
    print("---------------------------")

if __name__ == "__main__":
    fire.Fire(main)
