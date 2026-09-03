with open("hbd.html","r",encoding="utf-8") as f:
    html = f.read()

old_css = """  .deep{
    margin-top:22px; text-align:left; background:#fff; color:#222;
    border:3px solid #111; border-radius:18px; padding:24px 22px;
    box-shadow:5px 5px 0 #111; line-height:1.75; font-size:.95rem;
    opacity:0; transform:translateY(14px); transition:.6s ease;
  }
  .deep.show{opacity:1; transform:translateY(0);}"""

new_css = """  .deep{
    display:none;
    margin-top:22px; text-align:left; background:#fff; color:#222;
    border:3px solid #111; border-radius:18px; padding:24px 22px;
    box-shadow:5px 5px 0 #111; line-height:1.75; font-size:.95rem;
    opacity:0; transform:translateY(14px); transition:.6s ease;
  }
  .deep.show{display:block; opacity:0; transform:translateY(14px);}
  .deep.show.in{opacity:1; transform:translateY(0);}
  a.back{ display:none; }
  a.back.show{ display:inline-block; }"""

html = html.replace(old_css, new_css, 1)

html = html.replace(
    '<a class="back" href="index.html">← Kembali</a>',
    '<a class="back" id="backLink" href="index.html">← Kembali</a>'
)

old_reveal = """    document.getElementById('hint').style.display = 'none';
    const box = document.getElementById('deepMsg');
    box.classList.add('show');"""

new_reveal = """    document.getElementById('hint').style.display = 'none';
    const box = document.getElementById('deepMsg');
    box.classList.add('show');
    requestAnimationFrame(()=> box.classList.add('in'));
    document.getElementById('backLink').classList.add('show');"""

html = html.replace(old_reveal, new_reveal, 1)

old_color = "color: 'hsl(' + Math.floor((t.x/canvas.width)*360) + ',85%,62%)',"
new_color = "color: 'hsl(' + Math.floor(((t.x/canvas.width)*300 + 330) % 360) + ',90%,65%)',"
html = html.replace(old_color, new_color, 1)

with open("hbd.html","w",encoding="utf-8") as f:
    f.write(html)

print("hbd.html berhasil diperbaiki!")
