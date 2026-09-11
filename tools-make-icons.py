from PIL import Image, ImageDraw
import os

BG     = (22, 24, 29, 255)      # charcoal, reads on light and dark toolbars
ORANGE = (255, 161, 22, 255)    # LeetCode orange
SS     = 8                      # supersample factor

def rr(d, box, r, fill):
    d.rounded_rectangle(box, radius=r, fill=fill)

def render(size):
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    u = lambda v: v * S  # unit -> px

    # tile
    rr(d, [0, 0, S - 1, S - 1], u(0.22), BG)

    # shackle: open ring above the body, legs tucked under it
    cx, cy = u(0.5), u(0.505)
    rad    = u(0.173)
    w      = int(u(0.076))
    d.arc([cx - rad, cy - rad, cx + rad, cy + rad], 180, 360, fill=ORANGE, width=w)
    for lx in (cx - rad, cx + rad):
        d.rectangle([lx - w / 2, cy - u(0.01), lx + w / 2, u(0.56)], fill=ORANGE)

    # body
    rr(d, [u(0.215), u(0.495), u(0.785), u(0.845)], u(0.072), ORANGE)

    # up-arrow keyhole cut out of the body (keyhole when tiny, arrow when large)
    ax, top, bot = u(0.5), u(0.565), u(0.775)
    hw, sw       = u(0.098), u(0.035)
    mid          = u(0.655)
    d.polygon([(ax, top), (ax + hw, mid), (ax + sw, mid), (ax + sw, bot),
               (ax - sw, bot), (ax - sw, mid), (ax - hw, mid)], fill=BG)

    return img.resize((size, size), Image.LANCZOS)

os.makedirs("assets", exist_ok=True)
for s in (16, 32, 48, 128):
    render(s).save(f"assets/icon{s}.png")
render(512).save("assets/icon512.png")
print("wrote", [f"assets/icon{s}.png" for s in (16, 32, 48, 128)])
