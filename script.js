// Initialize Lucide Icons (guarded in case lucide isn't available)
if (typeof lucide !== 'undefined' && lucide && typeof lucide.createIcons === 'function') {
  lucide.createIcons();
}

// Mobile Menu Toggle
// Mobile Menu Toggle (guarded)
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');
if (mobileMenuBtn && mobileMenu) {
  mobileMenuBtn.addEventListener('click', () => {
    mobileMenu.classList.toggle('hidden');
  });
  // Close mobile menu on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => mobileMenu.classList.add('hidden'));
  });
}

// Scroll Reveal
const revealElements = document.querySelectorAll('.reveal');
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
revealElements.forEach(el => revealObserver.observe(el));

const skillCounters = document.querySelectorAll('.skill-percent');
const skillFills = document.querySelectorAll('.skill-fill');
const skillBarObserver = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      skillCounters.forEach(el => {
        const target = Number(el.dataset.target) || 0;
        const duration = 1200;
        const start = performance.now();

        const animateValue = (now) => {
          const progress = Math.min((now - start) / duration, 1);
          el.textContent = `${Math.round(progress * target)}%`;
          if (progress < 1) {
            requestAnimationFrame(animateValue);
          }
        };

        requestAnimationFrame(animateValue);
      });

      skillFills.forEach(fill => {
        const rawFill = fill.style.getPropertyValue('--fill') || getComputedStyle(fill).getPropertyValue('--fill');
        if (rawFill) {
          fill.style.width = rawFill.trim();
        }
      });

      observer.disconnect();
    }
  });
}, { threshold: 0.2 });

const skillSection = document.querySelector('.skill-bar');
if (skillSection) {
  skillBarObserver.observe(skillSection);
}

// Portfolio Category Filter
const categoryBtns = document.querySelectorAll('.category-btn');
const portfolioCards = document.querySelectorAll('.portfolio-card');

categoryBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    categoryBtns.forEach(b => {
      b.classList.remove('active');
      b.classList.add('text-silver-mid');
    });
    btn.classList.add('active');
    btn.classList.remove('text-silver-mid');

    const cat = btn.dataset.cat;
    portfolioCards.forEach(card => {
      if (cat === 'all' || card.dataset.category === cat) {
        card.style.display = 'block';
        card.style.animation = 'slideUp 0.5s cubic-bezier(0.16,1,0.3,1) both';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// Portfolio card click behavior (prefer native anchors; attach handlers only to non-anchor cards)
const workCards = document.querySelectorAll('#work .portfolio-card');
workCards.forEach((card) => {
  // If this card is an anchor, let the browser handle the click via href + target
  if (card.tagName.toLowerCase() === 'a') {
    // ensure safe attributes exist
    if (!card.hasAttribute('target')) card.setAttribute('target', '_blank');
    if (!card.hasAttribute('rel')) card.setAttribute('rel', 'noopener noreferrer');
    return;
  }

  const videoUrl = card.getAttribute('data-youtube');
  if (videoUrl && videoUrl.trim()) {
    card.style.cursor = 'pointer';
    card.addEventListener('click', (event) => {
      window.open(videoUrl, '_blank', 'noopener,noreferrer');
    });
  } else {
    card.style.cursor = 'default';
  }
});

// Contact Form (guarded — some pages don't have the form)
const contactForm = document.getElementById('contactForm');
const formMessage = document.getElementById('formMessage');
const FORM_ENDPOINT = 'https://formspree.io/f/your-form-id';

if (contactForm) {
  contactForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const btn = contactForm.querySelector('button[type="submit"]');
    const originalButtonHtml = btn ? btn.innerHTML : '';

    if (btn) {
      btn.innerHTML = '<svg class="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="3" stroke-dasharray="30 70" stroke-linecap="round"/></svg> Sending...';
      btn.disabled = true;
    }

    try {
      const response = await fetch(FORM_ENDPOINT, {
        method: 'POST',
        headers: {
          'Accept': 'application/json'
        },
        body: new FormData(contactForm)
      });

      if (!response.ok) {
        throw new Error('Submission failed');
      }

      if (formMessage) {
        formMessage.classList.remove('hidden');
        formMessage.className = 'text-center text-sm font-medium py-2 text-green-400';
        formMessage.textContent = '✓ Message sent successfully. I\'ll get back to you within 24 hours.';
      }

      contactForm.reset();
    } catch (error) {
      if (formMessage) {
        formMessage.classList.remove('hidden');
        formMessage.className = 'text-center text-sm font-medium py-2 text-red-400';
        formMessage.textContent = '⚠ Unable to send right now. Please try again later or email me directly.';
      }
    } finally {
      if (btn) {
        btn.innerHTML = originalButtonHtml;
        btn.disabled = false;
      }
      if (typeof lucide !== 'undefined' && lucide && typeof lucide.createIcons === 'function') {
        lucide.createIcons();
      }

      if (formMessage) {
        setTimeout(() => {
          formMessage.classList.add('hidden');
        }, 5000);
      }
    }
  });
}

// Navbar background on scroll
const nav = document.querySelector('nav');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    nav.style.borderBottomColor = 'rgba(255,255,255,0.08)';
  } else {
    nav.style.borderBottomColor = 'rgba(255,255,255,0.03)';
  }
});

// Highlight current page nav link by default
(function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link').forEach(link => {
    const href = link.getAttribute('href');
    const linkPage = href.split('/').pop();
    if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
      link.classList.add('active');
    }
  });
})();

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Showreel placeholder click -> load video
const showreelPlaceholder = document.getElementById('showreelPlaceholder');
if (showreelPlaceholder) {
  showreelPlaceholder.addEventListener('click', () => {
    const iframe = document.createElement('iframe');
    iframe.src = 'https://player.vimeo.com/video/1203614608?badge=0&autopause=0&player_id=0&app_id=58479';
    iframe.title = 'Vincero-x-Sam-Newton-Commercial-ft-Karl';
    iframe.frameBorder = '0';
    iframe.allow = 'autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share';
    iframe.referrerPolicy = 'strict-origin-when-cross-origin';
    iframe.allowFullscreen = true;
    iframe.className = 'w-full h-full';
    showreelPlaceholder.replaceWith(iframe);
  });
}

// Editing Workflow IntersectionObserver (triggers the pop animation)
(function(){
  const container = document.getElementById('editingSteps');
  if(!container) return;
  const io = new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        entry.target.classList.add('play-steps');
        io.unobserve(entry.target);
      }
    });
  },{threshold:0.18});
  io.observe(container);
})();

// Addis Ababa Real-time Clock
const addisAbabaTimeElement = document.getElementById('addisAbabaTime');
if (addisAbabaTimeElement) {
  function updateAddisAbabaTime() {
    // Get current UTC time
    const now = new Date();
    
    // Addis Ababa is UTC+3 (East Africa Time)
    const addisTime = new Date(now.toLocaleString('en-US', { timeZone: 'Africa/Addis_Ababa' }));
    
    // Format as HH:MM
    const hours = String(addisTime.getHours()).padStart(2, '0');
    const minutes = String(addisTime.getMinutes()).padStart(2, '0');
    
    addisAbabaTimeElement.textContent = `${hours}:${minutes} ADDIS ABABA, ET`;
  }
  
  // Update immediately on page load
  updateAddisAbabaTime();
  
  // Update every second
  setInterval(updateAddisAbabaTime, 1000);
}
