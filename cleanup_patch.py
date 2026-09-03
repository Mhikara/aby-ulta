import re

with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

# hapus section "Untuk Aby dari hati" (kalau ada)
html = re.sub(
    r'\s*<section>\s*<h2 class="st">Untuk Aby.*?</section>',
    '',
    html, flags=re.S
)

# hapus CSS balon/particle overlay kalau masih ada sisa
html = re.sub(r'\.balloonOverlay\{.*?\}\s*', '', html, flags=re.S)
html = re.sub(r'\.letterBalloon.*?\}\s*', '', html, flags=re.S)
html = re.sub(r'@keyframes floatBalloon\{.*?\}\s*', '', html, flags=re.S)

# hapus fungsi launchBalloons() dan deepText kalau masih ada
html = re.sub(r'function launchBalloons\(\)\{.*?\n\}\n', '', html, flags=re.S)
html = re.sub(r'const deepText = `.*?`;\s*', '', html, flags=re.S)

# ganti isi function tiupLilin supaya redirect ke hbd.html
html = re.sub(
    r'function tiupLilin\(\)\{.*?\n\}',
    '''function tiupLilin(){
  const f=$("#flame");
  if(f.classList.contains("off"))return;
  f.classList.add("off");
  $("#smoke").classList.add("show");
  $("#cakeHint").textContent="🎉 Yeay! Menuju kejutan berikutnya...";
  $("#cakeHint").classList.add("done");
  boom();
  setTimeout(()=>{ window.location.href = "hbd.html"; }, 1400);
}''',
    html, flags=re.S
)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("index.html sudah dibersihkan dan tiup lilin sekarang pindah ke hbd.html")
