#!/usr/bin/env python3
"""Generate Kyrgyz WhatsApp invitation cards with large readable type."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "img" / "cards"
FONT_REG = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
FONT_ITALIC = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"

BG = (252, 249, 242)
INK = (45, 50, 62)
GOLD = (201, 154, 60)
GOLD_BRIGHT = (214, 170, 72)
MUTED = (95, 100, 112)

# Vertical 16:9 => 9:16 portrait (WhatsApp Stories / phone share)
W, H = 1080, 1920


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_centered(
    draw: ImageDraw.ImageDraw,
    text: str,
    y: int,
    fnt: ImageFont.FreeTypeFont,
    fill,
    max_width: int,
    line_gap: int,
) -> int:
    lines = wrap(draw, text, fnt, max_width)
    for line in lines:
        width = draw.textlength(line, font=fnt)
        draw.text(((W - width) / 2, y), line, font=fnt, fill=fill)
        y += fnt.size + line_gap
    return y


def gold_diamond(draw: ImageDraw.ImageDraw, cx: int, cy: int, size: int = 10) -> None:
    """Draw a small gold diamond ornament (not a font glyph)."""
    points = [
        (cx, cy - size),
        (cx + size, cy),
        (cx, cy + size),
        (cx - size, cy),
    ]
    draw.polygon(points, outline=GOLD_BRIGHT)
    inner = max(4, size - 4)
    points_inner = [
        (cx, cy - inner),
        (cx + inner, cy),
        (cx, cy + inner),
        (cx - inner, cy),
    ]
    draw.polygon(points_inner, outline=GOLD_BRIGHT)


def ornament(draw: ImageDraw.ImageDraw, y: int) -> int:
    gold_diamond(draw, W // 2, y + 12, 11)
    return y + 52


def divider(draw: ImageDraw.ImageDraw, y: int) -> int:
    x0, x1 = W // 2 - 110, W // 2 + 110
    for i in range(x0, x1):
        t = abs((i - W / 2) / 110)
        alpha = max(0.0, 1 - t)
        color = (
            int(GOLD_BRIGHT[0] * alpha + BG[0] * (1 - alpha)),
            int(GOLD_BRIGHT[1] * alpha + BG[1] * (1 - alpha)),
            int(GOLD_BRIGHT[2] * alpha + BG[2] * (1 - alpha)),
        )
        draw.point((i, y), fill=color)
        draw.point((i, y + 1), fill=color)
    gold_diamond(draw, W // 2, y + 1, 6)
    return y + 44


def card_base() -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    margin = 48
    draw.rectangle([margin, margin, W - margin, H - margin], outline=GOLD_BRIGHT, width=3)
    draw.rectangle(
        [margin + 12, margin + 12, W - margin - 12, H - margin - 12],
        outline=(230, 200, 130),
        width=1,
    )
    return img, draw


def save(img: Image.Image, name: str) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    img.save(path, "JPEG", quality=92, optimize=True)
    print(f"Wrote {path.relative_to(ROOT)} ({W}x{H})")
    return path


def card_invite() -> Path:
    """Main invitation + key details in one card."""
    img, draw = card_base()
    y = 120
    y = ornament(draw, y)

    y = draw_centered(draw, "ҮЙЛӨНҮҮ ТОЙГО ЧАКЫРУУ", y, font(FONT_BOLD, 42), GOLD_BRIGHT, 900, 12)
    y += 32
    y = draw_centered(draw, "Эльдияр  &  Жамиля", y, font(FONT_REG, 82), INK, 920, 8)
    y += 18
    y = divider(draw, y)
    y += 14

    y = draw_centered(
        draw,
        "Сиздерди балдарыбыздын үйлөнүү үлпөтүнө арналган салтанаттуу кечеге чын дилибиздең чакырабыз.",
        y,
        font(FONT_REG, 42),
        INK,
        880,
        16,
    )
    y += 36
    y = divider(draw, y)
    y += 16

    details = [
        ("Күнү", "9-сентябрь, 2026-жыл"),
        ("Убакыт", "саат 16:00"),
        ("Дареги", '"Ak Bulut" рестораны\n7-апрель көч., 120/1, Бишкек'),
    ]
    label_f = font(FONT_BOLD, 34)
    value_f = font(FONT_REG, 48)
    for label, value in details:
        draw.text(((W - draw.textlength(label, font=label_f)) / 2, y), label, font=label_f, fill=GOLD_BRIGHT)
        y += 46
        for part in value.split("\n"):
            y = draw_centered(draw, part, y, value_f, INK, 900, 12)
        y += 28

    y += 10
    y = divider(draw, y)
    y += 12
    y = draw_centered(draw, "Урматтоо менен,", y, font(FONT_ITALIC, 36), MUTED, 880, 10)
    y = draw_centered(draw, "той ээлери", y, font(FONT_ITALIC, 36), MUTED, 880, 10)
    y += 10
    y = draw_centered(draw, "Тимур  &  Назгуль", y, font(FONT_BOLD, 48), INK, 880, 10)
    y += 44
    y = draw_centered(draw, "Толук маалымат:", y, font(FONT_ITALIC, 34), MUTED, 880, 8)
    y += 8
    y = draw_centered(draw, "eldiyar-zhamilia.com/kg/", y, font(FONT_BOLD, 38), GOLD_BRIGHT, 900, 10)

    return save(img, "whatsapp-kg-chakiru.jpg")


def card_guests() -> Path:
    img, draw = card_base()
    y = 160
    y = ornament(draw, y)
    y = draw_centered(draw, "Урматтуу коноктор!", y, font(FONT_BOLD, 62), GOLD_BRIGHT, 900, 12)
    y += 36
    y = divider(draw, y)
    y += 24

    paragraphs = [
        "Сиздердин келишиңиздер биздин майрамыбызды дагы да көрккө бөлөйт.",
        "Бул өзгөчө күндүн кубанычын Сиздер менен бөлүшүүнү чыдамсыздык менен күтөбүз.",
        "Майрамыбыздын эң маанилүү учурлары алгачкы мүнөттөрдөн тартып башталат.",
        "Ошондуктан Сиздерди конокторду тосуп алуу убактысына келип коюуңуздарды урматтоо менен өтүнөбүз.",
    ]
    for p in paragraphs:
        y = draw_centered(draw, p, y, font(FONT_REG, 46), INK, 880, 18)
        y += 36

    y += 20
    y = divider(draw, y)
    y += 24
    y = draw_centered(draw, "9-сентябрь · 16:00 · Ak Bulut", y, font(FONT_BOLD, 44), GOLD_BRIGHT, 900, 12)
    y += 40
    y = draw_centered(draw, "eldiyar-zhamilia.com/kg/", y, font(FONT_BOLD, 36), GOLD_BRIGHT, 900, 10)
    return save(img, "whatsapp-kg-konoktor.jpg")


def main() -> None:
    # Remove obsolete details-only card
    old = OUT / "whatsapp-kg-maalymat.jpg"
    if old.exists():
        old.unlink()
        print(f"Removed {old.relative_to(ROOT)}")

    card_invite()
    card_guests()


if __name__ == "__main__":
    main()
