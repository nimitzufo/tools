import java.text.NumberFormat;
import java.util.Scanner;

public class MortgageCalculator {

	public static void main(String[] args) {

		final byte MONTHS_IN_YEAR = 12;
		final byte PERCENT = 100;
		
		Scanner scan = new Scanner(System.in);
		int principal = 0;
		
		while (true) {
			System.out.print("Principal (1k-1kk): ");
			principal = scan.nextInt();
			if(principal > 1000 && principal <= 1_000_000)
				break;
			System.out.println("Enter a number between $1,000 and $1,000,000");
		}
		
		System.out.print("Annual Interest Rate: ");
		
		float annualInt = scan.nextFloat();
		while (annualInt <= 0 || annualInt > 30) {
			System.out.println("Enter a value greater than 0 and less than or equal to 30");
			System.out.print("Annual Interest Rate: ");
			annualInt = scan.nextFloat();
		}
		float monthlyInt = annualInt /PERCENT/MONTHS_IN_YEAR;
		
		System.out.print("Period (Years): ");
		
		byte years = scan.nextByte();
		while (years < 1 || years > 30) {
			System.out.println("Enter a value between 1 and 30");
			System.out.print("Period (Years): ");
			years = scan.nextByte();
		}
		int numberOfPayments = years*12;
		double fact = Math.pow(monthlyInt+1, numberOfPayments);
		double mortgage = (principal*monthlyInt)*fact/(fact-1);
		
		String mortgageFormatted =  NumberFormat.getCurrencyInstance().format(mortgage);
		
		System.out.print("Mortgage: " + mortgageFormatted);
	}
				
}
