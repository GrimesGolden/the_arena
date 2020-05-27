import java.util.Random;
import java.lang.Thread;
// Class requires random.

public class Hobo extends Fighter
// Initializes a hobo class inheriting from fighter.
{	
	private String name = "The Hobo";
	private String weapon = "Slingshot";
	private int special = 3;

	public void specialMove() throws InterruptedException
	{	
		if (special > 0)
		{
			Random randomNumber = new Random();
			System.out.println(this.getName() + " pulls out 40oz of King Cobra\n");
			System.out.println("AND STARTS CHUGGING!!\n");
			int x = randomNumber.nextInt(10) + 15;
			String healing = "It heals " + this.getName() + " for " + x + " hitpoints!\n";
			System.out.println(healing);

			if (x > 6)
			{
				System.out.println("||IT'S SUPER EFFECTIVE||");
			}

			this.incHitpoints(x);
			String statement = "||" + this.getName() + "s hitpoints:  " + this.getHitpoints() + " ||\n";
			System.out.println(statement);
			special--;
			Thread.sleep(1000);
		}

		if (special <= 0)
		{
			System.out.println(this.getName() + " is out of malt liquor!!");
			Thread.sleep(1000);
		}
		
	}

	public String getName()
	{
		// This method returns the name variable, and will be overidden by the child class. 
		return name;
	}

	public int getSpecial()
	// Return number of special moves left.
	{
		return special;
	}

	public String getWeapon()
	{
		// Getter method for weapon variable/
		return weapon;
	}

	public void setName(String name)
	{
		//Set name variable
		this.name = name;
	}

}


