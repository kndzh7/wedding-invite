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
        "seo.description": "Приглашение на свадьбу Эльдияра и Жамили. 9 сентября 2026, 16:00, ресторан Ak Bulut, Бишкек.",
        "seo.canonical": f"{SITE}/ru/",
        "seo.og_locale": "ru_RU",
        "seo.og_locale_alt": "ky_KG",
        "seo.og_title": "Эльдяр & Жамиля - приглашение на свадьбу",
        "seo.og_description": "Приглашаем Вас на свадьбу 9 сентября 2026 года в ресторане Ak Bulut.",
        "intro.hint": "ПРИГЛАШЕНИЕ",
        "intro.open": "Открыть",
        "music.on": "Включить музыку",
        "music.off": "Выключить музыку",
        "nav.invite": "Приглашение",
        "nav.events": "Гостям",
        "nav.photos": "Фото",
        "nav.venue": "Адрес",
        "hero.eyebrow": "Приглашение на свадьбу",
        "hero.date": "9 сентября 2026 · 16:00",
        "hero.venue": 'РЕСТОРАН "AK BULUT"',
        "invite.text": (
            "<p>С большой радостью приглашаем Вас на свадебное торжество наших детей.</p>"
            "<p>Пусть этот счастливый день станет ещё ярче в кругу близких и дорогих людей.</p>"
            "<p>Для нас будет большой честью разделить этот особенный день вместе с Вами.</p>"
            "<p>Ваше присутствие, доброе благословение и тёплые пожелания станут самым ценным подарком для молодых.</p>"
            "<p>Будем счастливы видеть Вас среди наших дорогих гостей!</p>"
        ),
        "invite.date_line": "9 сентября 2026 · 16:00 · Ak Bulut",
        "invite.hosts": "С уважением,<br>Тимур &amp; Назгуль",
        "events.message": (
            "<p class=\"guest-message-title\">Дорогие гости!</p>"
            "<p>Ваше присутствие сделает наш праздник еще теплее и прекраснее. "
            "Мы с нетерпением ждем возможности разделить с Вами самые счастливые мгновения этого особенного дня.</p>"
            "<p>Мы подготовили для Вас яркий, насыщенный и незабываемый вечер, наполненный приятными сюрпризами "
            "и особенными моментами.</p>"
            "<p>Самые важные и трогательные события начнутся с первых минут торжества. "
            "Будем очень рады, если Вы прибудете к началу сбора гостей, чтобы с самого начала разделить с нами "
            "атмосферу этого праздника и не пропустить ни одного важного момента.</p>"
        ),
        "dress.title": "Dress code",
        "dress.text": (
            "<strong>Классический, праздничный</strong><br>"
            "Костюмы, платья, нарядные образы — всё, в чём Вам будет комфортно и торжественно."
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
        "seo.description": "Эльдияр менен Жамилянын үйлөнүү тоюна чакыруу. 9-сентябрь 2026, 16:00, Ak Bulut рестораны, Бишкек.",
        "seo.canonical": f"{SITE}/kg/",
        "seo.og_locale": "ky_KG",
        "seo.og_locale_alt": "ru_RU",
        "seo.og_title": "Эльдияр & Жамиля - үйлөнүү тойго чакыруу",
        "seo.og_description": "Сиздерди 2026-жылдын 9-сентябрында Ak Bulut ресторанында өтүүчү үйлөнүү тойго чакырабыз.",
        "intro.hint": "ЧАКЫРУУ",
        "intro.open": "Ачуу",
        "music.on": "Музыканы күйгүзүү",
        "music.off": "Музыканы өчүрүү",
        "nav.invite": "Чакыруу",
        "nav.events": "Конокторго",
        "nav.photos": "Сүрөт",
        "nav.venue": "Дареги",
        "hero.eyebrow": "Үйлөнүү тойго чакыруу",
        "hero.date": "9-сентябрь, 2026-жыл · 16:00",
        "hero.venue": '"AK BULUT" РЕСТОРАНЫ',
        "invite.text": (
            "<p>Сиздерди балдарыбыздын үйлөнүү үлпөтүнө арналган салтанаттуу кечеге чын дилден чакырабыз.</p>"
            "<p>Өмүрдөгү эң унутулгус күндөрдүн биринде жакындарыбыз жана кадырлуу конокторубуз менен бирге болуп, "
            "бул кубанычтуу күндү Сиздер менен бөлүшүүнү чын жүрөктөн каалайбыз.</p>"
            "<p>Сиздердин катышууңуздар, ак батаңыздар жана жылуу каалоо-тилектериңиздер жаш жубайлар үчүн эң кымбат белек болот.</p>"
            "<p>Кадырлуу коногубуз болуп келиңиздер!</p>"
        ),
        "invite.date_line": "9-сентябрь, 2026 · 16:00 · Ak Bulut",
        "invite.hosts": "Урматтоо менен,<br>той ээлери<br>Тимур &amp; Назгуль",
        "events.message": (
            "<p class=\"guest-message-title\">Урматтуу коноктор!</p>"
            "<p>Сиздердин келишиңиздер биздин майрамыбызды дагы да көрккө бөлөйт. "
            "Бул өзгөчө күндүн кубанычын Сиздер менен бөлүшүүнү чыдамсыздык менен күтөбүз.</p>"
            "<p>Сиздер үчүн эстен кеткис, кубанычка, жагымдуу сюрприздерге жана өзгөчө көз ирмемдерге бай кече даярдадык.</p>"
            "<p>Майрамыбыздын эң маанилүү жана таасирдүү учурлары алгачкы мүнөттөрдөн тартып башталат. "
            "Ошондуктан майрамыбыздын өзгөчө маанайын башынан тартып биз менен бирге бөлүшүп, "
            "анын эң сонун көз ирмемдерине күбө болуу үчүн, Сиздерди конокторду тосуп алуу убактысына "
            "келип коюуңуздарды урматтоо менен өтүнөбүз.</p>"
        ),
        "dress.title": "Dress code",
        "dress.text": (
            "<strong>Классикалык, майрамдык</strong><br>"
            "Классикалык жана салтанаттуу кийим үлгүсү кубатталат. "
            "Өзүңүздөрдү ыңгайлуу жана жарашыктуу сезе турган кийим менен келсеңиздер болот."
        ),
        "photos.title": "Сүрөттөр",
        "photos.alt": "Эльдияр жана Жамиля",
        "map.title": "Кантип жетүүгө болот",
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
        "startDate": "2026-09-09T16:00:00+06:00",
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
