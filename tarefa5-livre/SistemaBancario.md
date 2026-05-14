import java.util.Scanner;

public class SistemaBancario {

    public static String criarTitular(Scanner sc) {
        System.out.print("Digite o nome do titular: ");
        return sc.nextLine();
    }

    public static double depositar(double saldo, double valor) {
        return saldo + valor;
    }

    public static double sacar(double saldo, double valor) {

        if (valor > saldo) {
            System.out.println("Saldo insuficiente.");
            return saldo;
        }

        return saldo - valor;
    }

    public static void consultarSaldo(double saldo) {
        System.out.println("Saldo atual: R$ " + saldo);
    }

    public static void exibirMenu() {
        System.out.println("\n===== MENU =====");
        System.out.println("1 - Depositar");
        System.out.println("2 - Sacar");
        System.out.println("3 - Consultar Saldo");
        System.out.println("4 - Sair");
    }

    public static void imprimirDados(String titular, double saldo) {
        System.out.println("\n===== DADOS DA CONTA =====");
        System.out.println("Titular: " + titular);
        System.out.println("Saldo: R$ " + saldo);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String titular = criarTitular(sc);

        double saldo = 0;
        int opcao;

        do {

            exibirMenu();

            System.out.print("Escolha uma opção: ");
            opcao = sc.nextInt();

            switch (opcao) {

                case 1:
                    System.out.print("Valor do depósito: ");
                    double deposito = sc.nextDouble();

                    saldo = depositar(saldo, deposito);
                    break;

                case 2:
                    System.out.print("Valor do saque: ");
                    double saque = sc.nextDouble();

                    saldo = sacar(saldo, saque);
                    break;

                case 3:
                    consultarSaldo(saldo);
                    break;

                case 4:
                    imprimirDados(titular, saldo);
                    System.out.println("Encerrando sistema...");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }

        } while (opcao != 4);

        sc.close();
    }
}
