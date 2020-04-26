public class Gladiator extends Fighter
{
	private String name = "The Gladiator";
	private String weapon = "Gladius";
	private int special = 3;


	public void specialMove() throws InterruptedException
	{
		System.out.println("Special Move Activated\n");
		special--;
		
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