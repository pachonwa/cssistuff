let boxes = document.querySelectorAll('div')

boxes.forEach(box => {
  box.addEventListener('mouseenter', e => {
    box.classList.add('spin');
  });

  box.addEventListener('mouseleave', e => {
    box.classList.remove('spin');
  });
});

window.addEventListener('keydown', e => {
  if (e.key == 'g' || e.key == 'G') {
    boxes.forEach(box => {
      box.classList.remove('red', 'blue');
      box.classList.add('green');
    });
  }


if (e.key == 'b' || e.key == 'B') {
  boxes.forEach(box => {
    box.classList.remove('red', 'green');
    box.classList.add('blue');
  });
}
});
