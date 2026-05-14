import java.util.Scanner;

public class ControleAcademico {

    public static String lerAluno(Scanner sc, int indice) {
        System.out.println("Digite o nome do aluno " + (indice + 1) + ":");
        return sc.nextLine();
    }

    public static double[] lerNotas(Scanner sc, String aluno) {
        double[] notas = new double[3];

        for (int i = 0; i < 3; i++) {
            System.out.println("Digite a nota " + (i + 1) + " de " + aluno + ":");
            notas[i] = sc.nextDouble();
        }

        sc.nextLine();
        return notas;
    }

    public static double calcularMedia(double[] notas) {
        double soma = 0;

        for (double nota : notas) {
            soma += nota;
        }

        return soma / notas.length;
    }

    public static String determinarSituacao(double media) {
        if (media >= 7) {
            return "Aprovado";
        } else if (media >= 5) {
            return "Recuperação";
        } else {
            return "Reprovado";
        }
    }

    public static void imprimirRelatorio(String[] alunos, double[] medias, String[] situacoes) {
        System.out.println("\n===== RELATÓRIO FINAL =====");

        for (int i = 0; i < alunos.length; i++) {
            System.out.println("Aluno: " + alunos[i]);
            System.out.println("Média: " + medias[i]);
            System.out.println("Situação: " + situacoes[i]);
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] alunos = new String[5];
        double[] medias = new double[5];
        String[] situacoes = new String[5];

        for (int i = 0; i < 5; i++) {
            alunos[i] = lerAluno(sc, i);

            double[] notas = lerNotas(sc, alunos[i]);

            medias[i] = calcularMedia(notas);

            situacoes[i] = determinarSituacao(medias[i]);
        }

        imprimirRelatorio(alunos, medias, situacoes);

        sc.close();
    }
}
