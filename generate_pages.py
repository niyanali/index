from pathlib import Path
import re

root = Path(__file__).parent
NAV_LINKS = [
    ("work.html", "Work"),
    ("about.html", "About"),
    ("cases.html", "Cases"),
    ("shop.html", "Shop"),
    ("contact.html", "Contact"),
]


def nav_html(active, show_cart=False):
    desktop = []
    mobile = []
    for href, label in NAV_LINKS:
        desktop_css = "text-white" if href == active else "text-silver-mid hover:text-white transition-colors"
        mobile_css = "text-white" if href == active else "text-silver-mid hover:text-white"
        desktop.append(f"      <a href=\"{href}\" class=\"nav-link text-xs font-medium tracking-wider uppercase {desktop_css}\">{label}</a>")
        mobile.append(f"    <a href=\"{href}\" class=\"block text-sm font-medium tracking-wider uppercase {mobile_css}\">{label}</a>")
    cart = ""
    if show_cart:
        cart = "      <a href=\"#cart\" class=\"hidden sm:inline-flex items-center gap-2 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-[10px] font-bold uppercase tracking-[0.18em] text-white hover:bg-white/10 transition-colors\">\n        <i data-lucide=\"shopping-cart\" class=\"w-4 h-4\"></i> Checkout\n      </a>\n"
    desktop_html = "\n".join(desktop)
    mobile_html = "\n".join(mobile)
    return f"""<!-- NAVIGATION -->
<nav class=\"fixed top-0 left-0 w-full z-50 bg-dark-900/85 backdrop-blur-xl border-b border-white/5\">
  <div class=\"max-w-full mx-auto px-5 py-3 flex items-center justify-between\">
    <a href=\"index.html\" class=\"flex items-center gap-3\">
      <div class=\"w-9 h-9 rounded-sm bg-neon-orange flex items-center justify-center font-black text-dark-900 text-sm tracking-tighter\">NA</div>
      <div class=\"hidden sm:block\">
        <div class=\"text-sm font-bold tracking-tight text-white leading-none\">NIYAN ALI</div>
        <div class=\"text-[10px] font-medium tracking-[0.2em] text-silver-dark uppercase\">Filmmaker</div>
      </div>
    </a>
    <div class=\"hidden md:flex items-center gap-7\">
{desktop_html}
{cart}    </div>
    <div class=\"flex items-center gap-3\">
      <div class=\"hidden sm:flex items-center gap-1.5 text-[10px] text-silver-dark tracking-wider uppercase\">
        <span class=\"w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse\"></span>
        <span id=\"addisAbabaTime\">--:-- ADDIS ABABA, ET</span>
      </div>
      <a href=\"contact.html\" class=\"cta-btn bg-neon-orange text-dark-900 px-5 py-2.5 text-xs font-bold tracking-wider uppercase hover:bg-neon-orangeHover hidden sm:inline-flex\">Get in Touch</a>
      <button id=\"mobileMenuBtn\" class=\"md:hidden text-white p-1.5\"><i data-lucide=\"menu\" class=\"w-5 h-5\"></i></button>
    </div>
  </div>
  <div id=\"mobileMenu\" class=\"hidden md:hidden bg-dark-800/95 backdrop-blur-xl border-t border-white/5 px-5 py-5 space-y-4\">
{mobile_html}
  </div>
</nav>
"""


def page_head(title):
    template = """<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>{title}</title>
<script src=\"https://cdn.tailwindcss.com\"></script>
<script src=\"https://unpkg.com/lucide@latest\"></script>
<link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap\" rel=\"stylesheet\">
<script>
tailwind.config = {
  theme: { extend: {
    fontFamily: { 'inter': ['Inter', 'sans-serif'] },
    colors: {
      neon: { orange: '#FF4F30', orangeHover: '#FF6A4D' },
      silver: { light: '#E8E8E8', mid: '#A0A0A0', dark: '#6B6B6B' },
      dark: { 900: '#050505', 800: '#0A0A0A', 700: '#111111', 600: '#1A1A1A', 500: '#222222' }
    }
  }}
}
</script>
<link rel=\"stylesheet\" href=\"style.css\">
</head>
<body class=\"grain-overlay scanline-overlay\">
"""
    return template.replace('{title}', title)


