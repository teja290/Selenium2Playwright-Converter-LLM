# Findings

## Architectural Decisions
- **Stack Update**: Streamlit only.
- **Reasoning**: User machine lacks `npm`, making React impossible without extensive setup. Streamlit provides the required Web UI using existing Python environment.
- **Model**: User explicitly requested `codellama`.

## Constraints
- **Local Environment**: Python only.
- **Ollama**: Must have `codellama` pulled.
- **File System**: `converted_output/` required.
