import java.util.Random;
import java.util.Scanner;
import java.lang.Thread;
//For use in Thread.sleep(), don't forget it throws interrupted.

public class Game
{	 static Fighter player;
	 static Fighter computer;

	public static void main(String[] args) throws InterruptedException
	{
		Game.gameLoop();
	} // End main method, need to design computers turn. 

	public static Fighter getPlayer()
	{
		return player;
	}

	public static Fighter getComputer()
	{
		return computer;
	}

	public static Fighter computers_pick()
	{
		Random randomNumber = new Random();
		int x = randomNumber.nextInt(3);

		Fighter computer;

		if (x == 0)
		{
			computer = new Gladiator();
		}

		else if (x == 1)
		{
			computer = new Hobo();
		}

		else
		// There must be an else here, otherwise the compiler will complain.
		{
			computer = new Elf();
		}

		return computer;
	}

	public static Fighter players_pick()
	{	Scanner kb = new Scanner(System.in); // Creating scanner object.
		System.out.println("Select your fighter:\n");
		System.out.println("For Hobo with a Slingshot || enter: A ||"
			+ "\nFor Gladiator || type B ||\nFor the Elf || type C");
		String letter = "";
		Fighter player = new Fighter(); // I intialized this first because java compiler needs it declared. keep an eye on this however, it could cause errors due to a blank fighter. 

		while (!letter.equals("A") || !letter.equals("B") || !letter.equals("C"))
		{	
			System.out.println("Enter your selection: "); 
			letter = kb.nextLine(); 
			if (letter.equals("A"))
			{
				player = new Hobo();
				break;
			}
			else if (letter.equals("B"))
			{
				player = new Gladiator();
				break;
			}
			else if (letter.equals("C"))
			{
				player = new Elf();
				break;
			}
			else
			{
				System.out.println("Incorrect input\nChoices are A, B or C: ");
			}
		}

		return player;
	
		
	}

	public static void instructions() throws InterruptedException
	{
		// Prints a series of instructions for the user.
		System.out.println("Welcome to the Arena. A Product of \'Grimes Golden\' Software\n");
		Thread.sleep(2000);
		System.out.println("Every fighter will begin with 100 hit points and 50 stamina.\n");
		System.out.println("Your fighter will die if they reach 0 hit points.\n");
		System.out.println("Press P for punch, K for kick, W for weapon (takes 10 stamina), S for special move, or Q to quit.");
		Thread.sleep(2000);
		System.out.println("Type H at any time to see these instructions again.\n");
	}

	public static Fighter intro() throws InterruptedException
	{
		// Prints an introduction
		System.out.println("Computer is selecting.");
		Thread.sleep(1000);
		System.out.println("...");
		Thread.sleep(1000);
		System.out.println("...");
		Thread.sleep(1000);
		Fighter computer = Game.computers_pick();
		System.out.println("Compiling fighters.");
		Thread.sleep(1000);
		System.out.println("...");
		Thread.sleep(1000);
		return computer;
	}

	public static void init() throws InterruptedException
	{
		// Initializes the games variables, starting the game.
		Game.instructions();
		player = Game.players_pick();
		computer = Game.intro();
		String playerName = (player.getName());
		String computerName = (computer.getName());
		System.out.println("Player picked " + playerName + "\nComputer picked " + computerName + "\n");

		player.setName("Player"); // Set names so they refer to player rather than "hobo" for example, during the rest of the game. 
		computer.setName("Computer");
	}

