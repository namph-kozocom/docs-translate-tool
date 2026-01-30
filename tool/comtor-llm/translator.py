import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

class LLMTranslator:
    def __init__(self, model="gpt-4o"):
        self.model = model
        self.input_tokens = 0
        self.output_tokens = 0

    def translate(self, content, target_lang):
        """
        Translates Markdown content to the target language using an LLM.
        """
        # Map simple language codes to full names for better prompting
        lang_map = {
            'en': 'English',
            'vi': 'Vietnamese',
            'ja': 'Japanese'
        }
        full_lang = lang_map.get(target_lang, target_lang)

        prompt = f"""You are a professional technical translator.
Translate the following Markdown content into {full_lang}.
Keep technical terms, code blocks, and proper nouns unchanged.
Maintain the original Markdown formatting exactly.
Do not add any explanations, just return the translated content.

Content:
{content}
"""
        
        try:
            response = completion(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            
            translated_text = response.choices[0].message.content
            
            # Track token usage
            if hasattr(response, 'usage'):
                self.input_tokens += response.usage.prompt_tokens
                self.output_tokens += response.usage.completion_tokens
            
            return translated_text
            
        except Exception as e:
            print(f"Translation error: {e}")
            return content  # Return original if failed

    def get_token_usage(self):
        return {
            "input": self.input_tokens,
            "output": self.output_tokens,
            "total": self.input_tokens + self.output_tokens
        }
