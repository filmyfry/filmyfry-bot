from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

TOKEN = "8963258868:AAEfxE_8jbbYiL7jgRKXb-mPiOP5evidJtc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        ["🎬 Latest Movies", "🔥 Trending"],
        ["🎥 Hollywood", "🍿 Bollywood"],
        ["📺 Web Series", "🔍 Search"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        buttons,
        resize_keyboard=True
    )

    text = """
🔥 Welcome To FilmyFry Bot 🔥

🎥 Hollywood Movies
🍿 Bollywood Movies
📺 Web Series
🔥 Trending Content

👇 Choose an option below
"""

    await update.message.reply_text(
        text,
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    if msg == "🎬 Latest Movies":
        await update.message.reply_text(
            "🎬 Latest Movies Coming Soon..."
        )

    elif msg == "🔥 Trending":
        await update.message.reply_text(
            "🔥 Trending Movies Coming Soon..."
        )

    elif msg == "🎥 Hollywood":
        await update.message.reply_text(
            "🎥 Hollywood Section Coming Soon..."
        )

    elif msg == "🍿 Bollywood":
        await update.message.reply_text(
            "🍿 Bollywood Section Coming Soon..."
        )

    elif msg == "📺 Web Series":
        await update.message.reply_text(
            "📺 Web Series Section Coming Soon..."
        )

    elif msg == "🔍 Search":
        await update.message.reply_text(
            "🔍 Send movie name to search..."
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("✅ FilmyFry Bot Running...")
app.run_polling()
