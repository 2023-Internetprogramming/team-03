const plusButton = document.getElementById('plus');
const footer = document.getElementById('footer');

function handleScroll() {
    const footerRect = footer.getBoundingClientRect();
    if (footerRect.top < window.innerHeight) {
        plusButton.style.display = 'none';
    } else {
        plusButton.style.display = 'block';
    }
}

function redirectToNewPage() {
    window.location.href = window.location.href + 'new/';
}

window.addEventListener('scroll', handleScroll);