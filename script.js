// Import required libraries
import { Modal } from 'bootstrap';
import { JSDOM } from 'jsdom';

// Responsive nav toggle
const toggleBtn = document.querySelector('.toggle-btn');
const navLinks = document.querySelector('.nav-links');
const navItems = document.querySelectorAll('.nav-links li a');

// Event delegation for nav toggle
toggleBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
});

// Active link highlighting
const activeLinkHighlight = () => {
    const fromTop = window.scrollY + 85;
    navItems.forEach(link => {
        const section = document.querySelector(link.hash);
        if (
            section &&
            section.offsetTop <= fromTop &&
            section.offsetTop + section.offsetHeight > fromTop
        ) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
};
window.addEventListener('scroll', activeLinkHighlight);

// Scroll-to-top button
const scrollTopBtn = document.getElementById('scrollTopBtn');
const isScrollTopBtnVisible = () => {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        scrollTopBtn.style.display = 'block';
    } else {
        scrollTopBtn.style.display = 'none';
    }
};
window.addEventListener('scroll', isScrollTopBtnVisible);
scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

// Contact form simulation
const contactForm = document.getElementById('contactForm');
const contactFormSubmit = () => {
    const modal = new Modal(document.getElementById('contactFormModal'));
    modal.show();
    contactForm.reset();
};
contactForm.addEventListener('submit', contactFormSubmit);

// Reveal sections on scroll (animation)
const revealElements = document.querySelectorAll('.reveal');
const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;
    revealElements.forEach(el => {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                el.classList.add('reveal');
            }
        }, { threshold: 0.85 });
        observer.observe(el);
    });
};
document.addEventListener('scroll', revealOnScroll);
window.addEventListener('DOMContentLoaded', () => {
    revealOnScroll();
});

// Optional: Dynamic background palette (eye comfort)
const dynamicBackgroundPalette = [
    ['#fff8f0', '#e6ded5'], // morning
    ['#fff4e6', '#f9ebdd'], // afternoon
    ['#e7e6e1', '#dacec1'] // evening
];
const dynamicBackground = () => {
    if (!dynamicBackgroundPalette || dynamicBackgroundPalette.length === 0) {
        return;
    }
    const hour = new Date().getHours();
    let colors;
    if (hour >= 6 && hour < 12) {
        colors = dynamicBackgroundPalette[0];
    } else if (hour >= 12 && hour < 18) {
        colors = dynamicBackgroundPalette[1];
    } else {
        colors = dynamicBackgroundPalette[2];
    }
    document.body.style.background = `linear-gradient(120deg, ${colors[0]} 0%, ${colors[1]} 100%)`;
};
window.onload = dynamicBackground;

// Named constant for reveal trigger bottom
const REVEAL_TRIGGER_BOTTOM = 0.85;

// Clean up IntersectionObserver when element is removed from DOM
const observers = new WeakMap();
revealElements.forEach(el => {
    const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
            el.classList.add('reveal');
        }
    }, { threshold: 0.85 });
    observers.set(el, observer);
    observer.observe(el);
});
document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') {
        revealElements.forEach(el => {
            const observer = observers.get(el);
            observer.unobserve(el);
        });
    } else {
        revealElements.forEach(el => {
            const observer = observers.get(el);
            observer.observe(el);
        });
    }
});

// Display alerts using a modal dialog
const displayAlert = (message) => {
    const modal = new Modal(document.getElementById('alertModal'));
    modal.setContent(message);
    modal.show();
};