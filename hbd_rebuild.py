with open("hbd.html","r",encoding="utf-8") as f:
    html = f.read()

# ganti seluruh style di dalam <style>...</style> tetap dipakai, cuma tambah class baru
extra_css = """
.bdayText{
  text-align:center; font-family:'Bangers',cursive; letter-spacing:.04em;
  line-height:1.25; margin:20px 0 6px;
}
.bdayText span.line{
  display:block; opacity:0; transform:translateY(24px) scale(.85);
  animation:popIn .7s cubic-bezier(.2,.9,.3,1.3) forwards;
  font-size:clamp(1.8rem, 9vw, 3rem);
  background:linear-gradient(90deg,#ff6b9d,#ffd36e,#7dffc3,#c4a0ff);
  background-size:300% 100%;
  -webkit-background-clip:text; background-clip:text; color:transparent;
  animation-name:popIn, gradientMove;
  animation-duration:.7s, 3s;
  animation-timing-function:cubic-bezier(.2,.9,.3,1.3), linear;
  animation-iteration-count:1, infinite;
  animation-fill-mode:forwards, none;
  text-shadow:0 0 18px rgba(255,255,255,.15);
}
.bdayText span.line:nth-child(1){animation-delay:0s, .7s;}
.bdayText span.line:nth-child(2){animation-delay:.25s, .95s;}
.bdayText span.line:nth-child(3){animation-delay:.5s, 1.2s;}
@keyframes popIn{
  0%{opacity:0; transform:translateY(24px) scale(.85);}
  100%{opacity:1; transform:translateY(0) scale(1);}
}
@keyframes gradientMove{
  0%{background-position:0% 50%;}
  100%{background-position:300% 50%;}
}
.sparkleWrap{position:relative; height:0;}
.sparkle{
  position:absolute; width:5px; height:5px; border-radius:50%;
  background:#fff; opacity:0; animation:sparklePop 1.6s ease-in-out infinite;
}
@keyframes sparklePop{
  0%,100%{opacity:0; transform:scale(.4);}
  50%{opacity:.9; transform:scale(1.3);}
}
"""
html = html.replace("</style>", extra_css + "\n</style>", 1)

# ganti canvas#stage dengan div teks + tetap sisakan canvas kecil buat sparkle dekorasi (opsional dihapus saja)
old_body_block = '''<div class="wrap">
  <canvas id="stage"></canvas>
  <p class="hint" id="hint">Menyalakan keajaiban…</p>'''

new_body_block = '''<div class="wrap">
  <div class="sparkleWrap" id="sparkleWrap"></div>
  <div class="bdayText" id="bdayText">
    <span class="line">HAPPY</span>
    <span class="line">BIRTHDAY</span>
    <span class="line">ABY!</span>
  </div>
  <p class="hint" id="hint" style="display:none;">Menyalakan keajaiban…</p>'''

html = html.replace(old_body_block, new_body_block, 1)

# ganti seluruh script canvas particle dengan script sederhana: sparkle dekorasi + reveal surat setelah delay
import re
old_script = re.search(r'<script>.*?</script>', html, flags=re.S).group(0)

new_script = '''<script>
const sparkleWrap = document.getElementById('sparkleWrap');
for(let i=0;i<18;i++){
  const s = document.createElement('div');
  s.className = 'sparkle';
  s.style.left = (Math.random()*100) + '%';
  s.style.top = (Math.random()*140 - 20) + 'px';
  s.style.animationDelay = (Math.random()*1.6) + 's';
  sparkleWrap.appendChild(s);
}

setTimeout(()=>{
  const box = document.getElementById('deepMsg');
  box.classList.add('show');
  requestAnimationFrame(()=> box.classList.add('in'));
  document.getElementById('backLink').classList.add('show');
}, 2200);
</script>'''

html = html.replace(old_script, new_script, 1)

with open("hbd.html","w",encoding="utf-8") as f:
    f.write(html)

print("hbd.html berhasil dirombak, teks sekarang tajam dan jelas!")
