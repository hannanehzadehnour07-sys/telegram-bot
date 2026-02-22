import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
from telegram.request import HTTPXRequest

logging.basicConfig(level=logging.INFO)

(
    PROFESSOR,
    COURSE,
    GROUP,
    FACULTY,
    ASSIGNMENT,
    TEACHING_RESOURCES,
    EXAM_RESOURCES,
    RESOURCES_ENOUGH,
    GRADE_INCREASE,
    GRADING,
    MY_GRADE,
    ETHICS,
    ATTENDANCE_IMPORTANCE,
    PROFESSOR_ATTENDANCE,
    CLASS_STYLE,
    CONTACT,
    EXTRA,
) = range(17)

TOKEN = "8397063236:AAEj_lqJHivkQ-DaE_7CulJgAZNDMjXDSMQ"
ADMIN_ID = 7373612882


# ---------------- START ----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    welcome_text = (
        "🎓 به بات معرفی اساتید دانشگاه تخصصی فناوری‌های نوین خوش آمدید.\n\n"
        "این بات برای معرفی و ثبت تجربه دانشجویان درباره اساتید طراحی شده است.\n"
        "📝 هدف ما کمک به انتخاب آگاهانه‌تر واحدهای درسی است.\n\n"
        "🔒 تمامی نظرات به‌صورت کاملاً ناشناس ارسال می‌شوند.\n"
        "📩 در پایان، یک نسخه از پاسخ‌های شما برای خودتان نیز ارسال خواهد شد.\n\n"
        "🙏 ممنون می‌شویم با دقت و صداقت به سوالات پاسخ دهید و با ما همکاری کنید."
    )

    # پیام اول: خوشامدگویی
    await update.message.reply_text(welcome_text)

    # پیام دوم: شروع فرم
    await update.message.reply_text("👨‍🏫 لطفاً نام استاد را وارد کنید:")

    return PROFESSOR


async def get_professor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["professor"] = update.message.text
    await update.message.reply_text("📚 نام درس را وارد کنید:")
    return COURSE


async def get_course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["course"] = update.message.text
    await update.message.reply_text("🏷 گروه درسی را وارد کنید:")
    return GROUP


async def get_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["group"] = update.message.text
    await update.message.reply_text("🏫 دانشکده را وارد کنید:")
    return FACULTY


async def get_faculty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["faculty"] = update.message.text
    await update.message.reply_text("📝 تکلیف یا تمرین چگونه بود؟")
    return ASSIGNMENT


async def get_assignment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["assignment"] = update.message.text
    await update.message.reply_text("📚 منابع تدریس چه بود؟")
    return TEACHING_RESOURCES


async def get_teaching_resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["teaching_resources"] = update.message.text
    await update.message.reply_text("📖 منابع امتحان چه بود؟")
    return EXAM_RESOURCES