def page_footer():
    return """<footer class=\"border-t border-white/5 py-8\">
  <div class=\"max-w-full mx-auto px-5\">
    <div class=\"flex flex-col md:flex-row items-center justify-between gap-4\">
      <div class=\"flex items-center gap-3\">
        <div class=\"w-7 h-7 rounded-sm bg-neon-orange flex items-center justify-center font-black text-dark-900 text-[10px] tracking-tighter\">NA</div>
        <span class=\"text-xs font-bold tracking-tight text-white\">NIYAN ALI</span>
        <span class=\"text-[10px] text-silver-dark ml-2\">© 2025</span>
      </div>
      <div class=\"text-[9px] font-mono text-silver-dark tracking-wider\">ZEMA STUDIOS · ADDIS ABABA, ETH</div>
    </div>
  </div>
</footer>
<script src=\"script.js\"></script>
</body>
</html>
"""


def cases_html():
    return page_head('CASE STUDIES — Newsletter — Niyan Ali') + nav_html('cases') + '''
<section class="relative min-h-screen overflow-hidden pt-28 pb-16">
  <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_left,_rgba(255,79,48,0.2),_transparent_22%),linear-gradient(180deg,_rgba(5,5,5,0.98),_rgba(5,5,5,0.99))]"></div>
  <div class="absolute inset-0 bg-[url('https://picsum.photos/seed/case-newsletter-hero/1600/1200.jpg')] bg-cover bg-center opacity-15"></div>
  <div class="relative max-w-7xl mx-auto px-5 h-full flex flex-col justify-center">
    <div class="max-w-3xl space-y-8">
      <div class="inline-flex items-center gap-3 text-[10px] font-bold uppercase tracking-[0.25em] text-neon-orange">
        <span class="w-10 h-[1px] bg-neon-orange block"></span>BIWEEKLY STORYLETTER
      </div>
      <h1 class="text-5xl md:text-6xl xl:text-7xl font-black tracking-tight text-white leading-tight">INSIDER CASE STUDY NOTES, DELIVERED EVERY TWO WEEKS.</h1>
      <p class="text-base md:text-lg text-silver-mid leading-relaxed">Subscribe for behind-the-scenes breakdowns on production strategy, color grading, and campaign-ready visual storytelling from every major case.</p>
      <form class="grid gap-4 sm:grid-cols-[1fr_auto] items-center">
        <input type="email" placeholder="Enter your email" required class="w-full rounded-full border border-white/10 bg-dark-900/85 px-5 py-4 text-sm text-white placeholder:text-silver-dark focus:border-neon-orange focus:ring-2 focus:ring-neon-orange/20" />
        <button type="submit" class="cta-btn bg-neon-orange text-dark-900 px-6 py-4 text-xs font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">Subscribe</button>
      </form>
      <div class="text-sm text-silver-mid uppercase tracking-[0.25em]">No spam • Delivered every two weeks • Production insights only</div>
    </div>
  </div>
</section>
<section class="py-16 border-t border-white/10">
  <div class="max-w-6xl mx-auto px-5 grid md:grid-cols-3 gap-6">
    <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-4">
      <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Featured Topic</div>
      <h2 class="text-2xl font-black text-white">Production Playbooks</h2>
      <p class="text-sm text-silver-mid leading-relaxed">Learn how craft decisions in lighting, sound, and edit flow deliver premium results.</p>
    </div>
    <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-4">
      <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">What You'll Get</div>
      <h2 class="text-2xl font-black text-white">Case Study Breakdowns</h2>
      <p class="text-sm text-silver-mid leading-relaxed">From concept to final grade: real project summaries with practical insights.</p>
    </div>
    <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-4">
      <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Why Subscribe</div>
      <h2 class="text-2xl font-black text-white">Creative Momentum</h2>
      <p class="text-sm text-silver-mid leading-relaxed">Stay inspired with new case study notes that sharpen your visual storytelling every fortnight.</p>
    </div>
  </div>
</section>
<section class="py-16">
  <div class="max-w-6xl mx-auto px-5">
    <div class="grid sm:grid-cols-2 gap-6">
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 overflow-hidden">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/case-vault-1/900/900.jpg');"></div>
        <div class="p-6 space-y-4">
          <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Case Notes</div>
          <h3 class="text-2xl font-black text-white">From shoots to screen</h3>
          <p class="text-sm text-silver-mid leading-relaxed">Stories of lighting systems, edit structure, and brand positioning crafted for broadcast and digital campaigns.</p>
        </div>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 overflow-hidden">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/case-vault-2/900/900.jpg');"></div>
        <div class="p-6 space-y-4">
          <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Creative Tools</div>
          <h3 class="text-2xl font-black text-white">LUTs, effects, and workflow</h3>
          <p class="text-sm text-silver-mid leading-relaxed">Real-world examples of how effects and grading choices support the mood of each story.</p>
        </div>
      </div>
    </div>
  </div>
</section>
''' + page_footer()


