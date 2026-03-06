(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    if (mobileNavToggleBtn) {
      mobileNavToggleBtn.classList.toggle('bi-list');
      mobileNavToggleBtn.classList.toggle('bi-x');
    }
  }

  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });
  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }

  if (scrollTop) {
    scrollTop.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }

  window.addEventListener('load', aosInit);

  /**
   * Initiate glightbox
   */
  if (typeof GLightbox !== "undefined") {
    GLightbox({
      selector: '.glightbox'
    });
  }

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {

    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;

    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {

      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });

    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {

      filters.addEventListener('click', function() {

        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');

        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

        if (typeof aosInit === 'function') {
          aosInit();
        }

      }, false);

    });

  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {

    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {

      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      new Swiper(swiperElement, config);

    });

  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();


  /**
   * CONTACT FORM AJAX
   */

  const contactForm = document.querySelector(".php-email-form");

  if (contactForm) {

    contactForm.addEventListener("submit", async function(e) {

      e.preventDefault();

      const loading = contactForm.querySelector(".loading");
      const errorBox = contactForm.querySelector(".error-message");
      const successBox = contactForm.querySelector(".sent-message");

      loading.style.display = "block";
      errorBox.style.display = "none";
      successBox.style.display = "none";

      const formData = new FormData(contactForm);

      try {

        const response = await fetch(contactForm.action, {
          method: "POST",
          body: formData,
          headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
          }
        });

        const data = await response.json();

        loading.style.display = "none";

        if (data.status === "success") {

          successBox.style.display = "block";
          contactForm.reset();

          setTimeout(() => {
            successBox.style.display = "none";
          }, 5000);

        } else {

          errorBox.innerHTML = data.message || "Error sending message";
          errorBox.style.display = "block";

        }

      } catch (error) {

        loading.style.display = "none";
        errorBox.innerHTML = "Server error. Please try again.";
        errorBox.style.display = "block";

      }

    });

  }

})();