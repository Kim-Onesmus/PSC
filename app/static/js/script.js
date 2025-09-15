// Mobile menu toggle
const mobileOpenButton = document.getElementById("mobile-open");
const mobileMenu = document.getElementById("mobile-menu");

if (mobileOpenButton && mobileMenu) {
  mobileOpenButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
  });
}

// Close mobile menu on link click
document.querySelectorAll("#mobile-menu a").forEach((link) => {
  link.addEventListener("click", () => {
    mobileMenu.classList.add("hidden");
  });
});

// Initialize Swiper for Organizations text carousel
document.addEventListener("DOMContentLoaded", () => {
  // eslint-disable-next-line no-undef
  const swiper = new Swiper(".swiper", {
    slidesPerView: 1,
    spaceBetween: 16,
    loop: true,
    autoplay: {
      delay: 3000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      640: { slidesPerView: 2 },
      1024: { slidesPerView: 3 },
    },
  });
});
