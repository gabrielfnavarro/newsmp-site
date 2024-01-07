let sections = document.querySelectorAll('section');
console.log('foi')
window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;

        if(top >= offset && top < offset + height) {
            sec.classList.add('show-animate');
            sec.style.opacity = 1;
        }

        else {
            sec.classList.remove('show-animate')
            sec.style.opacity = 0;
        }
    })
}