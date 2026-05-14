class Produto {
    String nome;
    double preco;
}

public class aplicarDesconto {

    public static void aplicarDesconto(Produto p) {

        System.out.println("Preço antes do desconto: " + p.preco);

        p.preco = p.preco - 50;

        System.out.println("Preço após desconto no método: " + p.preco);
    }

    public static void main(String[] args) {

        Produto produto = new Produto();

        produto.nome = "Notebook";
        produto.preco = 2500;

        System.out.println("Preço antes da chamada: " + produto.preco);

        aplicarDesconto(produto);

        System.out.println("Preço após a chamada: " + produto.preco);
    }
}
