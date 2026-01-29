import streamlit as st
import os
import time
from tools.ollama_client import OllamaClient

# Page configuration
st.set_page_config(
    page_title="Selenium to Playwright Converter",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium look
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextArea textarea {
        background-color: #1e2227;
        color: #ffffff;
        border: 1px solid #3e4451;
        font-family: 'Source Code Pro', monospace;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }
    .header-style {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle-style {
        font-size: 18px;
        color: #8b949e;
        text-align: center;
        margin-bottom: 40px;
    }
    .stCodeBlock {
        border: 1px solid #3e4451;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/3f/Selenium_logo.svg", width=50)
    st.title("Settings")
    model_name = st.selectbox("LLM Model", ["codellama", "llama3.2"], index=0)
    target_lang = st.radio("Target Language", ["Typescript", "Javascript"], index=0)
    
    st.divider()
    st.info("Ensure Ollama is running locally with the selected model.")

# Header
st.markdown('<div class="header-style">B.L.A.S.T. Converter</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-style">Seamlessly migrate your Selenium Java tests to Modern Playwright</div>', unsafe_allow_html=True)

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Selenium Java (TestNG)")
    source_code = st.text_area("Paste your Java code here...", height=500, placeholder="public class Test { ... }")

with col2:
    st.subheader("🚀 Playwright " + target_lang)
    if 'converted_code' not in st.session_state:
        st.session_state.converted_code = ""
    
    placeholder = st.empty()
    if st.session_state.converted_code:
        placeholder.code(st.session_state.converted_code, language=target_lang.lower())
    else:
        placeholder.info("Converted code will appear here...")

# Action Button
if st.button("✨ Convert Now"):
    if not source_code:
        st.warning("Please enter some Selenium code first!")
    else:
        with st.spinner(f"Converting using {model_name}..."):
            client = OllamaClient(model=model_name)
            
            # Simulated progress for UI feel
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            
            result = client.convert_selenium_to_playwright(source_code, target_lang.lower())
            
            if result.startswith("Error:"):
                st.error(result)
            else:
                st.session_state.converted_code = result
                placeholder.code(result, language=target_lang.lower())
                
                # Persistence
                output_dir = "converted_output"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                
                filename = f"converted_test_{int(time.time())}.{ 'ts' if target_lang == 'Typescript' else 'js' }"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "w") as f:
                    f.write(result)
                
                st.success(f"Converted successfully! Saved to `{filepath}`")
                
                # Explanation
                with st.expander("📝 View Conversion Logic"):
                    explanation = client.explain_conversion(source_code, result)
                    st.write(explanation)

# Footer
st.divider()
st.markdown('<div style="text-align: center; color: #8b949e;">Powered by Ollama + Codellama | Built with Streamlit</div>', unsafe_allow_html=True)
