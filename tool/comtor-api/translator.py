import time
import random
from googletrans import Translator

class SafeTranslator:
    def __init__(self):
        self.translator = Translator()
        self.max_chunk_size = 3000  # Conservative limit (well below 5000)
        self.total_chars_translated = 0

    def _chunk_text(self, text):
        """
        Split text into chunks smaller than max_chunk_size, 
        preserving logical structure where possible (split by lines).
        """
        if len(text) <= self.max_chunk_size:
            return [text]
        
        chunks = []
        current_chunk = []
        current_length = 0
        
        lines = text.split('\n')
        
        for line in lines:
            line_len = len(line) + 1 # +1 for newline
            
            if current_length + line_len > self.max_chunk_size:
                # If a single line is too long, we might have to split it forcedly
                # But for markdown usually lines are manageable.
                # If current chunk is not empty, flush it.
                if current_chunk:
                    chunks.append('\n'.join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                # If the line itself is super long, we might need more aggressive splitting,
                # but let's assume lines fit for now or just let it exceed slightly if it's one line.
                # Here we just start a new chunk with this line.
                current_chunk.append(line)
                current_length += line_len
            else:
                current_chunk.append(line)
                current_length += line_len
                
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
            
        return chunks

    def translate(self, text, dest='en', src='auto'):
        """
        Translate text with chunking and rate limiting.
        """
        if not text:
            return ""

        chunks = self._chunk_text(text)
        translated_chunks = []
        
        print(f"Translating {len(text)} chars in {len(chunks)} chunks to '{dest}'...")
        self.total_chars_translated += len(text)

        for i, chunk in enumerate(chunks):
            if not chunk.strip():
                translated_chunks.append(chunk)
                continue

            try:
                # Add delay to be nice to the API
                wait_time = random.uniform(1.0, 3.0)
                if i > 0:
                    print(f"  Waiting {wait_time:.1f}s before next chunk...")
                    time.sleep(wait_time)
                
                # Perform translation
                result = self.translator.translate(chunk, dest=dest, src=src)
                translated_chunks.append(result.text)
                
            except Exception as e:
                print(f"Error translating chunk {i+1}: {e}")
                # Fallback: append original text context to avoid losing data
                translated_chunks.append(f"[Translation Failed] {chunk}")
                # If we hit strict rate limit, we might want to wait longer
                time.sleep(5) 

        return '\n'.join(translated_chunks)