	public static void computers_turn() throws InterruptedException
	// Allows the computer to attack in it's own enclosed loop. 
	{
		int draw_weapon = 1;
		Random randomNumber = new Random();
		int comps_move = randomNumber.nextInt(4);

		if (computer.getSpecial() <= 0)
		// This simulates a human decision to not use your special move if you are out of counters. 
		{
			comps_move = randomNumber.nextInt(3);
		}
	
		System.out.println("------------------------Computers Turn-------------------------");

		if (comps_move == 0)
		{
			int x = randomNumber.nextInt(25);
			if (x > 10)
			{
				Thread.sleep(1000);
				System.out.println("Critical Hit!");
				String messageDisplay = "Computer critically hits player one  for " + x + " points ";
				Thread.sleep(1000);
				System.out.println(messageDisplay);
				player.decHitpoints(x);
				Thread.sleep(1000);
				String healthMessage = "||Player hitpoints:  " + player.getHitpoints() + " ||\n";
				System.out.println(healthMessage);
				Thread.sleep(1000);
			}
			else
			{
				String punchMessage = "Computer punches player for " + x + " points \n";
				System.out.println(punchMessage);
				Thread.sleep(1000);
				player.decHitpoints(x);
				String hitMessage = "||Player hitpoints:  " + player.getHitpoints() + " ||\n";
				System.out.println(hitMessage);
				Thread.sleep(1000);
			}
		}

		else if (comps_move == 1)
		{
			int x = randomNumber.nextInt(25);
			if (x > 10)
			{
				Thread.sleep(1000);
				System.out.println("Critical Hit!");
				String messageDisplay = "Computer critically hits player one  for " + x + " points \n";
				System.out.println(messageDisplay);
				Thread.sleep(1000);
				player.decHitpoints(x);
				Thread.sleep(1000);
				String healthMessage = "||Player hitpoints:  " + player.getHitpoints() + " ||\n";
				System.out.println(healthMessage);
				Thread.sleep(1000);
			}
			else
			{
				String punchMessage = "Computer kicks player for " + x + " points \n";
				System.out.println(punchMessage);
				Thread.sleep(1000);
				player.decHitpoints(x);
				String hitMessage = "||Player hitpoints:  " + player.getHitpoints() + " ||\n";
				System.out.println(hitMessage);
				Thread.sleep(1000);
			}
		}

		else if (comps_move == 2)
		{
			int x = randomNumber.nextInt(45);

			String wepMessage = "Computer draws " + computer.getWeapon() + "!\n";
			System.out.println(wepMessage);
			if (computer.getStamina() < 10)
			{
				System.out.println("But they are out of stamina\n");
			}
			if (computer.getStamina() > 10)
			{
				Thread.sleep(1000);
				player.decHitpoints(x);
				String wepMessage1 = computer.getWeapon() + " strike for " + x + " hitpoints.\n";
				System.out.println(wepMessage1);
				Thread.sleep(1000);
				String hitMessage = "||Player hitpoints:  " + player.getHitpoints() + " ||\n";
				System.out.println(hitMessage);
				Thread.sleep(1000);
				computer.decStamina(10);
			}
		}

		else if (comps_move == 3 && computer.getSpecial() > 0)
		{
			computer.specialMove();
		}

		System.out.println("------------------------Your Turn-------------------------");

	}

