public class Elf extends Fighter
{
	private String name = "The Elf";
	private String weapon = "Bow";
	private int special = 3;

	public void specialMove() throws InterruptedException
	{
		System.out.println("Special move, coming to a code near you");
		special--;
	}

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