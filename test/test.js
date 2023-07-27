console.log("hello world")

function isPrime(n) {
  // check 2 through n-1 
  // n = 100
  if (n < 2) {
    return false
  }

  for (let i = 2; i < Math.sqrt(n) + 1; i++) {
    if (n % i === 0) {
      return false
    }
  }
  return true
}

// console.log(isPrime(7))
// console.log(isPrime(6))

// for (let i = 0; i <= 100; i++) {
//   if (isPrime(i)) {
//     console.log(i)
//   }
// }

function isPrime2(n) {
  if (n < 2) {
    return false
  }

  for (let i = 2; i < n / 2; i++) {
    if (n % i === 0) {
      return false
    }
  }
  return true
}