def shop_html():
    return page_head('SHOP — Niyan Ali') + nav_html('shop', True) + '''
<section class="pt-28 pb-12 border-b border-white/5 relative">
  <div class="absolute inset-0 opacity-20 bg-[radial-gradient(circle_at_top_left,_rgba(255,79,48,0.18),_transparent_20%),linear-gradient(180deg,_rgba(5,5,5,0.96),_rgba(5,5,5,0.98))]"></div>
  <div class="max-w-full mx-auto px-5">
    <div class="flex flex-col lg:flex-row lg:items-end lg:justify-between gap-6">
      <div class="space-y-4 max-w-3xl">
        <div class="inline-flex items-center gap-3 text-[10px] font-bold uppercase tracking-[0.25em] text-neon-orange"><span class="w-8 h-[1px] bg-neon-orange block"></span>Shop</div>
        <h1 class="text-5xl md:text-6xl font-black tracking-tighter text-white">ASSETS, LUTS, AND FILMMAKING KITS</h1>
        <p class="text-sm text-silver-mid leading-relaxed">Browse premium bundles, plugin-ready assets, and gear rental packages made for filmmakers.</p>
      </div>
      <div class="flex flex-wrap gap-3">
        <a href="#topBundles" class="text-xs uppercase tracking-[0.25em] text-silver-mid hover:text-white transition-colors">Top Bundles</a>
        <a href="#categories" class="text-xs uppercase tracking-[0.25em] text-silver-mid hover:text-white transition-colors">Categories</a>
        <a href="#rentals" class="text-xs uppercase tracking-[0.25em] text-silver-mid hover:text-white transition-colors">Rentals</a>
      </div>
    </div>
  </div>
</section>
<section id="topBundles" class="py-16 bg-dark-900/40 border-t border-white/10">
  <div class="max-w-full mx-auto px-5">
    <div class="flex items-center justify-between gap-4 mb-8">
      <div>
        <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Top Bundles</div>
        <h2 class="text-4xl font-black text-white">Editor's Picks</h2>
      </div>
      <div class="text-sm text-silver-mid">1x1 thumbnails for instant product focus.</div>
    </div>
    <div class="grid sm:grid-cols-3 gap-6">
      <article class="group overflow-hidden rounded-3xl border border-white/10 bg-dark-700/40">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/bundle-thumb-1/800/800.jpg');"></div>
        <div class="p-6 space-y-4">
          <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Bundle</div>
          <h3 class="text-2xl font-black text-white">Cinematic LUT Suite</h3>
          <p class="text-sm text-silver-mid leading-relaxed">30 premium LUTs and film grain overlays for polished look development.</p>
          <div class="flex items-center justify-between gap-4">
            <span class="text-3xl font-black text-neon-orange">$49</span>
            <a href="effects-lut-packs.html" class="cta-btn bg-neon-orange text-dark-900 px-4 py-2 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">View</a>
          </div>
        </div>
      </article>
      <article class="group overflow-hidden rounded-3xl border border-white/10 bg-dark-700/40">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/bundle-thumb-2/800/800.jpg');"></div>
        <div class="p-6 space-y-4">
          <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Assets</div>
          <h3 class="text-2xl font-black text-white">Visual Asset Kit</h3>
          <p class="text-sm text-silver-mid leading-relaxed">120 motion graphics, titles, and transitions for fast editing.</p>
          <div class="flex items-center justify-between gap-4">
            <span class="text-3xl font-black text-neon-orange">$69</span>
            <a href="visual-assets-plugins.html" class="cta-btn bg-neon-orange text-dark-900 px-4 py-2 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">View</a>
          </div>
        </div>
      </article>
      <article class="group overflow-hidden rounded-3xl border border-white/10 bg-dark-700/40">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/bundle-thumb-3/800/800.jpg');"></div>
        <div class="p-6 space-y-4">
          <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Rental</div>
          <h3 class="text-2xl font-black text-white">Filmmaker Kit Rental</h3>
          <p class="text-sm text-silver-mid leading-relaxed">Sony FX6 rig with lenses, gimbal, and pro audio – ready for production.</p>
          <div class="flex items-center justify-between gap-4">
            <span class="text-3xl font-black text-neon-orange">$120/day</span>
            <a href="#rentals" class="cta-btn bg-neon-orange text-dark-900 px-4 py-2 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">Book</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>
<section id="categories" class="py-16 border-t border-white/10">
  <div class="max-w-full mx-auto px-5">
    <div class="grid lg:grid-cols-3 gap-6">
      <a href="effects-lut-packs.html" class="group rounded-3xl border border-white/10 bg-dark-700/40 p-8 hover:border-neon-orange/40 transition-all">
        <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Effects & LUT Packs</div>
        <h2 class="text-3xl font-black text-white mt-4">Effects & LUT Packs</h2>
        <p class="text-sm text-silver-mid mt-3">Color workflows, stylized looks, and cinematic filters for fast grading.</p>
        <div class="mt-8 inline-flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-neon-orange">Open Library <i data-lucide="arrow-right" class="w-4 h-4"></i></div>
      </a>
      <a href="visual-assets-plugins.html" class="group rounded-3xl border border-white/10 bg-dark-700/40 p-8 hover:border-neon-orange/40 transition-all">
        <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Visual Assets & Plugins</div>
        <h2 class="text-3xl font-black text-white mt-4">Visual Assets & Plugins</h2>
        <p class="text-sm text-silver-mid mt-3">Editable packs with Premiere, After Effects, and Resolve support.</p>
        <div class="mt-8 inline-flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-neon-orange">Open Library <i data-lucide="arrow-right" class="w-4 h-4"></i></div>
      </a>
      <a href="#rentals" class="group rounded-3xl border border-white/10 bg-dark-700/40 p-8 hover:border-neon-orange/40 transition-all">
        <div class="text-[10px] uppercase tracking-[0.25em] text-neon-orange">Filmmaking Kit Rentals</div>
        <h2 class="text-3xl font-black text-white mt-4">Rentals</h2>
        <p class="text-sm text-silver-mid mt-3">Gear listings, availability, and booking dates for production-ready kits.</p>
        <div class="mt-8 inline-flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-neon-orange">Browse Rentals <i data-lucide="arrow-right" class="w-4 h-4"></i></div>
      </a>
    </div>
  </div>
</section>
<section id="rentals" class="py-16 border-t border-white/10">
  <div class="max-w-full mx-auto px-5">
    <div class="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 mb-8">
      <div>
        <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Rentals</div>
        <h2 class="text-4xl font-black text-white mt-3">Gear Availability & Booking</h2>
      </div>
      <div class="rounded-full border border-white/10 bg-dark-800/70 px-5 py-3 text-sm text-silver-mid">Stock updated hourly from Addis Ababa</div>
    </div>
    <div class="space-y-4">
      <div class="grid md:grid-cols-12 gap-4 items-center rounded-3xl border border-white/10 bg-dark-700/40 p-5">
        <div class="md:col-span-5 text-white font-bold">Sony FX6 Kit</div>
        <div class="md:col-span-3 text-silver-mid text-sm">Available</div>
        <div class="md:col-span-2 text-neon-orange font-bold">$120/day</div>
        <div class="md:col-span-2 text-[11px] text-silver-dark">Book from 27 Jul</div>
      </div>
      <div class="grid md:grid-cols-12 gap-4 items-center rounded-3xl border border-white/10 bg-dark-700/40 p-5">
        <div class="md:col-span-5 text-white font-bold">RED Komodo 6K + Lens Set</div>
        <div class="md:col-span-3 text-silver-mid text-sm">Available</div>
        <div class="md:col-span-2 text-neon-orange font-bold">$220/day</div>
        <div class="md:col-span-2 text-[11px] text-silver-dark">Book from 01 Aug</div>
      </div>
      <div class="grid md:grid-cols-12 gap-4 items-center rounded-3xl border border-white/10 bg-dark-700/40 p-5">
        <div class="md:col-span-5 text-white font-bold">DJI RS 3 Pro + Gimbal</div>
        <div class="md:col-span-3 text-silver-mid text-sm">Limited</div>
        <div class="md:col-span-2 text-neon-orange font-bold">$80/day</div>
        <div class="md:col-span-2 text-[11px] text-silver-dark">Book from 29 Jul</div>
      </div>
      <div class="grid md:grid-cols-12 gap-4 items-center rounded-3xl border border-white/10 bg-dark-700/40 p-5">
        <div class="md:col-span-5 text-white font-bold">Zeiss CP.3 Lens Set</div>
        <div class="md:col-span-3 text-silver-mid text-sm">Available</div>
        <div class="md:col-span-2 text-neon-orange font-bold">$140/day</div>
        <div class="md:col-span-2 text-[11px] text-silver-dark">Book from 30 Jul</div>
      </div>
    </div>
  </div>
</section>
<section id="rates" class="py-16 border-t border-white/10 bg-dark-900/80">
  <div class="max-w-full mx-auto px-5">
    <div class="text-center mb-10">
      <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Package Hire Rate</div>
      <h2 class="text-4xl font-black text-white mt-4">Daily, Campaign, and Contract Rates</h2>
      <p class="text-silver-mid max-w-2xl mx-auto mt-4">Flexible rates for production, campaign, and extended contract bookings.</p>
    </div>
    <div class="grid lg:grid-cols-3 gap-6">
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-5">
        <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Daily</div>
        <div class="text-5xl font-black text-white">$350</div>
        <p class="text-silver-mid leading-relaxed">Single-day production coverage with camera, lighting, and sound support.</p>
        <ul class="space-y-2 text-sm text-silver-mid">
          <li>• Camera + kit</li>
          <li>• Lighting setup</li>
          <li>• Sound capture</li>
          <li>• Quick delivery</li>
        </ul>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-5">
        <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Campaign</div>
        <div class="text-5xl font-black text-white">$1,250</div>
        <p class="text-silver-mid leading-relaxed">Multi-day campaign work with creative direction and edit-ready deliverables.</p>
        <ul class="space-y-2 text-sm text-silver-mid">
          <li>• Pre-production planning</li>
          <li>• Storyboarding</li>
          <li>• Camera + rig support</li>
          <li>• Editing package</li>
        </ul>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-8 space-y-5">
        <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">Contract</div>
        <div class="text-5xl font-black text-white">$3,900</div>
        <p class="text-silver-mid leading-relaxed">Weekly contract support for ongoing content, episodic shoots, and brand storytelling.</p>
        <ul class="space-y-2 text-sm text-silver-mid">
          <li>• Dedicated production team</li>
          <li>• Weekly asset delivery</li>
          <li>• Creative direction</li>
          <li>• Production management</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section id="faq" class="py-16 border-t border-white/10">
  <div class="max-w-5xl mx-auto px-5">
    <div class="text-center mb-10">
      <div class="text-[10px] uppercase tracking-[0.3em] text-neon-orange">FAQ</div>
      <h2 class="text-4xl font-black text-white mt-4">Frequently Asked Questions</h2>
    </div>
    <div class="space-y-4">
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-6">
        <h3 class="text-lg font-bold text-white">How do I book rental gear?</h3>
        <p class="text-silver-mid mt-3">Choose the package, note the booking date, and contact me to confirm the rental. Availability updates hourly.</p>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-6">
        <h3 class="text-lg font-bold text-white">Can I use assets in Premiere, After Effects, and Resolve?</h3>
        <p class="text-silver-mid mt-3">Yes. The Visual Assets page includes support for Premiere Pro, After Effects, and DaVinci Resolve files.</p>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-6">
        <h3 class="text-lg font-bold text-white">Do you offer custom bundle packages?</h3>
        <p class="text-silver-mid mt-3">Yes. Contact me for a custom bundle built around your filmmaking style and project needs.</p>
      </div>
      <div class="rounded-3xl border border-white/10 bg-dark-700/40 p-6">
        <h3 class="text-lg font-bold text-white">How often are new case notes sent?</h3>
        <p class="text-silver-mid mt-3">Every two weeks. Each issue includes new case study insights from recent productions.</p>
      </div>
    </div>
  </div>
</section>
''' + page_footer()


