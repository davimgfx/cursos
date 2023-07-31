// Tratamento de erros
function errorMessage(message: string) : never {
    throw new Error(message)
}

console.log(errorMessage("Erro"))