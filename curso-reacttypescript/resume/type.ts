// Important of Type ( Without Type)

// const  worseFunction = ( user: {username: string, password?: string, type?: string, number?: number}) => {
//     console.log(user.username)
// }
// const obj = {
//     username: "Davi"
// }

// worseFunction(obj)


// Using Type

// type UserInfos = {
//     username: string,
//     password?: string,
//     type?: string,
//     number?: number
// }

// const obj = {
//     username: "Davi",
//     number: 999
// }

// const betterFunction = (user : UserInfos) => {
//     console.log(user.username)
//     console.log(user.number)
// }

// betterFunction(obj)

// Another example

// function add(a: number, b: number) : number {
//     return a + b
// }

// function subtract(a: number, b: number) : number {
//     return a - b
// }

// type MathOperation = (a: number, b: number) => number

// const add: MathOperation = (a, b) => a + b;
// const subtract: MathOperation = (a, b) => a - b;
// const multiply: MathOperation = (a, b) => a * b;

// console.log(add(1, 2))
// console.log(subtract(3, 1))
// console.log(multiply(2,2))