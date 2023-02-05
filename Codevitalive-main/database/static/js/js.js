/* scroll menu  */

window.addEventListener('scroll', function () {
  var header = document.querySelector('.header');
  header.classList.toggle("sticky", window.scrollY > 0);
})



$('nav').affix({
  offset: {
    top: $('#services').offset().top
  }
});


/*popup*/