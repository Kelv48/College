// A2
// Kelvin Osagie 122318693

public class loan {
    public static void main(String[] args) {
        int aliceIncome = 1500;
        int bobIncome = 700;
        int cliveIncome = 100;

        int aliceLoanCategory = calculateLoanCategory(aliceIncome);
        int bobLoanCategory = calculateLoanCategory(bobIncome);
        int cliveLoanCategory = calculateLoanCategory(cliveIncome);

        double aliceAnnualIncome = aliceIncome * 12;
        double bobAnnualIncome = bobIncome * 12;
        double cliveAnnualIncome = cliveIncome * 12;

        double aliceLoanAmount = calculateLoanAmount(aliceLoanCategory, aliceAnnualIncome);
        double bobLoanAmount = calculateLoanAmount(bobLoanCategory, bobAnnualIncome);
        double cliveLoanAmount = calculateLoanAmount(cliveLoanCategory, cliveAnnualIncome);

        System.out.println("Alice's loan category: " + aliceLoanCategory + " , Loan amount: " + aliceLoanAmount + " euros");
        System.out.println("Bob's loan category: " + bobLoanCategory + " , Loan amount: " + bobLoanAmount + " euros");
        System.out.println("Clive's loan category: " + cliveLoanCategory + " , Loan amount: " + cliveLoanAmount + " euros");
    }

    private static int calculateLoanCategory(int income) {
        int loanCategory;
        
        if (income > 1000) {
            loanCategory = 1;
            return loanCategory;
        } else if (income > 500 && income < 1000) {
            loanCategory = 2;
            return loanCategory;
        } else if (income > 200 && income < 500) {
            loanCategory = 3;
            return loanCategory;
        } else if (income > 0 && income < 200) {
            loanCategory = 4;
            return loanCategory;
        } else {
            loanCategory = 4;
            return loanCategory;
        }
    }

    private static double calculateLoanAmount(int category, double annualIncome) {
       double loanAmount;
       
       switch (category) {
        case 1:
            loanAmount = 3.5 * annualIncome;
            break;
        case 2:
            loanAmount = 2.5 * annualIncome;
            break;
        case 3:
            loanAmount = 2.0 * annualIncome;
            break;
        default:
            loanAmount = 0.0;
            break;
       }
       return loanAmount;
    }
}
