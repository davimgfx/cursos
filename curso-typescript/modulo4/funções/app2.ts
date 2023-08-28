function factorialNumbers(n : number) : number{
    if(n === 0 || n === 1){
      return 1
    }
    return n*factorialNumbers(n - 1)
}

function factDigits(n : number ) : number{
    const result = factorialNumbers(n).toString().split("")
    return result.length
}

console.log(factorialNumbers(777))
console.log(factDigits(777))