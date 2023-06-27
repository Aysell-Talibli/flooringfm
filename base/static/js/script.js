(function($) {

    "use strict";

    //Hide Loading Box (Preloader)
    function handlePreloader() {
        if ($('.preloader').length) {
            $('.preloader').delay(200).fadeOut(500);
        }
    }

    //Update Header Style and Scroll to Top
    function headerStyle() {
        if ($('.main-header').length) {
            var windowpos = $(window).scrollTop();
            var siteHeader = $('.main-header');
            var scrollLink = $('.scroll-to-top');
            if (windowpos >= 250) {
                siteHeader.addClass('fixed-header');
                scrollLink.fadeIn(300);
            } else {
                siteHeader.removeClass('fixed-header');
                scrollLink.fadeOut(300);
            }
        }
    }

    headerStyle();


    //Submenu Dropdown Toggle
    if ($('.main-header .navigation li.dropdown ul').length) {
        $('.main-header .navigation li.dropdown').append('<div class="dropdown-btn"><span class="fa fa-angle-down"></span></div>');

        //Dropdown Button
        $('.main-header .navigation li.dropdown .dropdown-btn').on('click', function() {
            $(this).prev('ul').slideToggle(500);
        });

        //Disable dropdown parent link
        $('.navigation li.dropdown > a').on('click', function(e) {
            e.preventDefault();
        });
    }


    //Portfolio Tabs
    if ($('.portfolio-tabs').length) {
        $('.portfolio-tabs .portfolio-tab-btns .p-tab-btn').on('click', function(e) {
            e.preventDefault();
            var target = $($(this).attr('data-tab'));

            if ($(target).hasClass('actve-tab')) {
                return false;
            } else {
                $('.portfolio-tabs .portfolio-tab-btns .p-tab-btn').removeClass('active-btn');
                $(this).addClass('active-btn');
                $('.portfolio-tabs .p-tabs-content .p-tab').removeClass('active-tab');
                $(target).addClass('active-tab');
            }
        });
    }


    //Portfolio Carousel
    if ($('.portfolio-carousel').length) {
        $('.portfolio-carousel').owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            smartSpeed: 700,
            autoplay: 5000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                800: {
                    items: 2
                },
                1024: {
                    items: 3
                },
                1200: {
                    items: 3
                },
                1400: {
                    items: 4
                },
                1600: {
                    items: 5
                }
            }
        });
    }


    //Testimonial Carousel
    if ($('.testimonial-carousel').length) {
        $('.testimonial-carousel').owlCarousel({
            loop: true,
            margin: 40,
            nav: true,
            smartSpeed: 700,
            autoplay: 5000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                800: {
                    items: 2
                },
                1024: {
                    items: 2
                },
                1200: {
                    items: 2
                }
            }
        });
    }


    // Sponsors Carousel
    if ($('.sponsors-carousel').length) {
        $('.sponsors-carousel').owlCarousel({
            loop: true,
            margin: 30,
            nav: true,
            smartSpeed: 500,
            autoplay: 4000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 2
                },
                600: {
                    items: 2
                },
                800: {
                    items: 3
                },
                1024: {
                    items: 4
                }
            }
        });
    }


    //Fact Counter + Text Count
    if ($('.count-box').length) {
        $('.count-box').appear(function() {

            var $t = $(this),
                n = $t.find(".count-text").attr("data-stop"),
                r = parseInt($t.find(".count-text").attr("data-speed"), 10);

            if (!$t.hasClass("counted")) {
                $t.addClass("counted");
                $({
                    countNum: $t.find(".count-text").text()
                }).animate({
                    countNum: n
                }, {
                    duration: r,
                    easing: "linear",
                    step: function() {
                        $t.find(".count-text").text(Math.floor(this.countNum));
                    },
                    complete: function() {
                        $t.find(".count-text").text(this.countNum);
                    }
                });
            }

        }, {
            accY: 0
        });
    }


    //Gallery With Filters
    if ($('.filter-list').length) {
        $('.filter-list').mixItUp({});
    }


    //Three Item Carousel
    if ($('.three-item-carousel').length) {
        $('.three-item-carousel').owlCarousel({
            loop: true,
            margin: 35,
            nav: true,
            smartSpeed: 700,
            autoplay: 4000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                800: {
                    items: 2
                },
                1024: {
                    items: 2
                },
                1200: {
                    items: 3
                }
            }
        });
    }


    // Product Carousel Slider
    if ($('.shop-page .image-carousel').length && $('.shop-page .thumbs-carousel').length) {

        var $sync1 = $(".shop-page .image-carousel"),
            $sync2 = $(".shop-page .thumbs-carousel"),
            flag = false,
            duration = 500;

        $sync1
            .owlCarousel({
                loop: false,
                items: 1,
                margin: 0,
                nav: false,
                navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
                dots: false,
                autoplay: true,
                autoplayTimeout: 5000
            })
            .on('changed.owl.carousel', function(e) {
                if (!flag) {
                    flag = false;
                    $sync2.trigger('to.owl.carousel', [e.item.index, duration, true]);
                    flag = false;
                }
            });

        $sync2
            .owlCarousel({
                loop: false,
                margin: 10,
                items: 1,
                nav: true,
                navText: ['<span class="icon flaticon-arrows-8"></span>', '<span class="icon flaticon-arrows-9"></span>'],
                dots: false,
                center: false,
                autoplay: true,
                autoplayTimeout: 5000,
                responsive: {
                    0: {
                        items: 3,
                        autoWidth: false
                    },
                    400: {
                        items: 3,
                        autoWidth: false
                    },
                    600: {
                        items: 3,
                        autoWidth: false
                    },
                    900: {
                        items: 5,
                        autoWidth: false
                    },
                    1000: {
                        items: 5,
                        autoWidth: false
                    }
                },
            })

            .on('click', '.owl-item', function() {
                $sync1.trigger('to.owl.carousel', [$(this).index(), duration, true]);
            })
            .on('changed.owl.carousel', function(e) {
                if (!flag) {
                    flag = true;
                    $sync1.trigger('to.owl.carousel', [e.item.index, duration, true]);
                    flag = false;
                }
            });
    }


    //Accordion Box
    if ($('.accordion-box').length) {
        $(".accordion-box").on('click', '.acc-btn', function() {

            var outerBox = $(this).parents('.accordion-box');
            var target = $(this).parents('.accordion');

            if ($(this).hasClass('active') !== true) {
                $(outerBox).find('.accordion .acc-btn').removeClass('active');
            }

            if ($(this).next('.acc-content').is(':visible')) {
                return false;
            } else {
                $(this).addClass('active');
                $(outerBox).children('.accordion').removeClass('active-block');
                $(outerBox).find('.accordion').children('.acc-content').slideUp(300);
                target.addClass('active-block');
                $(this).next('.acc-content').slideDown(300);
            }
        });
    }


    //Tabs Box
    if ($('.tabs-box').length) {
        $('.tabs-box .tab-buttons .tab-btn').on('click', function(e) {
            e.preventDefault();
            var target = $($(this).attr('data-tab'));

            if ($(target).is(':visible')) {
                return false;
            } else {
                target.parents('.tabs-box').find('.tab-buttons').find('.tab-btn').removeClass('active-btn');
                $(this).addClass('active-btn');
                target.parents('.tabs-box').find('.tabs-content').find('.tab').fadeOut(0);
                target.parents('.tabs-box').find('.tabs-content').find('.tab').removeClass('active-tab');
                $(target).fadeIn(300);
                $(target).addClass('active-tab');
            }
        });
    }


    //Single Item Carousel
    if ($('.single-item-carousel').length) {
        $('.single-item-carousel').owlCarousel({
            loop: true,
            margin: 10,
            nav: true,
            smartSpeed: 1000,
            autoplay: 5000,
            navText: ['<span class="fa fa-angle-left"></span>', '<span class="fa fa-angle-right"></span>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 1
                },
                1200: {
                    items: 1
                }
            }
        });
    }


    //Price Range Slider
    if ($('.range-slider-price').length) {

        var priceRange = document.getElementById('range-slider-price');

        noUiSlider.create(priceRange, {
            start: [180, 560],
            limit: 1000,
            behaviour: 'drag',
            connect: true,
            range: {
                'min': 100,
                'max': 1000
            }
        });

        var limitFieldMin = document.getElementById('min-value-rangeslider');
        var limitFieldMax = document.getElementById('max-value-rangeslider');

        priceRange.noUiSlider.on('update', function(values, handle) {
            (handle ? limitFieldMax : limitFieldMin).value = values[handle];
        });
    }


    //Jquery Spinner / Quantity Spinner
    if ($('.quantity-spinner').length) {
        $("input.quantity-spinner").TouchSpin({
            verticalbuttons: true
        });
    }


    //Custom Seclect Box
    if ($('.custom-select-box').length) {
        $('.custom-select-box').selectmenu().selectmenu('menuWidget').addClass('overflow');
    }

    //LightBox / Fancybox
    if ($('.lightbox-image').length) {
        $('.lightbox-image').fancybox({
            openEffect: 'fade',
            closeEffect: 'fade',
            helpers: {
                media: {}
            }
        });
    }


    //Contact Form Validation
    // if ($('#contact-form').length) {
    //     $('#contact-form').validate({
    //         rules: {
    //             firstname: {
    //                 required: true
    //             },
    //             lastname: {
    //                 required: true
    //             },
    //             email: {
    //                 required: true
    //             },
    //             message: {
    //                 required: true
    //             }
    //         }
    //     });
    // }


    // Scroll to a Specific Div
    if ($('.scroll-to-target').length) {
        $(".scroll-to-target").on('click', function() {
            var target = $(this).attr('data-target');
            // animate
            $('html, body').animate({
                scrollTop: $(target).offset().top
            }, 1000);

        });
    }


    // Elements Animation
    if ($('.wow').length) {
        var wow = new WOW({
            boxClass: 'wow', // animated element css class (default is wow)
            animateClass: 'animated', // animation css class (default is animated)
            offset: 0, // distance to the element when triggering the animation (default is 0)
            mobile: false, // trigger animations on mobile devices (default is true)
            live: true // act on asynchronously loaded content (default is true)
        });
        wow.init();
    }

    /* ==========================================================================
       When document is Scrollig, do
       ========================================================================== */

    $(window).on('scroll', function() {
        headerStyle();
    });

    /* ==========================================================================
       When document is loaded, do
       ========================================================================== */

    $(window).on('load', function() {
        handlePreloader();
    });

})(window.jQuery);

