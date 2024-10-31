import random
import matplotlib.pyplot as plt


def throwTwoDice(rounds):
    """
    Simulates the process of throwing two dice a specified number of times.

    Parameters:
        rounds (int): The number of rounds to simulate.

    Returns:
        list: A list of lists, where each inner list contains the result of two dice rolls
              and their sum in the format [dice1, dice2, sum].
    """
    results = []

    for _ in range(rounds):
        random_number1 = random.randint(1, 6)  # Roll the first die
        random_number2 = random.randint(1, 6)  # Roll the second die
        dice_sum = sumOfDices(random_number1, random_number2)
        results.append([random_number1, random_number2, dice_sum])  # Append dice results and their sum

    return results


def sumOfDices(number1, number2):
    """
    Calculates the sum of two dice values.

    Parameters:
        number1 (int): Result of the first die roll.
        number2 (int): Result of the second die roll.

    Returns:
        int: The sum of the two dice.
    """
    return number1 + number2


def x_inv(x, DiceValues, size):
    """
    Finds all pairs of dice rolls that add up to a specified target value x.

    Parameters:
        x (int): The target sum to search for.
        DiceValues (list): List of dice roll results and their sums.
        size (int): Total number of dice roll records.

    Returns:
        list: A list of pairs of dice rolls that add up to the target value x.
    """
    results = []

    for i in range(size):
        if DiceValues[i][2] == x:  # Check if the sum equals the target value
            results.append([DiceValues[i][0], DiceValues[i][1]])  # Append the pair if sum matches x

    return results


def get_expected_value(x):
    """
    Returns the theoretical probability of rolling a specific sum x with two dice.

    Parameters:
        x (int): Desired sum of two dice.

    Returns:
        float: The theoretical probability of rolling the specified sum.
    """
    match x:
        case 2:
            return 1 / 36
        case 3:
            return 2 / 36
        case 4:
            return 3 / 36
        case 5:
            return 4 / 36
        case 6:
            return 5 / 36
        case 7:
            return 6 / 36
        case 8:
            return 5 / 36
        case 9:
            return 4 / 36
        case 10:
            return 3 / 36
        case 11:
            return 2 / 36
        case 12:
            return 1 / 36
        case _:
            return 0


def prob(desired_value_length, size):
    """
    Calculates the probability of a specific event based on occurrences and total events.

    Parameters:
        desired_value_length (int): Number of occurrences of the desired event.
        size (int): Total number of events.

    Returns:
        float: The probability of the event.
    """
    return desired_value_length / size


def Expected_Value(DiceValues, size):
    """
    Calculates the average expected value for each die based on recorded rolls.

    Parameters:
        DiceValues (list): List of dice roll results.
        size (int): Total number of dice rolls.

    Returns:
        tuple: Expected values for the first and second dice.
    """
    total_sum_dice1 = 0
    total_sum_dice2 = 0

    for roll in DiceValues:
        total_sum_dice1 += roll[0]  # Sum of first die results
        total_sum_dice2 += roll[1]  # Sum of second die results

    expected_value_die1 = total_sum_dice1 / size  # Calculate expected value for first die
    expected_value_die2 = total_sum_dice2 / size  # Calculate expected value for second die

    return expected_value_die1, expected_value_die2


def plot_dice_sums_histogram(sums):
    """
    Plots a histogram showing the distribution of sums obtained from rolling two dice.

    Parameters:
        sums (list): List of sums obtained from each dice roll pair.
    """
    plt.hist(sums, bins=range(2, 14), edgecolor="black", align="left")
    plt.title("Distribution of Dice Sums")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Frequency")
    plt.xticks(range(2, 13))
    plt.show()


def plot_expected_values(expected_value_die1, expected_value_die2):
    """
    Plots the expected values of each die as a bar chart.

    Parameters:
        expected_value_die1 (float): Expected value for the first die.
        expected_value_die2 (float): Expected value for the second die.
    """
    plt.bar(['Dice 1', 'Dice 2'], [expected_value_die1, expected_value_die2], color=['blue', 'orange'])
    plt.title("Expected Value of Each Dice")
    plt.xlabel("Dice")
    plt.ylabel("Expected Value")
    plt.ylim(3, 4)
    plt.show()


def main():
    """
    Main function to simulate dice rolls, calculate probabilities, and display results.
    """
    size = 50  # Number of dice roll rounds
    x = 8  # Desired sum value

    DiceValues = throwTwoDice(size)
    x_preimages = x_inv(x, DiceValues, size)
    Possibility_Of_X = prob(len(x_preimages), size)
    x_expected = get_expected_value(x)
    sums = [roll[2] for roll in DiceValues]
    Expected_Value_x1, Expected_Value_x2 = Expected_Value(DiceValues, size)

    #Uncomment to display results and plots
    print(DiceValues)
    print("------------------------------------------------------------------------------------------")
    print(x_preimages)
    print(len(x_preimages))
    # print("------------------------------------------------------------------------------------------")
    # print(f"Expected value of: {x_expected:.3f}")
    # print(Possibility_Of_X)
    # plot_dice_sums_histogram(sums)
    # print("------------------------------------------------------------------------------------------")
    print("Expected value of one dice is : 3.5")
    print(Expected_Value_x1)
    print(Expected_Value_x2)
    # plot_expected_values(Expected_Value_x1, Expected_Value_x2)
    # print("------------------------------------------------------------------------------------------")


main()
