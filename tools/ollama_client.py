import requests
import json

class OllamaClient:
    def __init__(self, model="codellama", base_url="http://localhost:11434/api"):
        self.model = model
        self.base_url = base_url

    def convert_selenium_to_playwright(self, source_code, target_language="typescript"):
        prompt = f"""
        You are an expert test automation engineer. 
        Convert the following Selenium Java (TestNG) code into Playwright {target_language}.
        
        Rules:
        1. Prioritize readability and idiomatic Playwright patterns (like auto-waiting, locators).
        2. Do not do a strict 1:1 mapping if a better Playwright way exists.
        3. Convert everything, including setup/teardown if present.
        4. Return ONLY the code, no markdown blocks, no explanations.
        
        Selenium Java Code:
        {source_code}
        """
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(f"{self.base_url}/generate", json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "").strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def explain_conversion(self, source_code, converted_code):
        prompt = f"""
        Explain the key changes made during the conversion from Selenium Java to Playwright.
        Focus on how locators, waits, and assertions were handled.
        
        Original Code:
        {source_code}
        
        Converted Code:
        {converted_code}
        """
        
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        
        try:
            response = requests.post(f"{self.base_url}/generate", json=payload)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "").strip()
        except Exception as e:
            return f"Error: {str(e)}"
