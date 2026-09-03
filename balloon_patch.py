with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

balloon_css = """
.balloonOverlay{position:fixed;inset:0;pointer-events:none;z-index:60;overflow:hidden;}
.letterBalloon{position:absolute;bottom:-70px;text-align:center;
  font-family:'Bangers',cursive;font-size:1.7rem;color:#fff;
  animation:floatBalloon 3.4s ease-in forwards;}
.letterBalloon .balloon{width:26px;height:32px;margin:0 auto 4px;
  border-radius:50% 50% 50% 50%/60% 60% 40% 40%;
  box-shadow:inset -4px -4px 8px rgba(0,0,0,.25), 2px 4px 6px rgba(0,0,0,.3);}
.letterBalloon .string{width:1px;height:16px;background:rgba(255,255,255,.5);margin:0 auto;}
@keyframes floatBalloon{
  0%{transform:translateY(0) rotate(-4deg);opacity:0;}
  8%{opacity:1;}
  50%{transform:translateY(-60vh) rotate(4deg);}
  100%{transform:translateY(-125vh) rotate(-4deg);opacity:0;}
}
"""

balloon_js = """
function launchBalloons(){
  const msg = "HAPPY BIRTHDAY ABY!";
  const overlay = document.createElement('div');
  overlay.className = 'balloonOverlay';
  document.body.appendChild(overlay);
  const colors = ["#ff6b9d","#ffd36e","#7dffc3","#c4a0ff","#ff9d3f","#5ec8ff","#ff5e7e"];
  const chars = msg.split('');
  const usable = chars.filter(c => c !== ' ').length;
  let i = 0;
  chars.forEach(ch => {
    if(ch === ' ') return;
    const el = document.createElement('div');
    el.className = 'letterBalloon';
    const leftPos = 6 + (i/(usable-1)) * 88;
    el.style.left = leftPos + 'vw';
    el.style.animationDelay = (i*0.13) + 's';
    const color = colors[i % colors.length];
    el.innerHTML = '<div class="balloon" style="background:'+color+'"></div><div class="string"></div><span>'+ch+'</span>';
    overlay.appendChild(el);
    i++;
  });
  setTimeout(() => overlay.remove(), 4400);
}
"""

html = html.replace("</style>", balloon_css + "\n</style>", 1)
html = html.replace("<script>", "<script>" + balloon_js, 1)

old_tiup = """function tiupLilin(){
  const f=$("#flame");
  if(f.classList.contains("off"))return;
  f.classList.add("off");
  $("#smoke").classList.add("show");
  $("#cakeHint").textContent="🎉 Yeay! Semoga wish-nya kewujud, Aby.";
  $("#cakeHint").classList.add("done");
  boom();
  const box=$("#deepMsg");
  box.classList.remove("locked");
  box.classList.add("unlocked");
  box.innerHTML=deepText;
}"""

new_tiup = """function tiupLilin(){
  const f=$("#flame");
  if(f.classList.contains("off"))return;
  f.classList.add("off");
  $("#smoke").classList.add("show");
  $("#cakeHint").textContent="🎉 Yeay! Semoga wish-nya kewujud, Aby.";
  $("#cakeHint").classList.add("done");
  boom();
  launchBalloons();
  setTimeout(()=>{
    const box=$("#deepMsg");
    box.classList.remove("locked");
    box.classList.add("unlocked");
    box.innerHTML=deepText;
  }, 1200);
}"""

html = html.replace(old_tiup, new_tiup, 1)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("Animasi balon huruf berhasil ditambahkan!")
