$(document).ready(function () {
    var path = window.location.pathname || '';
    var lang = path.indexOf('/kg') === 0 ? 'kg' : 'ru';
    try {
        localStorage.setItem('wedding_lang', lang);
    } catch (e) {}
    document.documentElement.lang = lang === 'kg' ? 'ky' : 'ru';

    $('.lang-btn').on('click', function (e) {
        e.preventDefault();
        var target = $(this).attr('href') || '/ru/';
        var nextLang = $(this).attr('hreflang') === 'ky' ? 'kg' : 'ru';
        try {
            localStorage.setItem('wedding_lang', nextLang);
        } catch (err) {}
        window.location.href = target + (window.location.hash || '');
    });
});
