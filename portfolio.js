// --- typed.js (centered) ---
document.addEventListener("DOMContentLoaded", function () {
  if (window.Typed) {
    new Typed("#typed", {
      strings: ["Frontend Developer", "Web Designer", "Freelancer"],
      typeSpeed: 60,
      backSpeed: 40,
      backDelay: 1200,
      loop: true,
      showCursor: true,
      cursorChar: "|"
    });
  } else {
    // fallback text
    document.getElementById("typed").innerText = "Frontend Developer";
  }

  // --- AOS init (animations on scroll) ---
  if (window.AOS) {
    AOS.init({ duration: 900, once: true });
  }

  // --- Isotope init (project filtering) ---
  var grid = document.querySelector('.project-grid');
  var iso;
  if (grid && window.Isotope) {
    iso = new Isotope(grid, {
      itemSelector: '.project-item',
      layoutMode: 'fitRows',
      percentPosition: true
    });
  }

  // filter buttons
  document.querySelectorAll('.filters [data-filter]').forEach(btn => {
    btn.addEventListener('click', function () {
      document.querySelectorAll('.filters .btn').forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      var filter = this.getAttribute('data-filter');
      if (iso) iso.arrange({ filter: filter });
    });
  });

  // --- Progress bars animation when visible ---
  const progBars = document.querySelectorAll('.progress-bar');
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const bar = entry.target;
        const w = bar.getAttribute('data-width') || '80';
        bar.style.width = w + '%';
        // set inner text if not present
        if (!bar.innerText) bar.innerText = w + '%';
      }
    });
  }, { threshold: 0.4 });

  progBars.forEach(bar => obs.observe(bar));

  // --- Set current year in footer ---
  var y = new Date().getFullYear();
  document.getElementById('year').innerText = y;

});
