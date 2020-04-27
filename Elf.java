import java.util.Random;
import java.lang.Thread;

public class Elf extends Fighter
{
	private String name = "The Elf";
	private String weapon = "Bow";
	private int special = 3;

	public void specialMove() throws InterruptedException
	// Fires a flaming arrow that deals burn damage.

	{	
		Random randomNumber = new Random();
		int x = randomNumber.nextInt(12) + 1;
		int y = randomNumber.nextInt(20) + 1;
		System.out.println("\n");
		
		
		if (this.getName().equals("Player") && this.getSpecial() > 0)
			// If user is Player and has special moves left...
		{	
			System.out.println(this.getName() + " fires a flaming arrow at the enemy\n");

			if (Game.computer.getWeapon().equals("Slingshot"))
				//If computers weapon is slingshot, then they are playing as the hobo.

			{	
				
				System.out.println("The computer is playing as booze soaked hobo...");
				Thread.sleep(1000);
				System.out.println("...");
				System.out.println("The flames are super effective!");
				System.out.println("Roasted for " + y + " damage!");
				System.out.println();
				Game.computer.decHitpoints(y);
			}

			else
			{
				System.out.println("Computer roasted for " + x + " damage!");
				Game.computer.decHitpoints(x);
			} // End else
		} // End players if

		if (this.getName().equals("Computer") && this.getSpecial() > 0)
			// If this is the computer accessing the method....
		{	
			System.out.println(this.getName() + " fires a flaming arrow at the enemy\n");

			if (Game.player.getWeapon().equals("Slingshot"))
				// If player is hobo. 

			{
				System.out.println("The player is using the booze soaked hobo...");
				Thread.sleep(1000);
				System.out.println("...");
				System.out.println("The flames are super effective!");
				System.out.println("Roasted for " + y + " damage!");
				System.out.println();
				Game.player.decHitpoints(y);
			}

			else
			{
				System.out.println("Player roasted for " + x + " damage!");
				Game.player.decHitpoints(x);
			}
		} // End computers if.

		special--; // Decrement special moves.

		if (special <= 0) // Special is less than zero.
		{
			System.out.println(this.getName() + " is out of flame arrows!!"); 
			// Therefore out of flame arrows, also sleep so the log doesnt get spammed. 
			Thread.sleep(1000);
		}

		Thread.sleep(1000);

	} // End method.

	public String getName()
	{
		// This method returns the name variable, and will be overidden by the child class. 
		return name;
	}

	public void setName(String name)
	{
		//Set name variable
		this.name = name;
	}

	public String getWeapon()
	{
		// Getter method for weapon variable/
		return weapon;
	}

	public int getSpecial()
	// Return number of special moves left.
	{
		return special;
	}

}