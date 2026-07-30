$(document).ready(function () {

    /***************** Waypoints ******************/

    $('.wp1').waypoint(function () {
        $('.wp1').addClass('animated fadeInLeft');
    }, {
        offset: '75%'
    });
    $('.wp2').waypoint(function () {
        $('.wp2').addClass('animated fadeInRight');
    }, {
        offset: '75%'
    });
    $('.wp3').waypoint(function () {
        $('.wp3').addClass('animated fadeInLeft');
    }, {
        offset: '75%'
    });
    $('.wp4').waypoint(function () {
        $('.wp4').addClass('animated fadeInRight');
    }, {
        offset: '75%'
    });
    $('.wp5').waypoint(function () {
        $('.wp5').addClass('animated fadeInLeft');
    }, {
        offset: '75%'
    });
    $('.wp6').waypoint(function () {
        $('.wp6').addClass('animated fadeInRight');
    }, {
        offset: '75%'
    });
    $('.wp7').waypoint(function () {
        $('.wp7').addClass('animated fadeInUp');
    }, {
        offset: '75%'
    });
    $('.wp8').waypoint(function () {
        $('.wp8').addClass('animated fadeInLeft');
    }, {
        offset: '75%'
    });
    $('.wp9').waypoint(function () {
        $('.wp9').addClass('animated fadeInRight');
    }, {
        offset: '75%'
    });

    /***************** Initiate Flexslider ******************/
    $('.flexslider').flexslider({
        animation: "slide"
    });

    /***************** Initiate Fancybox ******************/

    $('.single_image').fancybox({
        padding: 4
    });

    $('.fancybox').fancybox({
        padding: 4,
        width: 1000,
        height: 800
    });

    /***************** Tooltips ******************/
    $('[data-toggle="tooltip"]').tooltip();

    /***************** Nav Transformicon ******************/

    /* When user clicks the Icon */
    $('.nav-toggle').click(function () {
        $(this).toggleClass('active');
        $('.header-nav').toggleClass('open');
        event.preventDefault();
    });
    /* When user clicks a link */
    $('.header-nav li a').click(function () {
        $('.nav-toggle').toggleClass('active');
        $('.header-nav').toggleClass('open');

    });

    /***************** Header BG Scroll ******************/

    $(function () {
        $(window).scroll(function () {
            var scroll = $(window).scrollTop();

            if (scroll >= 20) {
                $('section.navigation').addClass('fixed');
                $('header').css({
                    "border-bottom": "none",
                    "padding": "35px 0"
                });
                $('header .header-toolbar').css({
                    "top": "30px",
                });
            } else {
                $('section.navigation').removeClass('fixed');
                $('header').css({
                    "border-bottom": "solid 1px rgba(255, 255, 255, 0.2)",
                    "padding": "50px 0"
                });
                $('header .header-toolbar').css({
                    "top": "46px",
                });
            }
        });
    });
    /***************** Smooth Scrolling ******************/

    $(function () {

        $('a[href*=#]:not([href=#])').click(function () {
            if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {

                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top - 90
                    }, 2000);
                    return false;
                }
            }
        });

    });

    /********************** Embed youtube video *********************/
    if ($('.player').length) {
        $('.player').YTPlayer();
    }

    /********************** Background music **********************/
    (function () {
        var audio = document.getElementById('bg-music');
        var btn = document.getElementById('music-toggle');
        var gate = document.getElementById('intro-gate');
        var openBtn = document.getElementById('intro-open');
        if (!audio || !btn || !gate || !openBtn) {
            return;
        }

        audio.volume = 0.55;

        function setPlaying(playing) {
            var labelOn = btn.getAttribute('data-label-on') || 'Включить музыку';
            var labelOff = btn.getAttribute('data-label-off') || 'Выключить музыку';
            btn.classList.toggle('is-playing', playing);
            btn.classList.toggle('is-muted', !playing);
            btn.setAttribute('aria-label', playing ? labelOff : labelOn);
            btn.setAttribute('title', playing ? labelOff : labelOn);
        }

        function playMusic() {
            var playPromise = audio.play();
            if (playPromise && typeof playPromise.then === 'function') {
                return playPromise.then(function () {
                    setPlaying(true);
                }).catch(function () {
                    setPlaying(false);
                });
            }
            setPlaying(!audio.paused);
        }

        function openInvite() {
            playMusic();
            gate.classList.add('is-hidden');
            btn.hidden = false;
            setTimeout(function () {
                gate.style.display = 'none';
            }, 450);
        }

        openBtn.addEventListener('click', function (e) {
            e.preventDefault();
            openInvite();
        });

        gate.addEventListener('click', function (e) {
            if (e.target === gate) {
                openInvite();
            }
        });

        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            if (audio.paused) {
                playMusic();
            } else {
                audio.pause();
                setPlaying(false);
            }
        });
    })();

});
