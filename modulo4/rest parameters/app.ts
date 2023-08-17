// Não restringe o numero de valores, porem devem ser todos
// do mesmo tipo

function osNomes(...nomes: string[]): void {
    nomes.forEach(nome => console.log(nome));
}

osNomes("Davi", "Joao", "Caeteno", "Policia");
