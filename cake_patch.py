with open("index.html","r",encoding="utf-8") as f:
    html = f.read()

cake_section = """
  <section>
    <h2 class="st">Tiup Lilin <em>bikin wish</em></h2>
    <div class="cakewrap" id="cakewrap">
      <div class="smoke" id="smoke"></div>
      <div class="flame" id="flame" onclick="tiupLilin()"></div>
      <div class="wick"></div>
      <div class="candle"></div>
      <div class="cakeTop"></div>
      <div class="cakeMid"></div>
      <div class="cakeBase"></div>
    </div>
    <p class="hint" id="cakeHint">Tekan lilinnya untuk meniup, terus bikin wish</p>
    <p class="hint" id="cakeDone" style="display:none;color:var(--mint);font-weight:700;">Wish granted mode: ON</p>
  </section>
"""

cake_style = """
<style>
.cakewrap{position:relative;width:150px;margin:14px auto 4px;text-align:center;}
.flame{width:11px;height:17px;margin:0 auto;border-radius:50% 50% 50% 50%/60% 60% 40% 40%;
  background:radial-gradient(circle,#ffe08a 0%,#ff9d3f 60%,#ff5e3a 100%);
  animation:flicker .4s infinite alternate;cursor:pointer;}
@keyframes flicker{0%{transform:scale(1) rotate(-3deg)}100%{transform:scale(1.12) rotate(3deg)}}
.flame.off{animation:none;opacity:0;transition:opacity .3s;}
.smoke{width:4px;height:0;background:#ccc;margin:0 auto;border-radius:50%;opacity:0;}
.smoke.show{animation:smokeUp 1.1s ease-out forwards;}
@keyframes smokeUp{0%{opacity:.7;height:0}50%{opacity:.5;height:22px}100%{opacity:0;height:42px;transform:translateY(-16px)}}
.wick{width:3px;height:10px;background:#5a3d2b;margin:0 auto;}
.candle{width:9px;height:32px;margin:0 auto;border-radius:2px;
  background:repeating-linear-gradient(45deg,var(--pink),var(--pink) 4px,#fff 4px,#fff 8px);}
.cakeTop{width:110px;height:20px;margin:0 auto -7px;border-radius:50%;
  background:var(--card);border:3px solid #111;}
.cakeMid{width:130px;height:44px;margin:0 auto;border-left:3px solid #111;border-right:3px solid #111;
  background:linear-gradient(var(--lilac),var(--pink));}
.cakeBase{width:150px;height:16px;margin:0 auto;border:3px solid #111;border-radius:0 0 12px 12px;
  background:var(--comic);box-shadow:4px 4px 0 #111;}
</style>
"""

cake_js = """
function tiupLilin(){
  const f=document.getElementById('flame');
  if(f.classList.contains('off'))return;
  f.classList.add('off');
  document.getElementById('smoke').classList.add('show');
  document.getElementById('cakeHint').style.display='none';
  document.getElementById('cakeDone').style.display='block';
  boom();
}
"""

html = html.replace("<footer>", cake_section + "\n<footer>", 1)
html = html.replace("</head>", cake_style + "\n</head>", 1)
html = html.replace("</script>", cake_js + "\n</script>", 1)

with open("index.html","w",encoding="utf-8") as f:
    f.write(html)

print("Selesai! Section kue+lilin sudah ditambahkan.")