def effects_card(idx):
    return f'''      <article class="rounded-3xl border border-white/10 bg-dark-700/40 overflow-hidden">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/lut-{idx}/600/600.jpg');"></div>
        <div class="p-5 space-y-3">
          <div class="text-[9px] uppercase tracking-[0.2em] text-neon-orange">LUT Pack</div>
          <h3 class="text-sm font-bold text-white">Cinematic LUT Pack {idx}</h3>
          <p class="text-[11px] text-silver-mid leading-relaxed">Color grading presets for cinematic looks and mood shifts.</p>
          <div class="flex items-center justify-between gap-3">
            <span class="text-sm font-bold text-neon-orange">$19</span>
            <button class="cta-btn bg-white/5 text-white px-3 py-2 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">Add to Cart</button>
          </div>
        </div>
      </article>'''


def effects_page(page, start):
    cards = ''.join(effects_card(i) for i in range(start, start + 25))
    heading = 'Effects & LUT Packs' if page == 1 else 'More LUT & FX Packages'
    desc = 'Explore cinematic LUT packages with premium looks, film grain, and color grading tools.' if page == 1 else 'Continue browsing LUTs, presets, and creative FX for faster edit workflows.'
    pager = 'effects-lut-packs-2.html' if page == 1 else 'effects-lut-packs.html'
    btn = 'Next Page' if page == 1 else 'Previous Page'
    return page_head(f'Effects & LUT Packs — Page {page} — Niyan Ali') + nav_html('shop') + f'''
<section class="pt-28 pb-12 border-b border-white/5 relative">
  <div class="absolute inset-0 opacity-15 bg-[radial-gradient(circle_at_top_left,_rgba(255,79,48,0.16),_transparent_20%),linear-gradient(180deg,_rgba(5,5,5,0.96),_rgba(5,5,5,0.99))]"></div>
  <div class="max-w-full mx-auto px-5">
    <div class="space-y-4 max-w-4xl">
      <div class="inline-flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-neon-orange"><span class="w-8 h-[1px] bg-neon-orange block"></span>Effects & LUT Packs</div>
      <h1 class="text-5xl md:text-6xl font-black text-white">{heading}</h1>
      <p class="text-sm text-silver-mid leading-relaxed">{desc}</p>
    </div>
  </div>
</section>
<section class="py-12">
  <div class="max-w-full mx-auto px-5">
    <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-5 gap-4">
{cards}
    </div>
  </div>
</section>
<section class="py-12 border-t border-white/10">
  <div class="max-w-full mx-auto px-5 flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
    <a href="shop.html" class="inline-flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-neon-orange hover:text-white transition-colors"><i data-lucide="arrow-left" class="w-4 h-4"></i> Back to Shop</a>
    <a href="{pager}" class="cta-btn bg-neon-orange text-dark-900 px-6 py-3 text-xs font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">{btn}</a>
  </div>
</section>
''' + page_footer()


