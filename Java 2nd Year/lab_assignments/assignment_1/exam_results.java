// A2

public class exam_results {
   public static void main(String[] args) {
    //Alice's Scores
    int AliceExams[] = {90, 60, 80};

    //Bob's Scores
    int BobExams[] = {50, 0, 30};

    //Clive's Scores
    int CliveExams[] = {60, 70, 75};

    
    for (int i = 0; i < AliceExams.length; i++) {
        char aliceGrade = calculateGrade(AliceExams[i]);
        char bobGrade = calculateGrade(BobExams[i]);
        char cliveGrade = calculateGrade(CliveExams[i]);

        int temp = i + 1;
        String temp2 = Integer.toString(temp);
        String exam = "exam ";
        exam = exam + temp2 + " " + "is ";

        System.out.println("Alice's final grade for " + exam + aliceGrade);
        System.out.println("Bob's final grade for " + exam + bobGrade);
        System.out.println("Clive's final grade for " + exam + cliveGrade);
        System.out.println("\n");
    }
   } 

   private static char calculateGrade(int score) {
    if (score > 80) {
        return 'A';
    } else if (score > 60) {
        return 'B';
    } else if (score > 40) {
        return 'C';
    } else {
        return 'D';
    }
   }
}
