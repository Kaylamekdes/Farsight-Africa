(function () {
  'use strict';

  /* Mobile menu */
  var btn = document.querySelector('.menu-btn');
  var menu = document.getElementById('mobile-menu');
  function setMenu(open) {
    btn.setAttribute('aria-expanded', String(open));
    btn.querySelector('.menu-label').textContent = open ? 'Close' : 'Menu';
    menu.hidden = !open;
    if (open) { var first = menu.querySelector('a'); if (first) first.focus(); }
  }
  if (btn && menu) {
    btn.addEventListener('click', function () { setMenu(menu.hidden); });
    menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && !menu.hidden) { setMenu(false); btn.focus(); }
    });
  }

  /* Desktop dropdowns (disclosure pattern) */
  var toggles = document.querySelectorAll('.nav-toggle');
  function closeAll(except) {
    toggles.forEach(function (t) {
      if (t !== except) { t.setAttribute('aria-expanded', 'false'); document.getElementById(t.getAttribute('aria-controls')).hidden = true; }
    });
  }
  toggles.forEach(function (t) {
    var sub = document.getElementById(t.getAttribute('aria-controls'));
    t.addEventListener('click', function () {
      var open = t.getAttribute('aria-expanded') !== 'true';
      closeAll(t);
      t.setAttribute('aria-expanded', String(open));
      sub.hidden = !open;
    });
    sub.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { t.setAttribute('aria-expanded', 'false'); sub.hidden = true; t.focus(); }
    });
    t.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { t.setAttribute('aria-expanded', 'false'); sub.hidden = true; }
    });
  });
  document.addEventListener('click', function (e) { if (!e.target.closest('.has-sub')) closeAll(); });
  document.addEventListener('focusin', function (e) { if (!e.target.closest('.has-sub')) closeAll(); });

  /* Highlight the current section in a service page's contents list */
  var tocLinks = document.querySelectorAll('.toc a');
  if (tocLinks.length && 'IntersectionObserver' in window) {
    var map = {};
    tocLinks.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
    var tio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) {
          tocLinks.forEach(function (a) { a.classList.remove('is-current'); a.removeAttribute('aria-current'); });
          var a = map[en.target.id]; if (a) { a.classList.add('is-current'); a.setAttribute('aria-current', 'true'); }
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    document.querySelectorAll('.svc-section').forEach(function (s) { tio.observe(s); });
  }

  /* Subtle reveal on scroll */
  var items = document.querySelectorAll('.reveal');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!('IntersectionObserver' in window) || reduce) {
    items.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    items.forEach(function (el) { io.observe(el); });
  }

  /* Enquiry form: validation + mailto fallback (no backend in this concept) */
  var form = document.getElementById('enquiry');
  if (!form) return;
  var status = document.getElementById('form-status');
  var rules = {
    'f-name': ['e-name', function (v) { return v ? '' : 'Please enter your name.'; }],
    'f-org': ['e-org', function (v) { return v ? '' : 'Please enter your organisation.'; }],
    'f-email': ['e-email', function (v) {
      if (!v) return 'Please enter your email address.';
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) ? '' : 'Please enter a valid email address, like name@example.org.';
    }],
    'f-area': ['e-area', function (v) { return v ? '' : 'Please choose an area of interest.'; }],
    'f-msg': ['e-msg', function (v) { return v.length >= 10 ? '' : 'Please write a short message (at least 10 characters).'; }]
  };
  function check(id) {
    var el = document.getElementById(id);
    var msg = rules[id][1](el.value.trim());
    document.getElementById(rules[id][0]).textContent = msg;
    el.setAttribute('aria-invalid', msg ? 'true' : 'false');
    return !msg;
  }
  Object.keys(rules).forEach(function (id) {
    document.getElementById(id).addEventListener('blur', function () {
      if (this.value.trim() || this.getAttribute('aria-invalid') === 'true') check(id);
    });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstBad = null;
    Object.keys(rules).forEach(function (id) { if (!check(id) && !firstBad) firstBad = id; });
    if (firstBad) {
      status.hidden = false;
      status.className = 'form-status is-error';
      status.textContent = 'Please fix the highlighted fields.';
      document.getElementById(firstBad).focus();
      return;
    }
    var v = function (id) { return document.getElementById(id).value.trim(); };
    var subject = 'Enquiry: ' + v('f-area') + ' (' + v('f-org') + ')';
    var body = 'Name: ' + v('f-name') + '\nOrganisation: ' + v('f-org') + '\nEmail: ' + v('f-email') +
      '\nArea of interest: ' + v('f-area') + '\n\n' + v('f-msg');
    window.location.href = 'mailto:info@farsightafrica.com?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(body);
    status.hidden = false;
    status.className = 'form-status';
    status.textContent = 'Your email app should now open with this message filled in. It has not been sent yet: press send there to deliver it to info@farsightafrica.com. If nothing opened, email us directly at info@farsightafrica.com.';
    status.focus();
  });
})();
