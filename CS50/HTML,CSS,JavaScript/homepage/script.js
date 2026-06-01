// JavaScript functionality for interactivity

// Welcome button alert
document.addEventListener('DOMContentLoaded', function() {
    const welcomeBtn = document.getElementById('welcomeBtn');
    if (welcomeBtn) {
        welcomeBtn.addEventListener('click', function() {
            alert('Welcome to TechInnovate! Let\'s transform your business with technology.');
        });
    }

    // Counter animation on home page
    function startCounters() {
        const counters = document.querySelectorAll('.counter');
        if (counters.length > 0) {
            const targets = [247, 189, 15, 42];
            counters.forEach((counter, index) => {
                let current = 0;
                const target = targets[index];
                const increment = target / 50;
                const updateCounter = setInterval(() => {
                    if (current < target) {
                        current += increment;
                        counter.innerText = Math.floor(current);
                    } else {
                        counter.innerText = target;
                        clearInterval(updateCounter);
                    }
                }, 30);
            });
        }
    }
    startCounters();

    // Service buttons alert
    const serviceBtns = document.querySelectorAll('.service-btn');
    serviceBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const service = this.getAttribute('data-service');
            alert(`Thank you for your interest in ${service}! A specialist will contact you within 24 hours.`);
        });
    });

    // Portfolio items click effect
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    portfolioItems.forEach(item => {
        item.addEventListener('click', function() {
            const projectName = this.querySelector('h4').innerText;
            alert(`📁 Project: ${projectName}\n\nThis project showcases our expertise in delivering innovative solutions. Contact us for similar success!`);
        });
    });

    // Contact form handling
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (name && email && message) {
                const feedback = document.getElementById('formFeedback');
                feedback.innerHTML = '<div class="alert alert-success">✓ Message sent successfully! We\'ll respond within 24 hours.</div>';
                contactForm.reset();
                setTimeout(() => {
                    feedback.innerHTML = '';
                }, 5000);
            } else {
                alert('Please fill in all fields before submitting.');
            }
        });
    }

    // Clear form button
    const clearBtn = document.getElementById('clearFormBtn');
    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            const form = document.getElementById('contactForm');
            if (form) form.reset();
            const feedback = document.getElementById('formFeedback');
            if (feedback) feedback.innerHTML = '';
        });
    }

    // Map modal
    const showMapBtn = document.getElementById('showMapBtn');
    if (showMapBtn) {
        showMapBtn.addEventListener('click', function() {
            $('#mapModal').modal('show');
        });
    }

    // Dynamic time-based greeting
    const timeAlert = document.getElementById('timeAlert');
    if (timeAlert) {
        const hour = new Date().getHours();
        let greeting = '';
        if (hour < 12) greeting = 'Good morning! ☀️';
        else if (hour < 18) greeting = 'Good afternoon!';
        else greeting = 'Good evening! 🌙';

        timeAlert.innerHTML = `<strong>${greeting}</strong><br>Our team is ready to assist you during office hours: Mon-Fri, 9AM-6PM`;
    }
});
