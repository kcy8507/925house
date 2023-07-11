const loader = document.querySelector("#loader");
const html = document.querySelector("html");
window.addEventListener("load", () => {
  setTimeout(() => {
    //로딩속도 구현
    loader.style.opacity = "0";
    setTimeout(() => {
      loader.style.display = "none";
    }, 500);
  }, 500);
});
