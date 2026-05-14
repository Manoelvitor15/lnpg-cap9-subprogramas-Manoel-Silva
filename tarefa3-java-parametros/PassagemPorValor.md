public class PassagemPorValor {

    public static void alterarNumero(int x) {

        System.out.println("Valor recebido no método: " + x);

        x = 50;

        System.out.println("Valor após alteração no método: " + x);
    }

    public static void main(String[] args) {

        int numero = 10;

        System.out.println("Valor antes da chamada do método: " + numero);

        alterarNumero(numero);

        System.out.println("Valor após a chamada do método: " + numero);
    }
}
