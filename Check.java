import java.util.Random;

public class Check
{
	public static void main(String[] args)
	{
		Random randomNumber = new Random();
		System.out.println(randomNumber.nextInt(3));
		String test = "Hello";
		test = "fuck you";
		System.out.println(test);
		Fighter fighter1 = new Fighter();
		fighter1 = new Hobo();
		System.out.println(fighter1);
	}
}