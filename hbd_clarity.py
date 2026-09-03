with open("hbd.html","r",encoding="utf-8") as f:
    html = f.read()

old_font = """const fontSize = Math.min(canvas.width/7, 46);
octx.font = 'bold ' + fontSize + 'px Bangers, sans-serif';"""

new_font = """const fontSize = Math.min(canvas.width/6, 54);
octx.font = 'bold ' + fontSize + 'px Bangers, sans-serif';
octx.lineWidth = 2.5;
octx.strokeStyle = '#fff';"""

html = html.replace(old_font, new_font, 1)

old_draw = """lines.forEach((line,li)=>{
  octx.fillText(line, canvas.width/2, startY + li*lineHeight);
});"""

new_draw = """lines.forEach((line,li)=>{
  octx.fillText(line, canvas.width/2, startY + li*lineHeight);
  octx.strokeText(line, canvas.width/2, startY + li*lineHeight);
});"""

html = html.replace(old_draw, new_draw, 1)

old_gap = """const gap = 4;"""
new_gap = """const gap = 2;"""
html = html.replace(old_gap, new_gap, 1)

old_slice = """const targets = points.slice(0, 650);"""
new_slice = """const targets = points.slice(0, 1600);"""
html = html.replace(old_slice, new_slice, 1)

old_radius = "ctx.arc(p.cx, p.cy, 2.2, 0, Math.PI*2);"
new_radius = "ctx.arc(p.cx, p.cy, 1.6, 0, Math.PI*2);"
html = html.replace(old_radius, new_radius, 1)

with open("hbd.html","w",encoding="utf-8") as f:
    f.write(html)

print("Kejelasan tulisan berhasil ditingkatkan!")
