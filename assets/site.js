// Waldre Roos · royalenite.github.io. Everything here is optional: without script the page reads in full.
const EMAIL = 'hello@waldre.co.za';
const mailto = (subject, body) =>
  `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

// Reveal once as each part enters the viewport.
(() => {
  const els = document.querySelectorAll('[data-reveal], .band');
  if (!('IntersectionObserver' in window)) { els.forEach((el) => el.classList.add('is-in')); return; }
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
  els.forEach((el) => io.observe(el));
  addEventListener('load', () => setTimeout(() => els.forEach((el) => {
    const r = el.getBoundingClientRect(); if (r.top < innerHeight && r.bottom > 0) el.classList.add('is-in');
  }), 2500));
})();

// Work index: hovering or focusing a name shows its picture in the frame.
(() => {
  const names = [...document.querySelectorAll('.work .names a')];
  const frames = [...document.querySelectorAll('.work .frame > *')];
  if (!names.length) return;
  const show = (i) => {
    names.forEach((a, j) => a.classList.toggle('on', i === j));
    frames.forEach((f, j) => f.classList.toggle('on', i === j));
  };
  names.forEach((a, i) => { a.addEventListener('mouseenter', () => show(i)); a.addEventListener('focus', () => show(i)); });
  show(0);
})();

// "What runs your business today?": pick one, read what replaces it, email with it filled in.
(() => {
  const box = document.querySelector('.now');
  if (!box) return;
  const buttons = [...box.querySelectorAll('.choice')];
  const panels = [...box.querySelectorAll('.panel')];
  const pick = (key) => {
    buttons.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.key === key)));
    panels.forEach((p) => { p.hidden = p.dataset.key !== key; });
  };
  buttons.forEach((b) => b.addEventListener('click', () => pick(b.dataset.key)));
  panels.forEach((p) => {
    const a = p.querySelector('a.button');
    if (a) a.href = mailto(p.dataset.subject, p.dataset.body);
  });
  pick(buttons[0].dataset.key);
})();

// Contact: one field that opens an email with the message in it.
(() => {
  document.querySelectorAll('form[data-mail]').forEach((form) => {
    form.addEventListener('submit', (ev) => {
      ev.preventDefault();
      const text = form.querySelector('textarea').value.trim();
      location.href = mailto('A project', text || 'Hi Waldre,\n\n');
    });
  });
})();

// The one moving picture: no autoplay for people who asked for less motion.
(() => {
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('video[autoplay]').forEach((v) => { v.removeAttribute('autoplay'); v.pause(); v.controls = true; });
})();
