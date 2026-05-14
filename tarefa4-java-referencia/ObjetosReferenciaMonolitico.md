
class Produto {
    String nome;
    double preco;
}

public class ObjetosReferenciaMonolitico {

    public static void main(String[] args) {

        Produto produto = new Produto();

        produto.nome = "Notebook";
        produto.preco = 2500;

        System.out.println("Preço antes da alteração: " + produto.preco);

        System.out.println("Preço dentro do bloco antes do desconto: " + produto.preco);

        produto.preco = produto.preco - 50;

        System.out.println("Preço dentro do bloco após desconto: " + produto.preco);

        System.out.println("Preço após alteração: " + produto.preco);
    }
}
