from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8239626127:AAGAxvnro-8l0pEJjYWwXbkElFbPWB0XiFg"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("приветик мой сладкий фембойчик;)")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()