def visual_card(idx):
    tools = ' '.join(
        f'<span class="inline-flex items-center gap-1 rounded-full border border-white/10 bg-white/5 px-2 py-1 text-[10px] text-silver-mid">{tool}</span>'
        for tool in ['Premiere Pro', 'After Effects', 'Resolve']
    )
    return f'''      <article class="rounded-3xl border border-white/10 bg-dark-700/40 overflow-hidden">
        <div class="aspect-square bg-cover bg-center" style="background-image:url('https://picsum.photos/seed/asset-{idx}/600/600.jpg');"></div>
        <div class="p-5 space-y-3">
          <div class="text-[9px] uppercase tracking-[0.2em] text-neon-orange">Asset Pack</div>
          <h3 class="text-sm font-bold text-white">Visual Asset Bundle {idx}</h3>
          <p class="text-[11px] text-silver-mid leading-relaxed">Ready-to-use assets for fast creative editing.</p>
          <div class="flex flex-wrap gap-2">{tools}</div>
          <div class="flex items-center justify-between gap-3">
            <span class="text-sm font-bold text-neon-orange">$29</span>
            <button class="cta-btn bg-white/5 text-white px-3 py-2 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">Add to Cart</button>
          </div>
        </div>
      </article>'''


def visual_page():
    cards = ''.join(visual_card(i) for i in range(1, 13))
    return page_head('Visual Assets & Plugins — Niyan Ali') + nav_html('shop') + f'''
<section class="pt-28 pb-12 border-b border-white/5 relative">
  <div class="absolute inset-0 opacity-15 bg-[radial-gradient(circle_at_top_left,_rgba(255,79,48,0.16),_transparent_20%),linear-gradient(180deg,_rgba(5,5,5,0.96),_rgba(5,5,5,0.99))]"></div>
  <div class="max-w-full mx-auto px-5">
    <div class="space-y-4 max-w-4xl">
      <div class="inline-flex items-center gap-3 text-[10px] uppercase tracking-[0.25em] text-neon-orange"><span class="w-8 h-[1px] bg-neon-orange block"></span>Visual Assets & Plugins</div>
      <h1 class="text-5xl md:text-6xl font-black text-white">Assets for Premiere, After Effects & Resolve</h1>
      <p class="text-sm text-silver-mid leading-relaxed">Browse plugin-ready assets, motion templates, and editing kits for fast production.</p>
    </div>
  </div>
</section>
<section class="py-12">
  <div class="max-w-full mx-auto px-5">
    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-4">
{cards}
    </div>
  </div>
</section>
<section class="py-12 border-t border-white/10">
  <div class="max-w-full mx-auto px-5 flex flex-col sm:flex-row sm:justify-between sm:items-center gap-4">
    <a href="shop.html" class="inline-flex items-center gap-2 text-xs uppercase tracking-[0.25em] text-neon-orange hover:text-white transition-colors"><i data-lucide="arrow-left" class="w-4 h-4"></i> Back to Shop</a>
    <a href="contact.html" class="cta-btn bg-neon-orange text-dark-900 px-6 py-3 text-xs font-bold uppercase tracking-[0.2em] hover:bg-neon-orangeHover">Need Custom Assets?</a>
  </div>
</section>
''' + page_footer()


