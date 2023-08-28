// Interface
// Need to extend the type
interface User {
    username: string;
    email: string;
    age: number;
}

interface Employee extends User { 
    employeeID: number;
}

interface Owner extends User { 
    ownerID: number;
}

const emp1 : Employee = {
    username: "davi",
    email: "davi@gmail.com",
    age: 123,
    employeeID: 123
}

const owner1 : Owner = {
    username: "davi",
    email: "davi@gmail.com",
    age: 123,
    ownerID: 123
}

console.log(emp1.username);
console.log(owner1.username);