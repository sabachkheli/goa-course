let age = prompt("Enter your age:");
age = parseInt(age);

if (age <= 14) {
  console.log("you are kid");
} else if (age <= 18) {
  console.log("you are not adult yet");
} else {
  console.log("you are adult");
}


let name = "Saba"; 

if (name) {
  console.log("Hello, " + name + "!");
} else {
  name = "guest";
  console.log("Hello, " + name + "!");
}



let name = prompt("Enter your name:");
    let age = parseInt(prompt("Enter your age:"));

    if (age <= 18) {
      alert("you are not adult yet " + name + "!");
    } else {
      alert("Hello " + name + "!");
    }