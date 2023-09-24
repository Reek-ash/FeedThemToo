// Disable right-click inspect
// document.addEventListener('contextmenu', function(event) {
//     event.preventDefault();
//   });

const testimonials = document.querySelectorAll('.testimonials__block');

testimonials.forEach((testimonial) => {
  testimonial.addEventListener('mouseenter', () => {
    testimonials.forEach((t) => {
      if (t !== testimonial) {
        t.style.transform = 'translateY(10px)';
      }
    });
  });

  testimonial.addEventListener('mouseleave', () => {
    testimonials.forEach((t) => {
      if (t !== testimonial) {
        t.style.transform = 'translateY(0)';
      }
    });
  });
});



