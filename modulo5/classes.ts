// Programação orientada a objetos
// Fields(campos)
// Methods (Métodos)
// Construtores
// Classes Aninhadas e Interfaces( Nested Class & Interface)

class Pessoa {
    nome: string;
    idade: number;
    aFazeres: string[];
    constructor(nome: string, idade: number, aFazeres: string[]){
        this.nome = nome;
        this.idade = idade;
        this.aFazeres = aFazeres;
    }
    
    Cadastro(): string{
        return `Seu nome ${this.nome}, sua idade ${this.idade}, seus afazeres ${this.aFazeres}`
    }
}

const george = new Pessoa("George", 24, ["Box", "Code"])

console.log(george.Cadastro())