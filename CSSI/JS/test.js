console.log('Hello');

let name = "Sharon";
let daysLeft = 4;

console.log('Hello, ' + name);
console.log('There are '+ daysLeft + ' days left in CSSI');

if (daysLeft < 6 && name == "Matthew") {
  console.log('Remember to help with final projects');
}
//this is a comment


if (name == "Ciara" || name == "Matthew" || name == "Rachel") {
  console.log('You are an instructor.');
} else if (name == "Logan" || name == "Sharon" || name == "Stephanie") {
  console.log('You are a TA');
} else if (name == "Julia" || name == "Jess") {
  console.log('You are a site lead.')
}
else {
  console.log('You are a student.');
}
//1. Where to start.
//2. How long to keep going.
//3. What to do for each loop.

for (let i = 10; i >= 0; i = i - 1) {
  console.log(i);
}
console.log('Blast off!');

//DRY = Don't repeat yourself
console.log('Welcome Phoebe')

function greet(name) {
  console.log('Welcome, ' + name + '!');
}

function fullName(firstName, lastName) {
  return firstName + '' + lastName;
}

greet(fullName('Elvin', 'Ng'));
greet(fullName('Erin', 'Wu'));

function square(number) {
  return number * number; 
}

console.log(3 * 3 + 4 * 4);

let cSquared = square(3) + square(4);
console.log(cSquared);

function fourthPower(number) {
  let stepOne = square(number);
  let stepTwo = square(stepOne);
  return stepTwo;
}

console.log(fourthPower(2));
