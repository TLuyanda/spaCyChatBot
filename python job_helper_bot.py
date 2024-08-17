#!/usr/bin/env python3

from telegram import (Update)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random
import spacy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load spaCy model
nlp = spacy.load('en_core_web_sm')


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


def analyze_message(update: Update, context: CallbackContext) -> None:
    """Analyze the user's message and provide feedback."""
    user_message = update.message.text
    doc = nlp(user_message)

    # Example: Extract named entities
    entities = [ent.text for ent in doc.ents]
    if entities:
        update.message.reply_text(f"I noticed these entities in your message: {', '.join(entities)}.")
    else:
        update.message.reply_text("I didn't find any specific entities in your message.")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token
    updater = Updater(os.getenv('API_TOKEN'), use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("resume", resume_assistance))
    dp.add_handler(CommandHandler("interview", interview_preparation))
    dp.add_handler(CommandHandler("advice", career_advice))

    # Message handler with spaCy analysis
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, analyze_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()


if __name__ == '__main__':
    main()
