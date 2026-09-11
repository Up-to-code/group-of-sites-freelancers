from PIL import Image, ImageDraw

S = 512
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)

# Soft indigo rounded-square background
r = 116
d.rounded_rectangle([0, 0, S - 1, S - 1], radius=r, fill=(79, 70, 229, 255))

# White "profile network" glyph: hub node + orbiting nodes
cx, cy, R = S // 2, S // 2, 132
nodes = [(cx, cy), (cx, cy - R), (cx - int(R * 0.9), cy + int(R * 0.45)), (cx + int(R * 0.9), cy + int(R * 0.45))]
d.line([nodes[0], nodes[1]], fill=(255, 255, 255, 90), width=26)
d.line([nodes[0], nodes[2]], fill=(255, 255, 255, 90), width=26)
d.line([nodes[0], nodes[3]], fill=(255, 255, 255, 90), width=26)
d.line([nodes[1], nodes[2]], fill=(255, 255, 255, 90), width=26)
d.line([nodes[1], nodes[3]], fill=(255, 255, 255, 90), width=26)

def orb(pt, r_in, r_out):
    d.ellipse([pt[0] - r_out, pt[1] - r_out, pt[0] + r_out, pt[1] + r_out], fill=(255, 255, 255, 255))
    d.ellipse([pt[0] - r_in, pt[1] - r_in, pt[0] + r_in, pt[1] + r_in], fill=(79, 70, 229, 255))

orb(nodes[0], 62, 86)
orb(nodes[1], 30, 46)
orb(nodes[2], 30, 46)
orb(nodes[3], 30, 46)

for size in (16, 32, 48, 128):
    img.resize((size, size), Image.LANCZOS).save(f"extension/icons/icon{size}.png")
print("icons written")