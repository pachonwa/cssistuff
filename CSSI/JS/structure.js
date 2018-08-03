console.log('something');

let score1 = 97;
let score2 = 92;
let score3 = 90;

let scores = [97,92,90,87,88,100,99, 105];
let max = scores[0];
let total = 0;

for(i=0; i < scores.length; i++) {
  //console.log(scores[i]);
  if (scores[i] > max) {
    max = scores[i];
  }
}
//console.log('The max score is ' + max);

for (i=0; i < scores.length; i++) {
  total += scores[i];
}
//console.log('The total value is ' + total);

let names = ['Savion', 'Jenny', 'Olivia', 'Joshua'];
names.forEach(name => {
  //console.log('Welcome ' + name);
});

//let matthew = ['Matthew', 'Levine', 'Dartmouth', 'Harry Potter'];
//console.log(matthew[2]);
//let yojairo = ['Yojairo', 'Morales', 'USC', 'Kendrick Lamar'];

let matthew = {
  'firstName': 'Matthew',
  'lastName': 'Levine',
  'university': 'Dartmouth',
  'culture': 'Harry Potter',
  'siblings': 4,
};
console.log(matthew.university);

let yojairo = {
  'firstName': 'Yojairo',
  'lastName': 'Morales',
  'university': 'USC',
  'culture': 'Kendrick Lamar',
};
let people = [matthew, yojairo];
people.forEach(person => {
  console.log(person.firstName + ' really likes ' + person.culture)
});
