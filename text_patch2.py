with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

old_bubble = '''      Semangat terus buat kerja parfumnya ya — semoga makin laris, makin banyak pelanggan setia, dan makin lancar rezekinya. Semangat juga buat live-nya, semoga makin rame dan makin pede tiap kali on-cam. Hehe.<br><br>
      Terima kasih sudah jadi teman yang bisa diandalkan. Tetap jadi Aby yang sekarang ya. 🎀'''

new_bubble = '''      Semangat terus buat kerja sebagai parfumer ya — semoga makin laris, makin banyak pelanggan setia, dan makin lancar rezekinya. Semangat juga buat live-nya, semoga makin rame dan makin pede tiap kali on-cam. Hehe.<br><br>
      Terima kasih sudah jadi teman yang bisa diandalkan. Tetap jadi Aby yang sekarang ya. 🎀<br><br>
      Btw, kapan nih kita mabar ML lagi? Udah lama banget gak main bareng. 😆'''

old_deep = '''Kalau boleh jujur, senang banget lihat kamu terus jalan meski capek — bangun usaha parfum sendiri, jualan lewat live, semua itu nggak gampang tapi kamu tetap konsisten.<br><br>
Semoga umur yang baru ini bawa lebih banyak keberkahan buat usahamu, lebih banyak pelanggan yang loyal, dan lebih banyak hasil dari kerja keras yang selama ini kamu jalani sendiri.<br><br>
Sebagai teman terbaikmu, aku cuma mau bilang: semangat terus, Aby. Selamat ulang tahun. 🤍`'''

new_deep = '''Kalau boleh jujur, senang banget lihat kamu terus jalan meski capek — bekerja sebagai parfumer, jualan lewat live, semua itu nggak gampang tapi kamu tetap konsisten.<br><br>
Semoga umur yang baru ini bawa lebih banyak keberkahan buat kariermu, lebih banyak pelanggan yang loyal, dan lebih banyak hasil dari kerja keras yang selama ini kamu jalani sendiri.<br><br>
Sebagai teman terbaikmu, aku cuma mau bilang: semangat terus, Aby. Oh iya, jangan lupa ajakin mabar ML ya, udah kelamaan vakum kita berdua. 😂<br><br>
Selamat ulang tahun. 🤍`'''

ok1 = old_bubble in html
ok2 = old_deep in html

if not ok1 or not ok2:
    print("Pola tidak ditemukan (bubble:", ok1, ", deep:", ok2, "). Kirim ulang isi index.html terbaru.")
else:
    html = html.replace(old_bubble, new_bubble, 1)
    html = html.replace(old_deep, new_deep, 1)
    with open("index.html","w",encoding="utf-8") as f:
        f.write(html)
    print("Teks berhasil diperbarui!")
