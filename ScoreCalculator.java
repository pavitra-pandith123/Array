public class ScoreCalculator{
    public static void maon(String[] args){
        int[] score={72,83,63,83};
        int n=score.length;
        int sum=0;
        for(int Score:score){
            sum +=Score;
        }
        double average=(double)
        sum/n;
        System.out.println("Scores");
        for(int Score:score){
            System.out.println("\n sum of scores:"+sum);
            System.out.println("\n Average of scores:"+average);
        }
    }
}