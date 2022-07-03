

const navBtn = document.querySelector('#menu');
const menuBar = document.querySelector('#menubar');

navBtn.addEventListener('click', () => {
    const isExtended = JSON.parse(navBtn.getAttribute
        ('aria-expanded'));
        navBtn.setAttribute('aria-expanded', !isExtended);
        menuBar.classList.toggle('hidden');
        menuBar.classList.toggle('flex');
})