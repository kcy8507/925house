// 내용
$(document).ready(function () {
  $("a").smoothScroll();
  $(".menu-open").on("click", function () {
    $(".menu-lst").toggleClass("menuPop");
  });
  $(".menuCls").on("click", function () {
    $(".menu-lst").removeClass("menuPop");
  });
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
    .addTo(controller)
    .addIndicators({
      name: "1",
    });
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
const left = $("#left-side");
const handleOnMove = (e) => {
  const p = (e.clientX / window.innerWidth) * 100;
  left.css("width", `${p}%`);
};
$(document).on("mousemove", (e) => handleOnMove(e));
$(document).on("touchmove", (e) => handleOnMove(e.touches[0]));

$(".contactBtn").hover(
  function () {
    //이부분은 마우스가 올라 요소 위에 올라왔을때 이벤트입니다.
    // $(".contactUs").css({ display: "block" });
    $(".contactUs").slideDown();
  },
  function () {
    //이부분은 마우스가 요소에서 나갈떄 실행할 수 있는 이벤트 입니다.
    // $(".contactUs").css({ display: "none" });
    $(".contactUs").hide();
  }
);
