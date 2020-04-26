public class Fighter
{
	// Initializes a fighter with hitpoints and stamina.
	private int hitpoints = 100;
	private int stamina = 50;
	private String name = "The fighter"; // Try to overload this, as the name must be specific to the subclass. We may have to make this a method and overload it. Make it a getter method, and overload.  
	private String weapon = "Override me";
	private int special = 3; // Used for special move counter. 

	public Fighter()
	// Upon creation of fighter instance, fighter initialized prints.
	{
		System.out.println("Fighter Initialized");
	}

	public int getSpecial()
	// Return number of special moves left.
	{
		return special;
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

	public int getHitpoints()
	{
		// This method returns the players hitpoints.
		return hitpoints;
	}

	public int getStamina()
	{
		// Returns stamina, it won't be overidden as we keep our hitpoints and stamina safe in the parent class. 
		return stamina;
	}

	public void incHitpoints(int i)
	{
		// Increases hitpoints by i. 
		hitpoints += i;
	}

	public void incStamina(int i)
	{
		// Increases stamina by i. 
		stamina += i;
	}

	public void decHitpoints(int i)
	{
		// Decrease hitpoints by i.
		hitpoints -= i;
	}

	public void decStamina(int i)
	{
		// Decrease stamina by i. 
		stamina -= i;
	}

	public String getWeapon()
	{
		// Have no fear this will be overwritten.
		return weapon;
	}

	public void specialMove() throws InterruptedException
	{
		System.out.println("Special move, coming soon");
	}
}