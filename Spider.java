import java.util.Random;
import java.lang.Thread;
// Class requires random.

public class Spider extends Fighter
// Initializes a hobo class inheriting from fighter.
{	
	private String name = "Giant Spider";
	private String weapon = "Venomous Fangs";
	private int special = 3;

	public void specialMove() throws InterruptedException
	// Spider will attack with venom that increments the Fighter.java poison instance variable.
	// checkEffect() method will find this and act accordingly. 
	{	
		if (special > 0)
		{
			Random randomNumber = new Random();
			int x = randomNumber.nextInt(12) + 1;
			String message = this.getName() + " shoots venom for " + x + " damage";
			System.out.println(message);

			if (this.getName().equals("Computer"))
			{
				Game.player.decHitpoints(x);
			}

			if (this.getName().equals("Player"))
			{
				Game.computer.decHitpoints(x);
			}

			if (x > 6)
			{
				System.out.println("||IT'S SUPER EFFECTIVE||");

				if (this.getName().equals("Computer"))
				{
					System.out.println("Player is poisoned");
					Game.player.incPoison(2); // Increment the poison counter (inst variable) that will be checked for by the checkEffect() method in Fighter class. 
				}

				if (this.getName().equals("Player"))
				{
					System.out.println("Computer is poisoned");
					Game.computer.incPoison(2);
				}
			}
		}

		special--;

		if (special <= 0)
		{
			System.out.println(this.getName() + " is out of venom!!");
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
