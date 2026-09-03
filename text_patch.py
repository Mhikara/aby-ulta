with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

old_bubble = '''    <div class="bubble">
      Hai <b>Aby</b>!<br><br>
      Selamat bertambah usia. Semoga tahun ini lebih ringan langkahnya, lebih hangat harinya, dan lebih banyak alasan untuk tersenyum tanpa dipaksa.<br><br>
      Terima kasih sudah jadi orang yang selalu bawa warna di sekitar orang-orang terdekatnya. Semoga makin dikuatkan, makin dicintai, dan makin percaya sama proses hidupmu sendiri.<br><br>
      Tetap jadi Aby yang sekarang — yang elegan di luar, chaos receh di dalam. 🎀
      <span class="sign">— Teman yang sayang banget</span>
    </div>'''

new_bubble = '''    <div class="bubble">
      Hai <b>Aby</b>, teman terbaik!<br><br>
      Selamat bertambah usia. Semoga tahun ini makin banyak rezeki, makin banyak alasan buat ketawa lepas, dan makin sedikit hal yang bikin capek hati.<br><br>
      Semangat terus buat kerja parfumnya ya — semoga makin laris, makin banyak pelanggan setia, dan makin lancar rezekinya. Semangat juga buat live-nya, semoga makin rame dan makin pede tiap kali on-cam. Hehe.<br><br>
      Terima kasih sudah jadi teman yang bisa diandalkan. Tetap jadi Aby yang sekarang ya. 🎀
      <span class="sign">— Teman terbaikmu</span>
    </div>'''

deep_old_start = html.find('const deepText = `')
deep_old_end = html.find('`;', deep_old_start) + 2
old_deep_block = html[deep_old_start:deep_old_end]

new_deep_block = '''const deepText = `<span class="letterTitle">Surat Kecil Untuk Aby</span>
Kalau boleh jujur, senang banget lihat kamu terus jalan meski capek — bangun usaha parfum sendiri, jualan lewat live, semua itu nggak gampang tapi kamu tetap konsisten.<br><br>
Semoga umur yang baru ini bawa lebih banyak keberkahan buat usahamu, lebih banyak pelanggan yang loyal, dan lebih banyak hasil dari kerja keras yang selama ini kamu jalani sendiri.<br><br>
Sebagai teman terbaikmu, aku cuma mau bilang: semangat terus, Aby. Selamat ulang tahun. 🤍`'''

html = html.replace(old_bubble, new_bubble, 1)
html = html.replace(old_deep_block, new_deep_block, 1)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("Teks berhasil diperbarui!")
