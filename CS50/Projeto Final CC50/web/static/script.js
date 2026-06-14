// Atualizar dashboard em tempo real
function updateDashboard() {
    fetch('/api/web/dashboard-stats')
        .then(response => response.json())
        .then(data => {
            const pendingEl = document.getElementById('pending-count');
            const completedTodayEl = document.getElementById('completed-today');
            const dueReviewEl = document.getElementById('due-review');
            
            if (pendingEl) pendingEl.textContent = data.pending;
            if (completedTodayEl) completedTodayEl.textContent = data.completed_today;
            if (dueReviewEl) dueReviewEl.textContent = data.due_review;
        })
        .catch(error => console.error('Erro ao atualizar dashboard:', error));
}

// Atualizar a cada 10 segundos
if (window.location.pathname === '/' || window.location.pathname === '/index') {
    updateDashboard();
    setInterval(updateDashboard, 10000);
}

// Adicionar efeito ripple aos cards
document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('click', function(e) {
        const ripple = document.createElement('div');
        ripple.className = 'ripple';
        ripple.style.left = e.clientX - this.offsetLeft + 'px';
        ripple.style.top = e.clientY - this.offsetTop + 'px';
        this.appendChild(ripple);
        setTimeout(() => ripple.remove(), 600);
    });
});

// CSS para o efeito ripple
const style = document.createElement('style');
style.textContent = `
    .feature-card {
        position: relative;
        overflow: hidden;
    }
    
    .ripple {
        position: absolute;
        width: 100px;
        height: 100px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 50%;
        transform: scale(0);
        animation: ripple-animation 0.6s ease-out;
        pointer-events: none;
    }
    
    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
