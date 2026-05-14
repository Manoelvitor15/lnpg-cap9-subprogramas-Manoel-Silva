public class PassagemPorValorMonolitico {

    public static void main(String[] args) {

        int numero = 10;

        System.out.println("Valor antes da alteração: " + numero);

        int x = numero;

        System.out.println("Valor recebido no bloco: " + x);

        x = 50;

        System.out.println("Valor após alteração local: " + x);

        System.out.println("Valor original após alteração: " + numero);
    }
}
