# Project Constitution (gemini.md)

## Data Schemas

### 1. Converter Request (Input)
```json
{
  "source_code": "string",       // The raw Selenium Java code from the UI
  "target_language": "string",   // 'typescript' or 'javascript'
  "framework"; "string"          // 'playwright' logic (default)
}
```

### 2. Converter Response (Output)
```json
{
  "converted_code": "string",    // The generated Playwright code
  "explanation": "string",       // Brief summary of changes/logic
  "status": "success | error",
  "error_message": "string | null"
}
```

## Behavioral Rules
1. **Data-First Rule**: Define Data Schema before building tools.
2. **Self-Annealing**: Analyze -> Patch -> Test -> Update Architecture.
3. **Deliverables**: 
    - **Display**: Show full code in the Web UI.
    - **Persist**: Save converted files to a `converted_output/` directory on the backend.
4. **UI/UX Standard**: **Streamlit** (Python-only Web UI) to bypass missing Node.js environment.
5. **LLM Logic**: 
    - Use locally pulled `codellama` model.
    - **Prioritize Reliability**: Output idiomatic Playwright (e.g., auto-waiting) rather than strict 1:1 Java translation.

## Architectural Invariants
- **Frontend/Backend**: Streamlit (Port 8501) - Single unified Python process.
- **Bridge**: `tools/ollama_client.py` - Handles `codellama` API calls.
- **State**: `st.session_state` for frontend, temporary files for backend storage.
