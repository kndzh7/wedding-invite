#!/usr/bin/env python3
"""Generate /ru/ and /kg/ pages from build/template.html."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "build" / "template.html"
SITE = "https://eldiyar-zhamilia.com"

PAGES = {
    "ru": {
        "lang": "ru",
        "html_lang": "ru",
        "path": "ru",
        "ru_active": " active",
        "kg_active": "",
        "seo.title": "Эльдяр & Жамиля - приглашение на свадьбу",
        "seo.description": "Приглашение на свадьбу Эльдияра и Жамили. 9 сентября 2026, 17:00, ресторан Ak Bulut, Бишкек.",
        "seo.canonical": f"{SITE}/ru/",
        "seo.og_locale": "ru_RU",
        "seo.og_locale_alt": "ky_KG",
        "seo.og_title": "Эльдяр & Жамиля - приглашение на свадьбу",
        "seo.og_description": "Приглашаем вас на свадьбу 9 сентября 2026 года в ресторане Ak Bulut.",
        "intro.hint": "Нажмите, чтобы открыть приглашение",
        "intro.open": "Открыть",
        "music.on": "Включить музыку",
        "music.off": "Выключить музыку",
        "nav.invite": "Приглашение",
        "nav.events": "Программа",
        "nav.photos": "Фото",
        "nav.venue": "Место",
        "hero.eyebrow": "Приглашение на свадьбу",
        "hero.date": "9 сентября 2026 · 17:00",
        "hero.venue": 'РЕСТОРАН "AK BULUT"',
        "invite.text": (
            "<span>С большой радостью приглашаем вас</span>"
            "<span>на свадебное торжество наших детей.</span>"
            "<span>Пусть этот счастливый день станет ещё ярче</span>"
            "<span>в кругу близких и дорогих людей.</span>"
            "<span>Будем рады вашему присутствию,</span>"
            "<span>вашему доброму благословению</span>"
            "<span>и будем счастливы видеть вас</span>"
            '<span class="invite-finale">среди наших дорогих гостей</span>'
        ),
        "invite.date_line": "9 сентября 2026 · 17:00 · Ak Bulut",
        "invite.hosts": "С уважением Тимур &amp; Назгуль",
        "events.title": "Программа",
        "events.day": "9 сентября 2026",
        "events.item1": "Встреча и сбор дорогих гостей",
        "events.item2": "Welcome-зона в ожидании начала торжества",
        "events.item3": "Открытие праздничного вечера",
        "events.item4": "Первый музыкальный антракт",
        "events.item5": "Второй музыкальный антракт",
        "events.item6": "Окончание торжественной программы",
        "events.place": "Ресторан «Ak Bulut»",
        "dress.title": "Dress code",
        "dress.text": (
            "<strong>Классический, праздничный</strong><br>"
            "Костюмы, платья, нарядные образы — всё, в чём вам будет комфортно и торжественно."
        ),
        "photos.title": "Фотографии",
        "photos.alt": "Эльдияр и Жамиля",
        "map.title": "Как добраться?",
        "map.address": "ул. 7 апреля, 120/1, Бишкек",
        "map.open_2gis": "Открыть в 2GIS",
        "map.iframe_title": "Ak Bulut — 2GIS",
        "jsonld_name": "Свадьба Эльдияра и Жамили",
        "jsonld_description": "Свадебное торжество 9 сентября 2026 года в ресторане Ak Bulut, Бишкек.",
    },
    "kg": {
        "lang": "kg",
        "html_lang": "ky",
        "path": "kg",
        "ru_active": "",
        "kg_active": " active",
        "seo.title": "Эльдияр & Жамиля - үйлөнүү тойго чакыруу",
        "seo.description": "Эльдияр менен Жамилянын үйлөнүү тоюна чакыруу. 9-сентябрь 2026, 17:00, Ak Bulut рестораны, Бишкек.",
        "seo.canonical": f"{SITE}/kg/",
        "seo.og_locale": "ky_KG",
        "seo.og_locale_alt": "ru_RU",
        "seo.og_title": "Эльдияр & Жамиля - үйлөнүү тойго чакыруу",
        "seo.og_description": "Сиздерди 2026-жылдын 9-сентябрында Ak Bulut ресторанында өтүүчү үйлөнүү тойго чакырабыз.",
        "intro.hint": "Чакырууну ачуу үчүн басыңыз",
        "intro.open": "Ачуу",
        "music.on": "Музыканы күйгүзүү",
        "music.off": "Музыканы өчүрүү",
        "nav.invite": "Чакыруу",
        "nav.events": "Программа",
        "nav.photos": "Сүрөт",
        "nav.venue": "Жер",
        "hero.eyebrow": "Үйлөнүү тойго чакыруу",
        "hero.date": "9-сентябрь, 2026-жыл · 17:00",
        "hero.venue": 'РЕСТОРАН "AK BULUT"',
        "invite.text": (
            "<span>Сиздерди</span>"
            "<span>балдарыбыздын</span>"
            "<span>үйлөнүү үлпөт тоюна</span>"
            "<span>арналган салтанаттуу</span>"
            "<span>кечесине келип,</span>"
            "<span>ак дасторкондун үстүнө</span>"
            "<span>батаңыздарды берип,</span>"
            "<span>кадырлуу коногубуз</span>"
            "<span>болуп кетүүгө</span>"
            '<span class="invite-finale">чакырабыз</span>'
        ),
        "invite.date_line": "9-сентябрь, 2026 · 17:00 · Ak Bulut",
        "invite.hosts": "Урматтуу менен той ээси Тимур &amp; Назгуль",
        "events.title": "Программа",
        "events.day": "9-сентябрь, 2026-жыл",
        "events.item1": "Кадырлуу конокторду тосуп алуу жана чогулуу",
        "events.item2": "Салтанат башталганга чейинки Welcome-зона",
        "events.item3": "Майрамдык кечени ачуу",
        "events.item4": "Биринчи музыкалык антракт",
        "events.item5": "Экинчи музыкалык антракт",
        "events.item6": "Салтанаттуу программанын аягы",
        "events.place": "«Ak Bulut» рестораны",
        "dress.title": "Dress code",
        "dress.text": (
            "<strong>Классикалык, майрамдык</strong><br>"
            "Костюм, көйнөк, салтанаттуу кийим — өзүңүздөргө ыңгайлуу жана майрамдык көрүнүштө келиңиздер."
        ),
        "photos.title": "Сүрөттөр",
        "photos.alt": "Эльдияр жана Жамиля",
        "map.title": "Кантип жетсе болот?",
        "map.address": "7-апрель көч., 120/1, Бишкек",
        "map.open_2gis": "2GISте ачуу",
        "map.iframe_title": "Ak Bulut — 2GIS",
        "jsonld_name": "Эльдияр менен Жамилянын үйлөнүү тою",
        "jsonld_description": "2026-жылдын 9-сентябрында Бишкектеги Ak Bulut ресторанында өтүүчү үйлөнүү той.",
    },
}


def escape_attr(value: str) -> str:
    return (
        value.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render(template: str, data: dict) -> str:
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Event",
        "name": data["jsonld_name"],
        "description": data["jsonld_description"],
        "startDate": "2026-09-09T17:00:00+06:00",
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "image": [f"{SITE}/img/background.JPEG"],
        "url": data["seo.canonical"],
        "inLanguage": data["html_lang"],
        "location": {
            "@type": "Place",
            "name": "Ak Bulut",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "ул. 7 апреля, 120/1",
                "addressLocality": "Бишкек",
                "addressCountry": "KG",
            },
        },
        "organizer": {
            "@type": "Person",
            "name": "Тимур & Назгуль",
        },
    }

    values = dict(data)
    values["seo.jsonld"] = json.dumps(jsonld, ensure_ascii=False, indent=2)

    # Attribute-safe SEO fields used in meta content="..."
    for key in (
        "seo.title",
        "seo.description",
        "seo.og_title",
        "seo.og_description",
        "music.on",
        "music.off",
        "photos.alt",
        "map.iframe_title",
    ):
        values[key] = escape_attr(values[key])

    result = template
    for key, value in values.items():
        result = result.replace("{{" + key + "}}", value)
    leftover = [part for part in result.split("{{") if "}}" in part]
    if leftover:
        keys = [part.split("}}", 1)[0] for part in leftover]
        raise SystemExit(f"Unresolved placeholders: {', '.join(sorted(set(keys)))}")
    return result


def main() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    for code, data in PAGES.items():
        out_dir = ROOT / data["path"]
        out_dir.mkdir(parents=True, exist_ok=True)
        out_file = out_dir / "index.html"
        out_file.write_text(render(template, data), encoding="utf-8")
        print(f"Wrote {out_file.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
