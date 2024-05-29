import telebot
import socket
import threading

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = telebot.TeleBot("0KNVe4AtOLcV7WaJ5dgwaw2cEtqLpaA")

# تعريف الدالة للرد على الرسائل بكلمة "تم"
@bot.message_handler(func=lambda message: True)
def reply_with_done(message):
    bot.reply_to(message, "تم")

# فتح المنفذ بشكل تلقائي عند تشغيل البرنامج
def open_port_5000():
    try:
        # انشاء كائن socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # ربط السوكت بالعنوان والمنفذ المطلوبين
        s.bind(("0.0.0.0", 5000))
        # الاستماع للاتصالات الواردة
        s.listen(5)  # حد اقصى لعدد الاتصالات في قائمة الانتظار
        print("تم فتح المنفذ 5000")
    except Exception as e:
        print(f"حدث خطأ: {e}")

# استدعاء الدالة لفتح المنفذ
threading.Thread(target=open_port_5000).start()

# تشغيل البوت
bot.polling()
