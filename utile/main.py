from langchain_google_genai import ChatGoogleGenerativeAI


def llm_called(msg: str) -> str:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
    res = llm.invoke(msg)

    return str(res.content)
