import telebot
from telebot import types

TOKEN = "7626771054:AAHm59eB7KLXvkAa13gZ7Ch73V88ysVWnDc"
bot = telebot.TeleBot(TOKEN)

# Главное меню (Обзор бота и Сериалы и сайт Декстера)
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("📚 Обзор бота")
    btn2 = types.KeyboardButton("🎬 Сериалы Декстера")
    btn3 = types.KeyboardButton("🖥 Мой сайт Декстера")
    markup.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🖥 Мой сайт Декстера")
def site_dexter(message):
    bot.send_message(message.chat.id, "🔗 [Перейти на сайт Декстера](https://adwayne.github.io/Dexter/Dexter.html)", parse_mode="Markdown")

# Обзор бота (Студенты, Тех док, Презентация)
@bot.message_handler(func=lambda message: message.text == "📚 Обзор бота")
def bot_overview(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👨‍🎓 Студенты")
    btn2 = types.KeyboardButton("📄 Тех док проект")
    btn3 = types.KeyboardButton("📊 Презентация")
    btn_back = types.KeyboardButton("🔙 Назад")
    markup.add(btn1, btn2, btn3, btn_back)

    bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "👨‍🎓 Студенты")
def students_info(message):
    bot.send_message(message.chat.id, "👨‍🎓 Наши студенты:\n1. Нығмет Азамат\n2. Задай Назым")

@bot.message_handler(func=lambda message: message.text == "📄 Тех док проект")
def send_tech_doc(message):
    with open("tech_doc.docx", "rb") as doc:
        bot.send_document(message.chat.id, doc)

@bot.message_handler(func=lambda message: message.text == "📊 Презентация")
def send_presentation(message):
    with open("presentation.pdf", "rb") as doc:
        bot.send_document(message.chat.id, doc)

# Сериалы Декстера (8 сезонов)
@bot.message_handler(func=lambda message: message.text == "🎬 Сериалы Декстера")
def dexter_series(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(f"📺 Сезон {i}") for i in range(1, 9)]
    btn_back = types.KeyboardButton("🔙 Назад")
    markup.add(*buttons, btn_back)

    bot.send_message(message.chat.id, "Выберите сезон:", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text.startswith("📺 Сезон "))
def dexter_season(message):
    season_num = message.text.split(" ")[-1]
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(f"🎥 {season_num}x{i}") for i in range(1, 13)]
    btn_back = types.KeyboardButton("🔙 Назад к сезонам")
    markup.add(*buttons, btn_back)

    bot.send_message(message.chat.id, f"Вы выбрали {season_num} сезон. Выберите серию:", reply_markup=markup)

