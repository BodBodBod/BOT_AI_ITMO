from telegram import Update
from telegram.ext import ContextTypes
from llm.rag_retriever import find_relevant_context
from llm.llm_client import call_yandexgpt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я помогу тебе с выбором магистерской программы в ITMO.\n"
        "Спроси, например:\n"
        "— Какие курсы по выбору на 2 семестре в AI?\n"
        "— Чем отличается AI от AI и Product?\n"
        "— Что посоветуешь, если я разработчик?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text
    context_data = find_relevant_context(user_query)

    system_prompt = (
        "Ты — помощник абитуриенту ITMO. Отвечай только на основе предоставленного контекста. "
        "Не выдумывай. Если информации нет, скажи: 'Я не нашёл такой информации в учебных планах.'"
    )

    full_prompt = f"Контекст:\n{context_data}\n\nВопрос: {user_query}"

    response = call_yandexgpt(system_prompt, full_prompt)
    await update.message.reply_text(response)