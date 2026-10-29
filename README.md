# Ghost Story Generator 👻

A small Python + Streamlit app that creates spooky stories using the open-weight **Qwen2.5-3B-Instruct** model through Hugging Face's hosted inference API. The model runs on the provider's infrastructure, not on your laptop, so you do not need to download a large model locally.

## Run it

1. Install Python if needed.
2. In this folder, install packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a Hugging Face access token: https://huggingface.co/settings/tokens
4. Set the token as an environment variable named `HF_TOKEN`. Do not publish the token or put it in GitHub.
5. Start the app:
   ```bash
   streamlit run app.py
   ```

Inference access, quotas, and availability can vary by Hugging Face account and provider.

## Why open innovation matters

This project uses an open-weight model rather than hard-coding a closed model into the app. That makes it possible to inspect the model's license and documentation, experiment with alternatives, and build a small application around an openly available model. In this version, prompts are sent to a hosted inference provider, so it is **not fully offline** and prompts are processed by that provider.

## Tech

- Python
- Streamlit
- Hugging Face Inference API
- Qwen2.5-3B-Instruct
