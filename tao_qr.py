import qrcode

# === SỬA LINK WEB CỦA BẠN VÀO ĐÂY ===
link_web = "https://ky-niem-cua-chung-ta.onrender.com" 

# Cấu hình tạo QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(link_web)
qr.make(fit=True)

# Tạo ảnh và lưu lại
img = qr.make_image(fill_color="black", back_color="white")
ten_file = "ma_qr_tinh_yeu.png"
img.save(ten_file)

print(f"Đã tạo xong mã QR, lưu tại file: {ten_file} 🎉")