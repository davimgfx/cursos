export {};

class Estudantes {
    public nomeEstudante: string;
    private idEstudante: number;
    protected idade: number;

    constructor(nomeEstudante: string, idEstudante: number, idade: number) {
        this.nomeEstudante = nomeEstudante;
        this.idEstudante = idEstudante;
        this.idade = idade;
      }

    getNomeEstudante(): string {
        return this.nomeEstudante;
    }

    setNomeEstudante(nomeEstudante: string): void {
        this.nomeEstudante = nomeEstudante;
    }

    getIdEstudante(): number {
        return this.idEstudante;
    }

    setIdEstudante(idEstudante: number): void {
        this.idEstudante = idEstudante;
    }

    getIdade(): number {
        return this.idade;
    }

    setIdade(idade: number): void {
        this.idade = idade;
    }    
}

const estudanteDavi = new Estudantes("Davi", 2, 13);
estudanteDavi.setNomeEstudante("Davi");

console.log(estudanteDavi.getIdEstudante())
console.log(estudanteDavi.getNomeEstudante())
console.log(estudanteDavi.getIdade())