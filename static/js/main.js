// 내용
// $(document).ready(function () {
//   $("a").smoothScroll();
//   $(".menu-open").on("click", function () {
//     $(".menu-lst").toggleClass("menuPop");
//   });
//   $(".menuCls").on("click", function () {
//     $(".menu-lst").removeClass("menuPop");
//   });
// });

$(".menu-open").on("click", function (e) {
  $(".menu").toggleClass("on");
  if ($(".menu").hasClass("on") === true) {
    $(".menu-lst").addClass("menuPop");
    $(".menu-btn").css({ display: "none" });
    $(".menu-lst").css({ display: "block" });
  } else {
    $(".menu-lst").removeClass("menuPop");
    $(".menu-btn").css({ display: "block" });
    $(".menu-lst").css({ display: "none" });
  }
});

// about ani
(function () {
  var controller = new ScrollMagic.Controller({});

  var tween1 = TweenMax.to("#animate1", 0.3, {});

  var scene1 = new ScrollMagic.Scene({
    triggerElement: ".about__wrap",
  })
    .setClassToggle(".about_ani", "about_ani-big")
    .setTween(tween1)
    .addTo(controller);
})();

//portfolio slide
const swiper = new Swiper(".swiper", {
  slidesPerView: "4",
  slidesPerGroup: 1,
  spaceBetween: 25,
  loop: true,
  //   centeredSlides: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  scrollbars: false,
  slideToClickedSlide: true,
  breakpoints: {
    993: {
      slidesPerView: "4",
      spaceBetween: 25,
    },
    575: {
      slidesPerView: "1",
      spaceBetween: 27,
    },
    0: {
      slidesPerView: "1.3",
      spaceBetween: 10,
    },
  },
});

// 범위 랜덤 함수(소수점 2자리까지)
function random(min, max) {
  // `.toFixed()`를 통해 반환된 문자 데이터를,
  // `parseFloat()`을 통해 소수점을 가지는 숫자 데이터로 변환
  return parseFloat((Math.random() * (max - min) + min).toFixed(2));
}

function floatingObject(selector, delay, size) {
  // gsap.to(요소, 시간, 옵션)
  gsap.to(selector, random(1.5, 2.5), {
    y: size,
    repeat: -1, // -1 무한반복
    yoyo: true, // 애니메이션 되돌아오기(설정안할 시 끈킴)
    ease: Power1.easeInOut, // 타이밍함수
    delay: random(0, delay), // 지연시간
  });
}
floatingObject(".floating1", 1, 15);
floatingObject(".floating2", 0.5, 15);
// floatingObject(".contactArrow", 0.5, 15);

// introduce slider
// const left = $("#left-side");
// const handleOnMove = (e) => {
//   const p = (e.clientY / window.innerHeight) * 100;
//   left.css("height", `${p}vh`);
// };
// $(document).on("mousemove", (e) => handleOnMove(e));
// $(document).on("touchmove", (e) => handleOnMove(e.touches[0]));
var controller = new ScrollMagic.Controller({
  //   container: ".side", //body 스크롤이 아닌, 컨테이너 내부 스크롤 컨트롤
});
var tween1 = new TimelineMax();
tween1.add(TweenMax.to("#left-side", 1, { opacity: 1, height: "0" })); //.add 로 지정된 메서드는 동시 모션 실행
var scene1 = new ScrollMagic.Scene({
  triggerElement: ".introduce",
  triggerHook: "onLeave",
  duration: "100%",
})
  .setPin(".introduce")
  .setTween(tween1)
  .addTo(controller);

$(".contactBtn").hover(
  function () {
    $(".contactUs").slideDown();
  },
  function () {
    $(".contactUs").hide();
  }
);

gsap.registerPlugin(Draggable);
Draggable.create(".movingletter", {
  bounds: ".contact",
});

// about 페이지 스크롤 애니메이션
//$(function () {
// var controller = new ScrollMagic.Controller({
//    globalSceneOptions: {
//     triggerHook: "onLeave",
//   duration: "100%",
//   },
// });
// var slides = document.querySelectorAll("section.panel");
// for (var i = 0; i < slides.length; i++) {
//   new ScrollMagic.Scene({ triggerElement: slides[i] }).setPin(slides[i], { pushfollowers: false }).addIndicators().addTo(controller);
// }
//});