async def get_exam_resources(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["exam_resources"] = update.message.text
    await update.message.reply_text("❓ آیا منابع معرفی شده برای امتحان کافی بود؟")
    return RESOURCES_ENOUGH


async def get_resources_enough(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["resources_enough"] = update.message.text
    await update.message.reply_text("📊 آیا امکان افزایش نمره با تحقیق یا فعالیت وجود داشت؟")
    return GRADE_INCREASE


async def get_grade_increase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["grade_increase"] = update.message.text
    await update.message.reply_text("⭐ نحوه نمره‌دهی چگونه بود؟")
    return GRADING


async def get_grading(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["grading"] = update.message.text
    await update.message.reply_text("🎯 نمره شما چند شد؟")
    return MY_GRADE


async def get_my_grade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["my_grade"] = update.message.text
    await update.message.reply_text("🙂 اخلاق استاد چگونه بود؟")
    return ETHICS


async def get_ethics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["ethics"] = update.message.text
    await update.message.reply_text("📌 اهمیت حضور و غیاب چقدر بود؟")
    return ATTENDANCE_IMPORTANCE


async def get_attendance_importance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["attendance_importance"] = update.message.text
    await update.message.reply_text("👨‍🏫 میزان حضور و شرکت استاد در کلاس چگونه بود؟")
    return PROFESSOR_ATTENDANCE


async def get_professor_attendance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["professor_attendance"] = update.message.text
    await update.message.reply_text("📅 نحوه برگزاری کلاس در ترم گذشته چگونه بود؟")
    return CLASS_STYLE


async def get_class_style(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["class_style"] = update.message.text
    await update.message.reply_text("📞 راه ارتباطی با استاد چیست؟")
    return CONTACT


async def get_contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["contact"] = update.message.text
    await update.message.reply_text("📝 توضیحات تکمیلی:")
    return EXTRA


async def get_extra(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["extra"] = update.message.text

    summary_text = (
        "📋 خلاصه فرم ارسال‌شده:\n\n"
        f"👨‍🏫 نام استاد: {context.user_data['professor']}\n"
        f"📚 نام درس: {context.user_data['course']}\n"
        f"🏷 گروه درسی: {context.user_data['group']}\n"
        f"🏫 دانشکده: {context.user_data['faculty']}\n\n"
        f"📝 تکلیف یا تمرین: {context.user_data['assignment']}\n"
        f"📚 منابع تدریس: {context.user_data['teaching_resources']}\n"
        f"📖 منابع امتحان: {context.user_data['exam_resources']}\n"
        f"❓ کافی بودن منابع: {context.user_data['resources_enough']}\n"
        f"📊 امکان افزایش نمره: {context.user_data['grade_increase']}\n\n"
        f"⭐ نحوه نمره‌دهی: {context.user_data['grading']}\n"
        f"🎯 نمره شما: {context.user_data['my_grade']}\n"
        f"🙂 اخلاق استاد: {context.user_data['ethics']}\n"
        f"📌 اهمیت حضور غیاب: {context.user_data['attendance_importance']}\n"
        f"👨‍🏫 حضور استاد: {context.user_data['professor_attendance']}\n"
        f"📅 نحوه برگزاری کلاس: {context.user_data['class_style']}\n\n"
        f"📞 راه ارتباطی: {context.user_data['contact']}\n"
        f"📝 توضیحات تکمیلی: {context.user_data['extra']}"
    )

    # ارسال به دانشجو
    await update.message.reply_text(
        summary_text + "\n\n✅ فرم شما با موفقیت ثبت و برای بررسی ارسال شد."
    )

    # ارسال به ادمین
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ تایید", callback_data="approve"),
            InlineKeyboardButton("❌ رد", callback_data="reject"),
        ]
    ])

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text="📥 فرم جدید برای بررسی:\n\n" + summary_text,
        reply_markup=keyboard
    )

    return ConversationHandler.END


async def admin_decision(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "approve":
        await query.edit_message_text(query.message.text + "\n\n✅ تایید شد.")
    else:
        await query.edit_message_text(query.message.text + "\n\n❌ رد شد.")


# ---------------- MAIN ----------------

def main():
    proxy_url= "http://127.0.0.1:10809"  # اگر نیاز نداری حذف کن
    request = HTTPXRequest(proxy=proxy_url)

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .request(request)
        .get_updates_request(request)
        .build()
    )

    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            PROFESSOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_professor)],
            COURSE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_course)],
            GROUP: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_group)],
            FACULTY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_faculty)],
            ASSIGNMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_assignment)],
            TEACHING_RESOURCES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_teaching_resources)],
            EXAM_RESOURCES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_exam_resources)],
            RESOURCES_ENOUGH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_resources_enough)],
            GRADE_INCREASE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_grade_increase)],
            GRADING: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_grading)],
            MY_GRADE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_my_grade)],
            ETHICS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_ethics)],
            ATTENDANCE_IMPORTANCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_attendance_importance)],
            PROFESSOR_ATTENDANCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_professor_attendance)],
            CLASS_STYLE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_class_style)],
            CONTACT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_contact)],
            EXTRA: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_extra)],
        },
        fallbacks=[],
    )

    app.add_handler(conv)
    app.add_handler(CallbackQueryHandler(admin_decision))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()