def write_file(path: Path, content: str):
    path.write_text(content, encoding='utf-8')


if __name__ == '__main__':
    write_file(root / 'cases.html', cases_html())
    write_file(root / 'shop.html', shop_html())
    write_file(root / 'effects-lut-packs.html', effects_page(1, 1))
    write_file(root / 'effects-lut-packs-2.html', effects_page(2, 26))
    write_file(root / 'visual-assets-plugins.html', visual_page())

    files = sorted(root.glob('*.html'))
    for path in files:
        content = path.read_text(encoding='utf-8')
        nav_match = re.search(r'<!-- NAVIGATION -->.*?</nav>', content, flags=re.S)
        if not nav_match:
            nav_match = re.search(r'<nav\b.*?</nav>', content, flags=re.S)
        if not nav_match:
            print(f'skip {path.name}: nav not found')
            continue
        fn = path.name
        if fn == 'about.html':
            active = 'about.html'
        elif fn == 'cases.html':
            active = 'cases.html'
        elif fn == 'shop.html':
            active = 'shop.html'
        elif fn in ['effects-lut-packs.html', 'effects-lut-packs-2.html', 'visual-assets-plugins.html']:
            active = 'shop.html'
        elif fn == 'contact.html':
            active = 'contact.html'
        else:
            active = 'work.html'
        new_nav = nav_html(active, fn == 'shop.html')
        write_file(path, content[:nav_match.start()] + new_nav + content[nav_match.end():])
    print('done')
