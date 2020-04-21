import java.util.Random;
// Class requires random.

public class Hobo extends Fighter
// Initializes a hobo class inheriting from fighter.
{	
	String name = "The Hobo";
	String weapon = "Slingshot";

	public void specialMove()
	{	
		Random randomNumber = new Random();
		int playerHealth = this.getHitpoints(); // Thank god for the this statement ayy boys?
		System.out.println("The hobo pulls out 40oz of King Cobra\n");
		System.out.println("AND STARTS CHUGGING!!\n");
		int x = randomNumber.nextInt(12) + 1;
		String healing = "It heals Hobo for " + x + " hitpoints!";
		System.out.println(healing);
		if (x > 6)
		{
			System.out.println("||IT'S SUPER EFFECTIVE||");
		}

		this.incHitpoints(x);
		String statement = "Player One has " + playerHealth + " hitpoints.";
		System.out.println(statement);
	}

	public String getName()
	{
		// This method returns the name variable, and will be overidden by the child class. 
		return name;
	}

	public String getWeapon()
	{
		// Getter method for weapon variable/
		return weapon;
	}


}