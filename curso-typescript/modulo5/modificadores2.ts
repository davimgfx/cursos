export {}
// readonly - read only (Não Pode alterar o valor)

class Funcionario {
    readonly dataNascimento: Date;
    constructor(dataNascimento: Date) {
        this.dataNascimento = dataNascimento;
    }
}

const funcionario = new Funcionario(new Date(1999, 10, 10));
// erro funcionario.dataNascimento = new Date(2020, 10, 10)
console.log(funcionario.dataNascimento );

interface FuncionarioProps{
    codigoFuncionario: string;
    nomeEmpregado: string;
}

const funcionario2: Readonly<FuncionarioProps> = {
    codigoFuncionario: "string;",
    nomeEmpregado: "string;"
}

console.log(funcionario2.nomeEmpregado)