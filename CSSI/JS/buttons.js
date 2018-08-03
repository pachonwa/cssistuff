console.log('Hello');
let likeButton = document.querySelector('#like');
console.log(likeButton);
likeButton.addEventListener('click', e =>{
  likeButton.innerText = 'Liked';
  likeButton.disabled = true;
});

let growButton = document.querySelector('#grow');
growButton.addEventListener('click', e => {
  console.log('Click');
  let currentSize = growButton.style.fontSize;
  let newSize = parseInt(currentSize) + 10;
  console.log(newSize);
  growButton.style.fontSize = newSize + 'px';
})
