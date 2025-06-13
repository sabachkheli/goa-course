console.log(!false);
console.log(!0);
console.log(!null);
console.log!(undefined);
console.log(!"");

console.log(!true);
console.log(!1);
console.log(!"hello");
console.log(![]);
console.log(!{});





function randomNumberProcess() {
  const num = Math.floor(Math.random() * 10); // 0-დან 9-მდე რანდომი რიცხვი
  if (num > 5) {
    return num;
  } else {
    return num * num;
  }
}

const result = randomNumberProcess();
console.log(result);






const name = "Saba";

if (name.length > 5) {
  console.log("this is my friend");
} else {
  console.log(name);
}