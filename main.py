from telegram.ext import Application
from telegram.ext import CommandHandler, MessageHandler, filters
from bot.handlers import start, handle_message
from parser.parser_ai import parse_ai_program
from parser.parser_ai_product import parse_ai_product
import config

def main():
    print("🚀 Парсинг данных с сайтов ITMO...")
    ai_data = parse_ai_program()
    ai_product_data = parse_ai_product()

    if not ai_data:
        print("❌ Не удалось распарсить программу AI")
    if not ai_product_data:
        print("❌ Не удалось распарсить программу AI & Product")

    if not ai_data and not ai_product_data:
        print("⛔ Нет данных — бот не может работать.")
        return

    print("✅ Парсинг завершён. Запуск Telegram-бота...")

    # Создаём приложение
    app = Application.builder().token(config.TELEGRAM_TOKEN).build()

    # Подключаем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Бот запущен. Ожидание сообщений...")

    # Запускаем polling
    app.run_polling()

if __name__ == '__main__':
    main()