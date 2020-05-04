import java.util.Random;
import java.lang.Thread;

public class Gladiator extends Fighter
{
	private String name = "The Gladiator";
	private String weapon = "Gladius";
	private int special = 3;

	public void specialMove() throws InterruptedException
	{	
		Random randomNumber = new Random();
		int x = randomNumber.nextInt(4);

		System.out.println(this.getName() + " looks to the emperor.\n");
		Thread.sleep(1000);
		System.out.println("...");
		Thread.sleep(1000);

		if (this.getName().equals("Player") && this.getSpecial() > 0)
			// If this turn is  a player turn.
		{
			if (Game.computer.getHitpoints() < 25)
			{
				if (x == 0)
				{
					System.out.println("The emperor looks coldly at the Computer");
					Thread.sleep(1000);
					System.out.println("...");
					Thread.sleep(1000);
					System.out.println("Thumbs down, FINISH HIM!");
					Game.computer.decHitpoints(100);
					System.out.println("In desperation Computer mounts a final attack!!!");
				}

				else if (x > 0)
				{
					System.out.println("The emperor gives a thumbs up!");
					Thread.sleep(1000);
					System.out.println("CONTINUE THE FIGHT!");
				}
			}

			else if (Game.computer.getHitpoints() > 25)
			{
				System.out.println("The emperor does not deign to  intevene, Computers hitpoints are too great.");
			}

		} // End player if.
			

		if (this.getName().equals("Computer") && this.getSpecial() > 0)
		{
			// If this turn is  a Computer turn.
			if (Game.player.getHitpoints() < 25)
			{
				if (x == 0)
				{
					System.out.println("The emperor looks coldly at the Player");
					Thread.sleep(1000);
					System.out.println("...");
					Thread.sleep(1000);
					System.out.println("Thumbs down, FINISH HIM!");
					Game.player.decHitpoints(100);
				}

				else if (x > 0)
				{
					System.out.println("The emperor gives a thumbs up!");
					Thread.sleep(1000);
					System.out.println("CONTINUE THE FIGHT!");
					Thread.sleep(1000);
					System.out.println("...");
					Thread.sleep(1000);
					System.out.println("Phew!! That was close!");
				}
			}

			else if (Game.player.getHitpoints() > 25)
			{
				System.out.println("The emperor does not deign to  intevene, Players hitpoints are too great.");
			}
		} // End computer if.

		special--; // Decrement special.

		if (special <= 0) // Special is less than zero. Comes after decrementation to inform player.
		{
			System.out.println(" The emperor is bored with the proceedings, do not bother him again!"); 
			// Therefore out of specials, also sleep so the log doesnt get spammed. 
			Thread.sleep(1000);
		}
		
	} // End special move.

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

	public void setName(String name)
	{
		//Set name variable
		this.name = name;
	}

	public int getSpecial()
	// Return number of special moves left.
	{
		return special;
	}
	
}

