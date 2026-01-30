import os
import glob
from mcp.server.fastmcp import FastMCP, Context

# Initialize FastMCP server
mcp = FastMCP("ComtorMCP")

# Global Stats Tracking
class GlobalStats:
    files_processed = 0
    chars_read = 0
    chars_written = 0

STATS = GlobalStats()

# --- CONTEXT PROMPT ---
COMTOR_SYSTEM_PROMPT = """
You are a Senior IT Comtor tasked with sequentially and automatically translating technical documentation.

Your Workflow:
1.  Use the tool `list_doc_files` to get a list of files waiting to be translated in the directory.
2.  For each file in the list:
    a.  Use the tool `read_doc_content` to read the original file content.
    b.  Translate that content into 2 versions:
        -   English (save to file index.en.md)
        -   Vietnamese (save to file index.vi.md)
    c.  Use the tool `save_dict_translation` to save the results.
3.  Repeat until the list is empty.

Translation Requirements:
1.  Technical Accuracy: Must use correct IT terminology (e.g., Specification instead of Description, Deployment instead of Moving, Batch job, Latency, etc.).
2.  Professional Tone: Use formal, concise, and easy-to-understand language (Business Level) suitable for both Developers and Stakeholders.
3.  Preserve Structure: If the document contains Markdown formatting, Code snippets, or Tables, keep the format intact. Do not translate code blocks.
4.  Table of Contents & Anchor Links: When translating Headers, you must update the anchor links in the Table of Contents (TOC) at the top of the article to match the translated header (slugify), ensuring users can click to jump to the correct section.
5.  Loan Words (Katakana): For technical Katakana terms, prioritize translating them into their corresponding English terms when translating to Vietnamese (e.g., ログイン -> Login, インフラ -> Infrastructure).
6.  URL & Path: Always keep the original URLs or Paths 100% accurate.
7.  Context Note: If the original sentence is ambiguous, provide 1-2 translation options with a Context note for me to choose.
"""

@mcp.tool()
def list_doc_files(folder_path: str) -> list[str]:
    """
    Scan the folder to find files that need translation.
    """
    if not os.path.exists(folder_path):
        return [f"Error: Path {folder_path} does not exist."]
    
    candidates = []
    # Use glob to find all index.md
    search_path = os.path.join(folder_path, "**", "index.md")
    # Sort to ensure stable file traversal order
    all_files = sorted(glob.glob(search_path, recursive=True))
    
    for f_path in all_files:
        if len(candidates) >= 50:
            break
            
        parent_dir = os.path.dirname(f_path)
        # Check for translation file variants
        en_exists = os.path.exists(os.path.join(parent_dir, "index.en.md"))
        vi_exists = os.path.exists(os.path.join(parent_dir, "index.vi.md"))
        vn_exists = os.path.exists(os.path.join(parent_dir, "index.vn.md")) # Check typo case from requirements

        # Logic: If both target files exist -> Skip this file
        if en_exists and (vi_exists or vn_exists):
            continue
            
        candidates.append(f_path)
        
    return candidates

@mcp.tool()
def read_doc_content(file_path: str) -> str:
    """
    Read the content of a markdown file.
    """
    if not os.path.exists(file_path):
        return f"Error: File {file_path} does not exist."
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Update stats
        STATS.chars_read += len(content)
        return content
    except Exception as e:
        return f"Error reading file: {str(e)}"

@mcp.tool()
def save_dict_translation(original_file_path: str, en_content: str, vi_content: str) -> str:
    """
    Save the translation content (English and Vietnamese) to the corresponding files.
    - index.en.md
    - index.vi.md
    """
    parent_dir = os.path.dirname(original_file_path)
    
    en_path = os.path.join(parent_dir, "index.en.md")
    vi_path = os.path.join(parent_dir, "index.vi.md")
    
    result_msg = []
    
    try:
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(en_content)
        result_msg.append(f"Saved: {en_path}")
    except Exception as e:
        result_msg.append(f"Error saving {en_path}: {str(e)}")
        
    try:
        with open(vi_path, "w", encoding="utf-8") as f:
            f.write(vi_content)
        result_msg.append(f"Saved: {vi_path}")
    except Exception as e:
        result_msg.append(f"Error saving {vi_path}: {str(e)}")
        
    # Update Stats
    STATS.files_processed += 1
    STATS.chars_written += len(en_content) + len(vi_content)
    
    # Log current stats to stderr for visibility
    import sys
    print(f"[ComtorMCP Stats] Processed File #{STATS.files_processed} | Total Chars Read: {STATS.chars_read:,} | Total Chars Written: {STATS.chars_written:,}", file=sys.stderr)
    
    return "\n".join(result_msg)

@mcp.prompt()
def workflow_translation_prompt(folder_path: str) -> list[dict]:
    """
    Trigger the sequential translation process for the entire folder.
    """
    return [{
        "role": "user",
        "content": {
            "type": "text", 
            "text": f"Start the translation process for the folder: {folder_path}\nTarget: Find untranslated index.md files, read content, translate to EN/VI, and save.\n\n{COMTOR_SYSTEM_PROMPT}"
        }
    }]

if __name__ == "__main__":
    mcp.run()