@bot.message_handler(func=lambda message: "🎥" in message.text)
def dexter_episode(message):
    episode_num = message.text.split(" ")[-1]
    video_links = {
        "1x1":"https://dexter-hdrezka.net/2-novafilm/1-season/1-episode",
        "1x2":"https://dexter-hdrezka.net/2-novafilm/1-season/2-episode",
        "1x3":"https://dexter-hdrezka.net/2-novafilm/1-season/3-episode",
        "1x4":"https://dexter-hdrezka.net/2-novafilm/1-season/4-episode",
        "1x5":"https://dexter-hdrezka.net/2-novafilm/1-season/5-episode",
        "1x6":"https://dexter-hdrezka.net/2-novafilm/1-season/6-episode",
        "1x7":"https://dexter-hdrezka.net/2-novafilm/1-season/7-episode",
        "1x8":"https://dexter-hdrezka.net/2-novafilm/1-season/8-episode",
        "1x9":"https://dexter-hdrezka.net/2-novafilm/1-season/9-episode",
        "1x10":        "https://mega.nz/embed/zIVDkR6B#8mrbSpKdfBmO-rPVE1NBG0DzellnWgnCOLJ9L48r58c",
        "1x11":"https://dexter-hdrezka.net/2-novafilm/1-season/11-episode",
        "1x12":        "https://mega.nz/embed/zJ12kBrT#kJsC40ksuuN8h61CMi1mvwdNCWeQcuQBYHuVemi14og",
        "2x1":         "https://mega.nz/embed/UxgDhACT#DW0JTmehn316Q_vp-XFmUFzqV92HWa-eZFqiQtg-69Y",
        "2x2":         "https://mega.nz/embed/1sQywZYJ#YBD7bNn9xuhTpGxq3L_KDMgm9eK2aXQsfy911LlvFwM",
        "2x3":         "https://mega.nz/embed/sxQ1yI7b#kR0o1d4zIICRkLl9eqEfX0PVCNglolOF7S1BTkNt7eg",
        "2x4":         "https://mega.nz/embed/NsYwlRab#qUJyg-ngT5NMIpwXdDaVIehTEgFGRplzsj9DHXZ_nrM",
        "2x5":         "https://mega.nz/embed/U452wQzb#6Kr3A7SKADXWa6TH2UUtwLEFqpzp95P-3Lp76pkBGlA",
        "2x6":         "https://mega.nz/embed/o8Zl3LQL#IUVm7fW2hvWL_ABz1As6MHTX0w0FNXMss4SPWkVCePo",
        "2x7":         "https://mega.nz/embed/N14EzYCb#kasrFhNyMWiNq3fEVxA_rO7rX_y_Qb8yjsQT12Okcf4",
        "2x8":         "https://mega.nz/embed/p1BE2IrT#vNDUQ6rBHsTLUalWmJK6WCaObpVF6sT-FLfIK8eVIjE",
        "2x9":         "https://mega.nz/embed/KRtViZTJ#y4ETVsRYVf6gkW4uCIPWqdWgJYorsjzTSAsglvGvVks",
        "2x10":        "https://mega.nz/embed/3dtglT6T#eIAcvV2tvtWItVEcClXZmefylDSRctSeVHJjPrJ670c",
        "2x11":        "https://mega.nz/embed/TM1BlYia#4SI2Z8wtQ5U46Lkmq0RNPeuHiTRlRRNaR0Obf4hFQso",
        "2x12":        "https://mega.nz/embed/aRMywDoB#uYTECPHTYXjg6sg81zAfLeRsBlq6oIqwfgNnUi8eYdU",
        "3x1":        "https://mega.nz/embed/aJNCEAAT#RhwoyU1ukDf3ZkGVMGN8vQ7IH0fph6ZvyDT0j5jVHbY",
        "3x2":        "https://mega.nz/embed/E9gkTT5B#HW_BvEvr15OCi9kz3VZFPaoty5Gxu7U6Mf9BcFIXZz4",
        "3x3":        "https://mega.nz/embed/I0wCwZyZ#D63uft7cD_bG_iJeyXhRgvL-iLF_xgriVgKRPJn5Dws",
        "3x4":        "https://mega.nz/embed/hwAEEABD#tU6DbVTyyv9lDA301Hy9ZusNgVImgSy895IS7vhs-X8",
        "3x5":        "https://mega.nz/embed/kwhGxZSA#B-alOSj8xJf-eo01oM22lhrDGDuiqXePtvdCubb58Bk",
        "3x6":        "https://mega.nz/embed/IlhDzCYB#m6P9oTCsMCUUyrbS0as-7bQ6pMMWa5O9qxWnb8DS5wE",
        "3x7":        "https://mega.nz/embed/10RRCT6Q#9GdE2glEVBME4sDkvZJpxrViXMIgvP-kKW7A7zMWQnM",
        "3x8":        "https://mega.nz/embed/PywATAyT#uiFPpPluDZ5ttigJ3guv90fLzDdEmYtzTT9mycRUAYI",
        "3x9":        "https://mega.nz/embed/q3x3CbRT#zE-11D1-ElS9zWRodqWacUL8MT7OMRtbY8K9VcaCvBA",
        "3x10":        "https://mega.nz/embed/buh0SQ6B#Fx8uXTk_CbiyRXY__OMhXzT0bwaa-WHw5Eg4fKqxWyI",
        "3x11":        "https://mega.nz/embed/eyBWyb7A#m_fJNzJb_UXipwiyr4jiy6v9Kr5PAfM55iqs-p9ci94",
        "3x12":        "https://mega.nz/embed/CjQiBAjS#i9o6IeWkIlC1OLi5hKvf2BVOaRJ8y1Ktf8CVwoaAesY",
        "4x1":        "https://mega.nz/embed/Vz0h2DLZ#mpAS_j621Lmg1VhL5L6fAyGX1IvVSzOCJC49dxlcoRg",
        "4x2":        "https://mega.nz/embed/lyN0BaIa#EzFBS4qpD03cSuBz3afUidPmQStAUxxTP9q2nfCCFP0",
        "4x3":        "https://mega.nz/embed/EjcUFAAY#lwW4qQCsdSEG6a-nXYpJPoSUb1qBxpDfN0wBLYG1RGY",
        "4x4":        "https://mega.nz/embed/kqcBjbjD#oo8cQKLdu9QwoU3gxOWNifMW9MF2OXywaJveOtN54HI",
        "4x5":        "https://mega.nz/embed/43NkxYzY#b8wFxaDT5MfbmESg62WG3SCNkGO1c5NEhqtw9bUBw5E",
        "4x6":        "https://mega.nz/embed/s6F3UT4J#yyk9OYshAkR6Fq5x_LYNjtOO_dkmQ3kOlEPEGl_iqcg",
        "4x7":        "https://mega.nz/embed/86kRRBib#UGg30_kq3WBS_IUo0-vDN-EZBJfrwUQV0W8c09s7iQ8",
        "4x8":        "https://mega.nz/embed/wzEgyLzT#9g4Pp0seigt9x_qfAmWfMBcFK1Pc3qkak0SmrqLeHZ8",
        "4x9":        "https://mega.nz/embed/gnEyBC4Y#FxwdgKq44mnkAhHWnME5a5yB4tqRyIONyyJGry62BF0",
        "4x10":        "https://mega.nz/embed/1392nLYI#EyLuABBLaWY3hxcGeGAKDEaH4dcDO-cli3xj49BTE0w",
        "4x11":        "https://mega.nz/embed/3JFHTRqZ#eMpW7iyBG1_mqeQ4ZGDafUNI0_43rQvFg64qvy0l6Kw",
        "4x12":        "https://mega.nz/embed/TB0XDBrI#1lSu2qz0Vn1CAuZ-braFLedd41RYsa7yRHrBOKyH2AM",
        "5x1":        "https://mega.nz/embed/9zl1RBib#vKgWTR74EGKTg5uCKG2TsBPslmP5s-_0KIwbgNh-0HU",
        "5x2":        "https://mega.nz/embed/UrF2WKAB#LTb4ikoAgm7gQOv5RxUABoHoZ0KEZTRZ4mNIS334IZs",
        "5x3":        "https://mega.nz/embed/pvM11C5K#perZqQJusygnxfKLmO7zB2vrq1cPRoSz99EKRnDM2vs",
        "5x4":        "https://mega.nz/embed/WZkyWSZI#1OXLJuiATRTqyAuwKB641-UZMo0bp2Bj3YTUq_E1Rog",
        "5x5":        "https://mega.nz/embed/PRtBRKTR#VMIjYjuoTfoLBsfpJ_LA5GleR7DvYijSHPBI494ZTM0",
        "5x6":        "https://mega.nz/embed/fJxzgS5T#X3KRx7JNowvo4sy-mMebrVaQGlyi5G9iTvyCmPJgfYI",
        "5x7":        "https://mega.nz/embed/6IZ2nKYD#AZCvLRAb7vdRnanmKpo1XlH0NsixC9TaTLzCBCth_RE",
        "5x8":        "https://mega.nz/embed/PRtBRKTR#VMIjYjuoTfoLBsfpJ_LA5GleR7DvYijSHPBI494ZTM0",
        "5x9":        "https://mega.nz/embed/PRtBRKTR#VMIjYjuoTfoLBsfpJ_LA5GleR7DvYijSHPBI494ZTM0",
        "5x10":        "https://mega.nz/embed/Sc4CiC5Y#NycrYaseXtIFa7rTgX2NgoLdncvHIlsQCGcvXGuLxJw",
        "5x11":        "https://mega.nz/embed/PEJyWSYC#INtHk2GslzM1J0MYU1S2R1OY6sset8ECoVVlSEvxchE",
        "5x12":        "https://mega.nz/embed/zcww1DqC#wavmZtLEa-qhNVVNsH6xVfT6Hnl202DIDXucc6yM8Hg",
        "6x1":        "https://mega.nz/embed/nFkTHDKL#Q2-bf5clO69aVdwmc6GK_TBCv6A4XK1Fv1llTuGyJ4U",
        "6x2":        "https://mega.nz/embed/zRtDQa7T#iamehdJxErpxIClWmtHWGAyUTQ-qDzi8G6wiSqVHNG8",
        "6x3":        "https://mega.nz/embed/CYtWWYoI#bGTZLrVRX4DthWfaGQk1wbj6MK0LRl9jMyA_61BJ6wI",
        "6x4":        "https://mega.nz/embed/icNhzDJC#sK2zGnTPU1PNKgAOiJNL4ZvPRnG47Jdl8hztN4WNqM4",
        "6x5":        "https://mega.nz/embed/jM8EjbBT#iUFhyeYPxMDuX4wIZnoqCOCumACTjMqbqcy4L7srA8E",
        "6x6":        "https://mega.nz/embed/rVVCXBia#-VdERZUeaUd6Wfwv5PuTEgHD4UE0krHmpKddOKkMCJI",
        "6x7":        "https://mega.nz/embed/WZMgkRbD#X53JFxbAhJWFWahS9oblt870j7r6D1MLw-ArqCe916k",
        "6x8":        "https://mega.nz/embed/TFtWGaQY#8coZaeXBwMc3590PQ-YzsGSOcPJiCkYQKawGWrqAS0E",
        "6x9":        "https://mega.nz/embed/GYlDGI4S#hAbECL9kmK3X-SpMiDyBUfBf6B53x2Epmj9DPcgHoYA",
        "6x10":        "https://mega.nz/embed/zEEk1YzK#o3pUn1DfnqREhLW8Y3n6Qg6mF0sXmMhtcG70fPYEuo0",
        "6x11":        "https://mega.nz/embed/CB9FAKZL#TY1xZ5TjpbsNbWrEiaVawp4TO2XYMMEEEpf5D3YYHjg",
        "6x12":        "https://mega.nz/embed/XBtWBbBD#qdUyJ9PQCcsA9iy_ah_2H2DPxt99L8z_x1Q6nnxKMb8",
        "7x1":        "https://mega.nz/embed/6Yp1gRhB#TxtL-c72yxvpiUHTh91X9cljSjx2j4pUOAWOMNrJlZs",
        "7x2":        "https://mega.nz/embed/6AxhmQSB#8qB9K45slZtPBfWo75rF5tfxyqnJbQQPqde-oEJRFLQ",
        "7x3":        "https://mega.nz/embed/7BxT2Cya#Y657uPnHP0kO1BEzCV_S7ks74JBH7yc78YDGKDTzwv8",
        "7x4":        "https://mega.nz/embed/nEFAHCSB#8yhAI82SeKMTObwbbQB11rNIHfmTpzRnvN-p4Pe7pPU",
        "7x5":        "https://mega.nz/embed/aEtgiATS#YbO1SnSQLhhLsjFIcJ_TrpsEHB0EEzyf1qDJ8AG96RQ",
        "7x6":        "https://mega.nz/embed/CnAVTRCA#O7Et1M6Ta25rozLZHyh9ivAtQkOtujsrAZPzvyaKBvw",
        "7x7":        "https://mega.nz/embed/y3AGCADR#73u9DVTDivva6p5MmtCeShuOW_KJ16HLiqEPukevXZo",
        "7x8":        "https://mega.nz/embed/O6YwVAzB#UTWxybKmn49Pz2SxsU2ByVnYQe7l5vn9xRQUHWuV4Lc",
        "7x9":        "https://mega.nz/embed/y3AGCADR#73u9DVTDivva6p5MmtCeShuOW_KJ16HLiqEPukevXZo",
        "7x10":        "https://mega.nz/embed/Xnp1TYwT#Tmr-1zb3ccS8le1hx4ptPt9YeqsSYg1Qf4AFTkjeZ9o",
        "7x11":        "https://mega.nz/embed/bMc1hKqB#wul6PBTgWz0QTgPlH0xEfCIPtK8ovjVTbYdTAHCdXC4",
        "7x12":        "https://mega.nz/embed/GdVASaTC#7OBBu2xtU9KMQNxwqE7wz3_WVdGwgSPsVl-jodqmrbU",
        "8x1":        "https://mega.nz/embed/GEsGjASa#IdxS4j1cH6atmSPrMMrXe1ldwfsALLNe-aVvFFz2y-U",
        "8x2":        "https://mega.nz/embed/KElmhIpK#MhUe9izrT3KcxEUTPLXZIl0b7Yx6CfYN2A2PmjVfR0w",
        "8x3":        "https://mega.nz/embed/qFUwHASA#X74vGmXl5gTyzRoF--CBt3j7LusAjor_YlxhqRRM1vc",
        "8x4":        "https://mega.nz/embed/LVcFwYBS#59q9ZcBiYYXDSDfoSctuG_VhSG1f2kKqEbeL1iTh-a8",
        "8x5":        "https://mega.nz/embed/EhZXSY7Z#Z7igZ-nVVaSiTZxLVEgwTO0tCh2kYdr4IXekHZoWVtQ",
        "8x6":        "https://mega.nz/embed/xwYFiLBB#WVygkeZc8cWuQUTl8UR3LfY88XVgMQYnTlIJOHwxyOQ",
        "8x7":        "https://mega.nz/embed/rE8mCYzT#xzOGcHrBApqJG_UkS5D5gJh8MGTsA3zs0g2PtSoUC30",
        "8x8":        "https://mega.nz/embed/2d8SHTaC#yAlLloR0RaDVFLipMw-D9kj3n1kPRoOgL0W_nvPTb3A",
        "8x9":        "https://mega.nz/embed/CVkjUZLI#LcjLhYBeoFbm2VnnA_iM7IyC3hlA1tgUGZ4HI8bDhl4",
        "8x10":        "https://mega.nz/embed/1781GJrI#Ua9oQykBT89n1bN76dVT6F-KNWclHHFo20OcqYEfQww",
        "8x11":        "https://mega.nz/embed/Yv0UCSIa#DtuKMce9pH14WxDleIuTQ8scK6bqQzcfuQwcH3qdjJ0",
        "8x12":        "https://mega.nz/embed/TI5wGY7C#E_-cvuem7swup08orDtPbx85mp_ZD6H-sBVNhpK8q64",
 }
    file = video_links.get(episode_num, None)

    if file:
        bot.send_message(message.chat.id, f"Ссылка на серию: {file}")
    else:
        bot.send_message(message.chat.id, "Видео не найдено")

@bot.message_handler(func=lambda message: message.text == "🔙 Назад")
def back_to_main(message):
    start_message(message)

@bot.message_handler(func=lambda message: message.text == "🔙 Назад к сезонам")
def back_to_seasons(message):
    dexter_series(message)

bot.polling(none_stop=True)
