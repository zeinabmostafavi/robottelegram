import random
import telebot

bot = telebot.TeleBot("1727002396:AAFudzgtyIRRhfptQEHLBRYZIkqZ8P9x3X0")

buttons = telebot.types.ReplyKeyboardMarkup(row_width=2)
btn2 = telebot.types.KeyboardButton('طالع بینی ماه تولد🍰')
btn3 = telebot.types.KeyboardButton('بازی حدس عدد🎮')
buttons.add(btn2, btn3)


@bot.message_handler(commands=['start'])
def say_hi(message):
    bot.send_message(
        message.chat.id, "سلام دوست من👨🏼‍🤝‍👨🏻 من اینجام تا باهم تفریح کنیم.😍اماده ای؟")
    bot.send_message(message.chat.id, " بزن بریم!✊", reply_markup=buttons)


rand = random.randint(0, 20)


@bot.message_handler(func=lambda message: True)
def send_normal_message(message):
    if message.text == 'بازی حدس عدد🎮':
        bot.send_message(message.chat.id, 'یک عدد بین 0 تا20 وارد کن:🎈')
    if message.text.isnumeric():
        if rand == int(message.text):
            bot.reply_to(message, 'خدا قوت پهلوان🎉🎊')
            photo = open('telegrambot/m.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        elif int(message.text) > rand:
            bot.reply_to(message, 'برو پایین😌')
        elif int(message.text) < rand:
            bot.reply_to(message, 'برو بالا🙄')
    if message.text == 'طالع بینی ماه تولد🍰':
        bot.send_message(message.chat.id, 'ماه تولدتو بگو بهم🎈:')
    if message.text == 'فروردین':
        bot.reply_to(message, "فروردینی ها در پی عشق آتشین و پر شورترین عشق ممکن اند. او خود به خود جنس مخالف را جذب می کند.لذتهای جسمانی برای او بسیار اهمیت دارد و گاه احساس مالکیت شدیدی نسبت به معشوق خود را دارد..")
    elif message.text == 'اردیبهشت':
        bot.reply_to(message, "جذاب است و عشقش تا حدی نفسانی. برای او عشق اهمیت زیادی دارد و اگر عاشق شود، عاشقی فداکار خواهد بود. معمولاً صبر میکند. ابتدا طرف مقابل تعهد خود را ثابت کند و سپس خود را در این تعهد شریک میکند.")
    elif message.text == 'خرداد':
        bot.reply_to(message, "چه راحت میتوان عاشق او شد. جذابیت و شیرینی کلام او به خوبی بر این مدعاست. او عاشق شادی و خوش بودن است و اگر نتوانید او را شاد کنید، جذابیت خود را از دست می دهید.")
    elif message.text == 'تیر':
        bot.reply_to(message, "او مانند سیاره خود – ماه – در حال تغییر است. اگر به او اطمینان کامل نداشته باشی، هرگز رابطه عاشقانه با او نخواهید داشت. او از عشق ورزیدن لذت می برد و در عوض می خواهد آن را دریافت کند.")
    elif message.text == 'مرداد':
        bot.reply_to(
            message, "عاشق عاشق شدن است و معشوق خود را غرق هدایای خود می کند. تلاش می کند تا رابطه عاشقانه بی نقصی را خلق کند.")
    elif message.text == 'شهریور':
        bot.reply_to(message, "می تواند چنان تودار باشد که به نظر برسد که از برخورد با دیگران منع شده ولی آنگاه که به عشق واقعی خود دست پیدا کند، دیگر این ویژگی او را نخواهید دید. برای چنین انسان فداکار و مهربان، تحمل سختی بسیار با ارزش است. او به آسانی در عشق گول نمی خورد چون می داند در پی چیست.")
    elif message.text == 'مهر':
        bot.reply_to(
            message, "او می تواند دوست خوب و میزبانی عالی باشد. او در سیاست دومی ندارد.")
    elif message.text == 'آبان' or message.text == 'ابان':
        bot.reply_to(message, "مرموز است ولی میتواند عاشق باشد. از حمایت دیگران لذت می برد. او می تواند حسود و تودار باشد. با کسی که حس کند قابل اطمینان است، کنار می آید.")
    elif message.text == 'اذر' or message.text == 'آذر':
        bot.reply_to(
            message, "اگر شخص مورد علاقه اش را پیدا کند، وفادار است. مشکل اینجاست که خواسته اش را بیان نمی کند و صبر میکند تا خودتان حدس بزنید")
    elif message.text == 'دی':
        bot.reply_to(message, "عجله ای در عشق ندارد. نه به سرعت عاشق می شود، نه به سادگی راز دل خود را می گوید. او همواره در حرکت است ولی نمی داند چرا. فقط می داند باید موفق شود. اگر فکر میکنید می توانید او را از رسیدن به هدفش باز دارید و به سمت خود جذب کنید، سخت در اشتباهید.")
    elif message.text == 'بهمن':
        bot.reply_to(message, "اگر عاشق متولد بهمن باشید، با تمام وجود عاشق شما خواهد شد. تنها نکته ای که باید از آن دوری جویید، این است که بر سر راه پیشرفت او قرار نگیرید. او عاشقی صادق است. دیر عصبانی می شود. آزار دهنده نیست. برنامه های خودش را دارد. هرگز تغییر نخواهد کرد. اگر نتوانید خود را با ایده های گوناگون مذهبی، فرهنگی و اجتماعی او هماهنگ کنید، هرگز شانسی برای دستیابی به عشق پایدار او نخواهید داشت.")
    elif message.text == 'اسفند':
        bot.reply_to(message, "اگر عاشق شماست، واقعاً خوشبختید. او به پای معشوق، فداکاری های بسیار می کند. برای حفظ این رابطه از هیچ کاری رویگردان نیست. مادامی که به او وفادار باشید، از آن شما خواهد بود.")


bot.polling()
