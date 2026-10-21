from flask import Flask, render_template
from datetime import date
import os

app = Flask(__name__)

# ====== CẤU HÌNH CÁ NHÂN ======
START_DATE = date(2022, 10, 21)
YOUR_NAME = "Anhiu"
HER_NAME = "Emiu"
# ==============================

@app.route("/")
def home():
    today = date.today()
    delta = today - START_DATE

    days = delta.days
    hours = days * 24 + delta.seconds // 3600
    minutes = days * 24 * 60 + delta.seconds // 60

    image_folder = os.path.join(app.static_folder, "images")
    images = []
    if os.path.exists(image_folder):
        images = sorted([
            f for f in os.listdir(image_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
        ])

    music_path = os.path.join(app.static_folder, "music", "song.mp3")
    has_music = os.path.exists(music_path)

    return render_template(
        "index.html",
        days=days, hours=hours, minutes=minutes,
        images=images, has_music=has_music,
        your_name=YOUR_NAME, her_name=HER_NAME,
    )
import os


# === ĐƯỜNG DẪN 1: THƯ VIỆN ẢNH CHUNG ===
@app.route("/anh-ky-niem")
def gallery():
    image_folder = os.path.join(app.static_folder, "images")
    images = []
    if os.path.exists(image_folder):
        images = sorted([
            f for f in os.listdir(image_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
        ])
    return render_template("gallery.html", images=images, your_name=YOUR_NAME, her_name=HER_NAME)

# === ĐƯỜNG DẪN 2: GÓC THƯ TAY ===
@app.route("/thu-tay")
def letters():
    letter_folder = os.path.join(app.static_folder, "letters")
    letter_images = []
    if os.path.exists(letter_folder):
        # Lấy tất cả file ảnh trong thư mục letters (tự động sắp xếp theo tên)
        letter_images = sorted([
            f for f in os.listdir(letter_folder)
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))
        ])
    return render_template("letters.html", images=letter_images, your_name=YOUR_NAME, her_name=HER_NAME)