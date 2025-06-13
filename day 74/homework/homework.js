let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let strings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];



let combined = numbers.concat(strings);


delete combined[5];

combined.pop();


combined.shift();


combined.splice(1, 0, "ვანო");


combined.push("მოთიაშვილი");


let result = combined.join(", ");
console.log(result);




et list1 = [1, 2, 3];
let list2 = ["a", "b", "c"];
let list3 = [true, false, null];


let combined1 = list1.concat(list2);


let combined2 = combined1.concat(list3);  




combined2.splice(2, 3);  



delete combined2[2];  



let lastElement = combined2[combined2.length - 1];
console.log("Last element:", lastElement);