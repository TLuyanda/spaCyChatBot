### **3. `job_helper_bot.py`**


from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import os
from dotenv import load_dotenv

load_dotenv()

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    update.message.reply_text("Hello! I'm JobHelperBot. How can I assist you with your job application today?")

def resume_assistance(update: Update, context: CallbackContext) -> None:
    """Provide resume tips."""
    tips = [
        "Tailor your resume to the job you're applying for.",
        "Use action verbs to describe your achievements.",
        "Keep your resume concise and focused on relevant experience.",
        "Include measurable accomplishments rather than just duties."
    ]
    update.message.reply_text(random.choice(tips))

def interview_preparation(update: Update, context: CallbackContext) -> None:
    """Provide interview tips."""
    tips = [
        "Research the company and role before the interview.",
        "Practice common interview questions.",
        "Prepare questions to ask the interviewer.",
        "Dress appropriately for the interview."
    ]
    update.message.reply_text(random.choice(tips))

def career_advice(update: Update, context: CallbackContext) -> None:
    """Provide general career advice."""
    advice = [
        "Network with professionals in your industry.",
        "Keep learning and improving your skills.",
        "Set clear career goals and work towards them.",
        "Seek mentorship from experienced professionals."
    ]
    update.message.reply_text(random.choice(advice))

def main() -> None:
    """Start the bot."""
    updater = Updater(os.getenv('API_TOKEN'), use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("resume", resume_assistance))
    dp.add_handler(CommandHandler("interview", interview_preparation))
    dp.add_handler(CommandHandler("advice", career_advice))

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, lambda update, context: update.message.reply_text("Sorry, I didn't understand that. Please use /resume, /interview, or /advice.")))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()