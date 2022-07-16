$(document).ready(function () {

    $('.responsive').slick({
        // dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 2,
        responsive: [{
            breakpoint: 1024,
            settings: {
                slidesToShow: 6,
                slidesToScroll: 1,
                // centerMode: true,

            }

        }, {
            breakpoint: 800,
            settings: {
                slidesToShow: 3,
                slidesToScroll: 2,
                dots: true,
                infinite: true,

            }


        }, {
            breakpoint: 600,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2,
                dots: true,
                infinite: true,

            }
        }, {
            breakpoint: 480,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                dots: true,
                infinite: true,
                autoplay: true,
                autoplaySpeed: 2000,
            }
        }]
    });


});

       // Currency
        const apiUrl = 'https://nbu.uz/en/exchange-rates/json/'
        const usdPrice = document.querySelectorAll('.us-products-card-productPrice_dollar');
        const uzsPrice = document.querySelectorAll('.us-products-card-productPrice_som span')

        // Currency
       function WritePrice(usd, currecnyRate, element) {
            let finalPrice = Math.floor(currecnyRate * usd);
                element.innerHTML = finalPrice.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
       }

        async function ExchangeCurrency() {
            let response = await fetch(apiUrl);

            if (response.ok) {
                let json = await response.json();
                let CurrencyRate = json[json.length - 1]['cb_price'];
                //changeit
                uzsPrice.forEach(element => {
                let usdPriceOfElement = element.parentNode.previousElementSibling.innerHTML.substring(1);
                    WritePrice(usdPriceOfElement, CurrencyRate, element);
                });

            } else {
                alert("HTTP-Error: " + response.status);
            }
        }

        ExchangeCurrency()
/*------------------
    Preloader
--------------------*/
// jQuery(document).ready(function ($) {
//     $(window).on('load', function () {
//         $(".ctn-preloader").fadeOut();
//         $(".animation-preloader").delay(250).fadeOut();
//         $(".ctn-preloader").removeData();
//         $(".animation-preloader").removeData()
//     });
// })
// $(document).ready(function() {

// $('h3').magnificPopup({
//       delegate: 'a',
// 			gallery: {
// 			enabled: true
// 			},
// 			type: 'image'
// 		});

//   });

$(document).ready(function () {
    $(".minimalist-vertical-menu2").on("mouseleave", function () {
        $(".minimalist-tab-content2").removeClass("active");
        $(".minimalist-tab-menu2>.list-group2>.menu-item2").removeClass("active");
    });

    $(".menu-item2").on("mouseleave", function () {
        if (!$(".minimalist-tab-content2").hasClass("active")) {
            $(this).removeClass("active");
        }
    }).on("mouseenter", function (e) {
        e.preventDefault();
        $(this)
            .siblings(".menu-item2.active")
            .removeClass("active");
        $(this).addClass("active");
        var index = $(this).index();
        $(".minimalist-tab-content2")
            .removeClass("active")
        $(".minimalist-tab2>.minimalist-tab-content2")
            .eq(index)
            .addClass("active");
    });
});

$(document).ready(function () {
    $(".minimalist-vertical-menu3").on("mouseleave", function () {
        $(".minimalist-tab-content3").removeClass("active");
        $(".minimalist-tab-menu3>.list-group3>.menu-item3").removeClass("active");
    });

    $(".menu-item3").on("mouseleave", function () {
        if (!$(".minimalist-tab-content3").hasClass("active")) {
            $(this).removeClass("active");
        }
    }).on("mouseenter", function (e) {
        e.preventDefault();
        $(this)
            .siblings(".menu-item3.active")
            .removeClass("active");
        $(this).addClass("active");
        var index = $(this).index();
        $(".minimalist-tab-content3")
            .removeClass("active")
        $(".minimalist-tab3>.minimalist-tab-content3")
            .eq(index)
            .addClass("active");
    });
});

$('.btn1').click(function () {
    $(this).toggleClass("click");
    $('.sidebar').toggleClass("show");
});
$('.feat-btn').click(function () {
    $('nav ul .feat-show').toggleClass("show");
    $('nav ul .first').toggleClass("rotate");
});
$('.serv-btn').click(function () {
    $('nav ul .serv-show').toggleClass("show1");
    $('nav ul .second').toggleClass("rotate");
});
$('nav ul li').click(function () {
    $(this).addClass("active").siblings().removeClass("active");
});

(function () {
    var Accordion = function (el, multiple) {
        this.el = el || {};
        this.multiple = multiple || false;

        // Variables privadas
        var links = this.el.find('.link');
        // Evento
        links.on('click', {el: this.el, multiple: this.multiple}, this.dropdown)
    }

    Accordion.prototype.dropdown = function (e) {
        var $el = e.data.el;
        $this = $(this),
            $next = $this.next();

        $next.slideToggle();
        $this.parent().toggleClass('open');

        if (!e.data.multiple) {
            $el.find('.submenu').not($next).slideUp().parent().removeClass('open');
        }
        ;
    }

    var accordion = new Accordion($('#accordion3'), false);
});


document.addEventListener('DOMContentLoaded', function () {
    var splide = new Splide('.splide', {
        type: 'loop',
        perPage: 3,
        focus: 'center',
    });

    splide.mount();
});

(function () {

    $(".hamburger").on("click", function () {
        $(this).parent(".hamburger-wrapper").toggleClass("hamburger-active")
    });

}());


//splide 3
// menu

//  asd


(function ($) {
    $('.accordion5_1 > a').addClass('active').next().slideDown();

    $('.accordion5_1 a').click(function (j) {
        var dropDown = $(this).closest('li').find('p');

        $(this).closest('.accordion5_1').find('p').not(dropDown).slideUp();

        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).closest('.accordion5_1').find('a.active').removeClass('active');
            $(this).addClass('active');
        }

        dropDown.stop(false, true).slideToggle();

        j.preventDefault();
    });
})(jQuery);











