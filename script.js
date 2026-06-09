// Import required libraries
import { Modal } from 'bootstrap';
import { JSDOM } from 'jsdom';

// Responsive nav toggle
const toggleNav = () => {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('active');
};

// Active link highlighting
const activeLinkHighlight = () => {
    const fromTop = window.scrollY + 85;
    const navItems = document.querySelectorAll('.nav-links li a');
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

// Scroll-to-top button
const isScrollTopBtnVisible = () => {
    if (window.scrollY > 200) {
        const scrollTopBtn = document.getElementById('scrollTopBtn');
        scrollTopBtn.style.display = 'block';
    } else {
        const scrollTopBtn = document.getElementById('scrollTopBtn');
        scrollTopBtn.style.display = 'none';
    }
};

// Contact form simulation
const contactFormSubmit = () => {
    const modal = new Modal(document.getElementById('contactFormModal'));
    modal.show();
    const contactForm = document.getElementById('contactForm');
    contactForm.reset();
};

// Reveal sections on scroll (animation)
const revealOnScroll = () => {
    const triggerBottom = window.innerHeight * 0.85;
    const revealElements = document.querySelectorAll('.reveal');
    revealElements.forEach(el => {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                el.classList.add('reveal');
            }
        }, { threshold: 0.85 });
        observer.observe(el);
    });
};

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

// Named constant for reveal trigger bottom
const REVEAL_TRIGGER_BOTTOM = 0.85;

// Clean up IntersectionObserver when element is removed from DOM
const observers = new WeakMap();
const cleanupObservers = () => {
    revealElements.forEach(el => {
        const observer = observers.get(el);
        observer.unobserve(el);
    });
};

// Display alerts using a modal dialog
const displayAlert = (message) => {
    const modal = new Modal(document.getElementById('alertModal'));
    modal.setContent(message);
    modal.show();
};

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('.toggle-btn').addEventListener('click', toggleNav);
    window.addEventListener('scroll', () => {
        activeLinkHighlight();
        isScrollTopBtnVisible();
        revealOnScroll();
    });
    document.addEventListener('visibilitychange', () => {
        if (document.visibilityState === 'hidden') {
            cleanupObservers();
        } else {
            revealOnScroll();
        }
    });
    document.getElementById('scrollTopBtn').addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
    document.getElementById('contactForm').addEventListener('submit', contactFormSubmit);
    window.addEventListener('load', dynamicBackground);