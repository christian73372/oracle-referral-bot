from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start käsule vastamine
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Write @TheOraclesChris 🏆", url="https://t.me/TheOraclesChris")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        'Great! 🔥 Click the button below to write @TheOraclesChris "LINK" for your link to invite 3 friends to get 1 month free in our exclusive community ⬇️⬇️⬇️',
        reply_markup=reply_markup
    )

# Bot käivitub siit
app = ApplicationBuilder().token("7858518365:AAHhjtN7NSo8A3uTSM2LlvR96gyC2KCr9fI").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()


