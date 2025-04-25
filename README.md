# TELEGRAM-CHATBOT-WITH-LANGCHAIN

## 🧱 Tech Stack

- **Telegram**: Bot platform  
- **[Pyrogram](https://docs.pyrogram.org/)**: Telegram Bot framework  
- **Google Gemini**: Generative AI API  
- **LangChain**: Language model orchestration  
- **[uv](https://docs.astral.sh/uv/getting-started/installation)**: Python package manager  

---

## 🚀 How to Run

### 1. Clone the Project

```bash
git clone https://github.com/thedhruvish/telegram-chatbot-with-langchain
cd telegram-chatbot-with-langchain
```

### 2. Set Environment Variables

Rename `env.example` to `.env` and fill in the values:

```env
# @BotFather
BOT_TOKEN=

# From https://my.telegram.org
API_ID=
API_HASH=

# From https://aistudio.google.com/app/apikey
GOOGLE_API_KEY=
```

---

## 📦 Install Dependencies

Make sure `uv` is installed. If not, install it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then run the app:

```bash
uv main.py
```

---

## 🔐 Credentials Setup Guide

### 🤖 1. Get Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)  
2. Start the chat and run `/start`  
3. Create your bot by:
   - Setting a **name**
   - Choosing a **username** (must end with `bot`)  
4. Copy the **Bot Token** provided – keep it safe!

---

### 📱 2. Get Telegram API ID and API Hash

1. Visit [my.telegram.org](https://my.telegram.org)  
2. Log in with your Telegram phone number  
3. Go to **API Development Tools**  
4. Fill out the form:
   - **App title**: e.g., `MyBotApp`  
   - **Short name**: e.g., `botapp`  
5. Copy your **API ID** and **API Hash**

---

### 🌟 3. Get a Gemini API Key (Google Generative AI)

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)  
2. Sign in with your Google account  
3. Click your profile icon → **Create API Key**  
4. Copy the generated key

---


## 👤 Author

- **Dhruvish** – [GitHub](https://github.com/thedhruvish)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).