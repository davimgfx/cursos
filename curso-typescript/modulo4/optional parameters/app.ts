function cadastrarUsuario (name: string, email ?: string, number?: number): string {
    return `seu nome é ${name}, ${email ? `seu email é ${email} ` : "" }${number ? `seu numero é ${number}` : ""}`
}
console.log(cadastrarUsuario("davi"))
console.log(cadastrarUsuario("davi", "davi@gmail.com"))
console.log(cadastrarUsuario("davi", "", 888888))
console.log(cadastrarUsuario("davi", "davi@gmail.com", 888888))