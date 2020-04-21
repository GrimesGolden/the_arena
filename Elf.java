public class Elf extends Fighter
{
	String name = "The Elf";
	String weapon = "Bow";

	public void specialMove()
	{
		System.out.println("Special move, coming to a code near you");
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