def largest_pair_sum(numbers): 
    numbers.sort(reverse=True)
    
    return numbers[0] + numbers[1]


def spin_words(sentence):
    return " ".join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


function multiply(a, b){
  return a * b;
}



function evenOrOdd(number) {
if (number % 2 === 0) {
    return "Even";
  } else {
    return "Odd";
  }


  function makeNegative(num) {
  return num > 0 ? -num : num;
}


function opposite(number) {
  return -number
}