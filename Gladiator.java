public class Gladiator extends Fighter
{
	String name = "The Gladiator";
	String weapon = "Gladius";

	public void specialMove()
	{
		System.out.println("Special Move...Coming soon");
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