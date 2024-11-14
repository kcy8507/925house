window.onload = () => {
  let websiteImages = document.querySelectorAll(".menu-website>.card-wrapper");
  let websiteHeight = document.querySelector(".menu-website");
  let brandingImages = document.querySelectorAll(".menu-branding>.card-wrapper");
  let brandingHeight = document.querySelector(".menu-branding");
  let videoImages = document.querySelectorAll(".menu-video>.card-wrapper");
  let videoHeight = document.querySelector(".menu-video");
  let appImages = document.querySelectorAll(".menu-app>.card-wrapper");
  let appHeight = document.querySelector(".menu-app");
  let catalogImages = document.querySelectorAll(".menu-catalog>.card-wrapper");
  let catalogHeight = document.querySelector(".menu-catalog");
  let tabEls = document.querySelectorAll(".menu-section-wrap [data-index]");
  let tabEl = [...tabEls];
  let menuEls = document.querySelectorAll(".portfolio-menu li");
  let menuEl = [...menuEls];
  let allHeight = document.querySelector(".menu-section-wrap");

  let imgStack = [0, 0, 0];

  let colWidth = innerWidth;
  //반응형
  let resizeId = "";
  window.addEventListener("resize", function () {
    this.clearTimeout(resizeId);
    resizeId = setTimeout(doneResizing, 300);
  });

  function doneResizing() {
    let innerWidth = window.innerWidth;
    let innerContainerWidth = document.querySelector(".menu-section-wrap").offsetWidth;
    let imgW;
    if (innerWidth <= "576") {
      imgStack = [0, 0];
      colWidth = innerContainerWidth / 2;
      imgW = innerContainerWidth / 2;
      let cards = document.querySelectorAll(".card-wrapper");
      cards.forEach((card, i) => {
        cards[i].style.maxWidth = `${imgW}px`;
      });
    } else if (innerWidth <= "992") {
      imgStack = [0, 0];
      colWidth = innerContainerWidth / 2;
      imgW = innerContainerWidth / 2;
      let cards = document.querySelectorAll(".card-wrapper");
      cards.forEach((card, i) => {
        cards[i].style.maxWidth = `${imgW}px`;
      });
      // } else if (innerWidth <= "1700") {
      //   imgStack = [0, 0, 0];
      //   colWidth = innerContainerWidth / 3;
      //   imgW = innerContainerWidth / 3;
      //   let cards = document.querySelectorAll(".card-wrapper");
      //   cards.forEach((card, i) => {
      //     cards[i].style.maxWidth = `${imgW}px`;
      //   });
    } else {
      imgStack = [0, 0];
      colWidth = innerContainerWidth / 2;
      imgW = innerContainerWidth / 2;
      let cards = document.querySelectorAll(".card-wrapper");
      cards.forEach((card, i) => {
        cards[i].style.maxWidth = `${imgW}px`;
      });
    }
  }
  doneResizing();

  // menu탭 내용을 하나씩 잡았음
  // 카드가 리셋 되어야 함

  for (let i = 0; i < menuEl.length; i++) {
    menuEl[i].setAttribute("data-index", i);
    // tabEl[i].dataset.id = i;
    menuEl[i].addEventListener("click", (e) => {
      openTab(e.target.getAttribute("data-index"));
    });
  }

  function openTab(index) {
    menuEl.forEach((el) => el.classList.remove("selected"));
    tabEl.forEach((el) => el.classList.remove("active"));
    tabEl[index].classList.add("active");
    menuEl[index].classList.add("selected");
  }
  // 메뉴 누르면 탭 넘어가기

  // menuEl[0].addEventListener('click',function(){
  //   let offset = $(".portfolio-container").offset().top;
  //   console.log($(this))
  //   console.log(offset)
  //   console.log('이동',offset)

  //   $('html,body').animate({scrollTop : offset});
  // })

  menuEl.forEach((menuEls, i) => {
    menuEls.addEventListener("click", function () {
      let offset = $(".portfolio-container").offset().top;
      console.log($(this));
      console.log(offset);
      console.log("이동", offset);
      $("html,body").animate({ scrollTop: offset }, 0);
    });
  });

  for (let i = 0; i < websiteImages.length; i++) {
    let minIndex = imgStack.indexOf(Math.min.apply(0, imgStack));
    // 최소값
    // apply(null, imgStack)도 상관X
    let x = colWidth * minIndex;
    let y = imgStack[minIndex];
    imgStack[minIndex] += websiteImages[i].children[0].firstElementChild.height + 20;
    // 이미지 높이에+20
    websiteImages[i].style.transform = `translateX(${x}px) translateY(${y}px)`;
    // 그냥 애니메이션
    if (i === websiteImages.length - 1) {
      allHeight.offsetHeight = `${Math.max.apply(0, imgStack)}px`;
      allHeight.style.height = `${Math.max.apply(0, imgStack)}px`;
    }
  }
  menuEl[0].addEventListener("click", () => {
    doneResizing();
    for (let i = 0; i < websiteImages.length; i++) {
      let minIndex = imgStack.indexOf(Math.min.apply(0, imgStack));
      // 최소값
      // apply(null, imgStack)도 상관X
      let x = colWidth * minIndex;
      let y = imgStack[minIndex];
      imgStack[minIndex] += websiteImages[i].children[0].firstElementChild.height + 20;
      // 이미지 높이에+20
      websiteImages[i].style.transform = `translateX(${x}px) translateY(${y}px)`;
      // 그냥 애니메이션
      if (i === websiteImages.length - 1) {
        allHeight.offsetHeight = `${Math.max.apply(0, imgStack)}px`;
        allHeight.style.height = `${Math.max.apply(0, imgStack)}px`;
      }
    }
  });
  menuEl[1].addEventListener("click", () => {
    doneResizing();
    for (let i = 0; i < brandingImages.length; i++) {
      let minIndex = imgStack.indexOf(Math.min.apply(0, imgStack));
      // 최소값
      // apply(null, imgStack)도 상관X
      let x = colWidth * minIndex;
      let y = imgStack[minIndex];
      imgStack[minIndex] += brandingImages[i].children[0].height + 20;
      // 이미지 높이에+20
      brandingImages[i].style.transform = `translateX(${x}px) translateY(${y}px)`;
      // 그냥 애니메이션
      if (i === brandingImages.length - 1) {
        allHeight.style.height = `${Math.max.apply(0, imgStack)}px`;
      }
    }
  });
};
