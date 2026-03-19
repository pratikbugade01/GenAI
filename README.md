# GenAI

A hands-on LangChain learning repository covering chat models, embeddings, prompts, chains, retrievers, and more.

## Chat Model Examples (`2.Chat_models/`)

| File | Model |
|------|-------|
| `Anthropic_chatmodel.py` | Anthropic Claude (`claude-sonnet-4-5`) via `langchain-anthropic` |
| `GeminiAI_chatmodel.py` | Google Gemini (`gemini-2.5-flash`) via `langchain-google-genai` |
| `Huggingface_chatmodel_API.py` | Meta Llama via HuggingFace Inference API (`langchain-huggingface`) |

### Prerequisites

Set the required API keys in a `.env` file at the project root:

```
ANTHROPIC_API_KEY=your_anthropic_key   # for Anthropic Claude
GOOGLE_API_KEY=your_google_key         # for Google Gemini
HF_TOKEN=your_huggingface_token        # for HuggingFace models
```

Install dependencies:

```bash
pip install -r requirements.txt
```