	public static void gameLoop() throws InterruptedException
	{
		Game.init();
		Scanner kb = new Scanner(System.in); // Used to scan players moves.
		Random randomNumber = new Random(); // Used to randomize integers, simulating dice.
		int compHealth = computer.getHitpoints();
		int playerHealth = player.getHitpoints();
		int playerStamina = player.getStamina();
		int draw_weapon = 1;
		// Commence main loop.
		while(player.getHitpoints() > 0 && computer.getHitpoints() > 0)
		{
			System.out.println("Enter your move: \n");
			String move = kb.nextLine(); 
			switch (move) {
				case "P": 
					int x = randomNumber.nextInt(16);
					if (x > 10)
					{
						Thread.sleep(1000);
						System.out.println("...");
						Thread.sleep(1000);
						System.out.println("Critical Hit");
						String critMessage = ("You crit Computer for " + x + " points\n ");
						System.out.println(critMessage);
						Thread.sleep(1000);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						System.out.println(hitMessage);
						Thread.sleep(1000);
						Game.computers_turn(); 
						break;
					}
					else
					{
						String punchMessage = "You punch Computer for " + x + " points \n";
						System.out.println(punchMessage);
						Thread.sleep(1000);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						System.out.println(hitMessage);
						Thread.sleep(1000);
						Game.computers_turn(); 
						break;
					}

				case "K":
					x = randomNumber.nextInt(16);
					if (x > 10)
					{
						Thread.sleep(1000);
						System.out.println("...");
						Thread.sleep(1000);
						System.out.println("Critical Hit");
						String critMessage = ("You crit Computer for " + x + " points ");
						System.out.println(critMessage);
						Thread.sleep(1000);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						System.out.println(hitMessage);
						Thread.sleep(1000);
						Game.computers_turn(); // Replace with the computers turn.
						break;
					}
					else
					{
						String punchMessage = "You kick Computer for " + x + " points \n";
						System.out.println(punchMessage);
						Thread.sleep(1000);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						Thread.sleep(1000);
						System.out.println(hitMessage);
						Game.computers_turn(); // Replace with the computers turn.
						break;
					}

				case "W":
					// Weapon loop
					draw_weapon -= 1;
					x = randomNumber.nextInt(30);
					if (draw_weapon == 0)
					{
						String drawMessage = "You draw your " + player.getWeapon() + "!\n";
						System.out.println(drawMessage);
						Thread.sleep(1000);
					}

					if (draw_weapon <= 0)
					{
						x = randomNumber.nextInt(30);
					}

					if (player.getStamina() < 10)
					{
						System.out.println("You are too exhausted to use your weapon!!");
						break;
					}

					else if (x > 25)
					{
						Thread.sleep(1000);
						System.out.println("...");
						Thread.sleep(1000);
						System.out.println("Critical Hit");
						String wepCritMessage = ("You crit Computer with " + player.getWeapon() +  " for " + x + " points! ");
						System.out.println(wepCritMessage);
						Thread.sleep(1000);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						System.out.println(hitMessage);
						Thread.sleep(1000);
						System.out.println("Your stamina reduced by 10\n");
						player.decStamina(10);
						String stamMessage = player.getStamina() + " stamina left!";
						System.out.println(stamMessage);
						Thread.sleep(1000);
						Game.computers_turn();  
						break;
					}

					else
					{
						String weaponMessage = "You attack with " + player.getWeapon() + " for " + x + " points \n";
						System.out.println(weaponMessage);
						computer.decHitpoints(x);
						String hitMessage = "||Computer hitpoints: " + computer.getHitpoints() + "||\n";
						System.out.println(hitMessage);
						Thread.sleep(1000);
						System.out.println("Your stamina reduced by 10\n");
						player.decStamina(10);
						String stamMessage = player.getStamina() + " stamina left!";
						System.out.println(stamMessage);
						Thread.sleep(1000);
						Game.computers_turn(); 
						break;
					}

				case "S":
					player.specialMove();
					Game.computers_turn();
					break;

				case "H":
					Game.instructions();
					break;

				case "Q":
					System.out.println("||QUIT ENTERED||");
					Thread.sleep(1000);
					System.out.println("||EXITING||");
					computer.decHitpoints(1000);
					computer.decHitpoints(1000); // Assures the larger while loop will break.
					break;

				default:
					System.out.println("||INCORRECT INPUT||\n");
					System.out.println("Press H for instructions");	
					break;
					// The default will exit the switch, but it will not exit the while loop.
					// The only way to exit the while loop is by the hitpoints decrementing below <= 0.
					// That has to be hardcoded in (see case "Q");

			} // End switch

		} // End while loop

		if (player.getHitpoints() > computer.getHitpoints())
		{
			System.out.println("||PLAYER ONE WINS||");
		}

		else if (computer.getHitpoints() > player.getHitpoints())
		{
			System.out.println("||GAME OVER||");
			System.out.println("||COMPUTER WINS, ITS ONLY GETTING SMARTER WITH EACH WIN||");
		}

		else
		{
			System.out.println("Error");
			System.out.println("Whoops, you fell through the code! Sorry");
		}
	}

	
}