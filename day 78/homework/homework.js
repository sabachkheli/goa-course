const input = prompt("გთხოვთ შეიყვანოთ რიცხვი:");
const number = Number(input);

if (isNaN(number)) {
  console.log("შეყვანილი მონაცემი რიცხვი არაა.");
} else {
  if (number % 2 === 0) {
    console.log("ლუწია");
  } else {
    console.log("კენტი");
  }
}




const ageInput = prompt("გთხოვთ შეიყვანოთ თქვენი ასაკი:");
const age = Number(ageInput);

if (isNaN(age) || age < 0) {
  console.log("შეყვანილი მონაცემი არ არის სწორი ასაკი.");
} else {
  if (age < 18) {
    console.log("თქვენ მიიღეთ 50%-იანი ფასდაკლება.");
  } else {
    console.log("თქვენ არ მიიღეთ ფასდაკლება.");
  }
}


const name = prompt("გთხოვთ შეიყვანოთ თქვენი სახელი:");

if (name.length > 6) {
  console.log(`hello my friend '${name}!'`);
} else {
  console.log(`hello '${name}!'`);
}