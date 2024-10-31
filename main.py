import random;
import matplotlib.pyplot as plt

def throwTwoDice(rounds):
    #Tossing a dice
    
    inv_list = []

    for _ in range(rounds):
        random_number1 = random.randint(1,6)
        random_number2 = random.randint(1,6)
        sum = sumOfDices(random_number1,random_number2)
        inv_list.append([random_number1, random_number2, sum])
    
    #Finally, I created an array which contains both of the dice values and the summation.
    #To reach the summation, I can basically take the third element for each round. 


    return inv_list

def sumOfDices(number1,number2):
    return (number1+number2)


def x_inv(x,DiceValues,size):

    results = []

    #At this for loop we are looking for the matched value into our array with our desired value x
    #If the summation of two dices values are equal to X value, then save the pre image values of that spesific values.
  
    for i in range(size):
        if DiceValues[i][2] == x:
            results.append([DiceValues[i][0],DiceValues[i][1]])
    
    return results

def get_expected_value(x):
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

def prob(desired_value_length,size):
    
    return desired_value_length/size


def Expected_Value(DiceValues, size):
    total_sum_dice1 = 0
    total_sum_dice2 = 0
    
    for roll in DiceValues:
        total_sum_dice1 += roll[0]  
        total_sum_dice2 += roll[1]  
    
    expected_value_die1 = total_sum_dice1 / size
    expected_value_die2 = total_sum_dice2 / size
    
    return expected_value_die1, expected_value_die2

def plot_dice_sums_histogram(sums):
    plt.hist(sums, bins=range(2, 14), edgecolor="black", align="left")
    plt.title("Distribution of Dice Sums")
    plt.xlabel("Sum of Two Dice")
    plt.ylabel("Frequency")
    plt.xticks(range(2, 13))
    plt.show()

def plot_expected_values(expected_value_die1, expected_value_die2):
    plt.bar(['Dice 1', 'Dice 2'], [expected_value_die1, expected_value_die2], color=['blue', 'orange'])
    plt.title("Expected Value of Each Dice")
    plt.xlabel("Dice")
    plt.ylabel("Expected Value")
    plt.ylim(3, 4)  
    plt.show()


def main():
   
    size = 500000
    x = 8 #Desired summation equivelent.

    DiceValues = throwTwoDice(size)
    x_preimages = x_inv(x,DiceValues,size) 
    Possibility_Of_X = prob(len(x_preimages),size)
    x_expected = get_expected_value(x)
    sums = [roll[2] for roll in DiceValues]
    Expected_Value_x1,Expected_Value_x2 = Expected_Value(DiceValues,size)


    print(DiceValues)
    print("------------------------------------------------------------------------------------------")
    print(x_preimages)
    print(len(x_preimages))
    print("------------------------------------------------------------------------------------------")
    print(f"Theoric value of picking the number: {x_expected:.3f}")
    print(Possibility_Of_X)
    plot_dice_sums_histogram(sums)
    print("------------------------------------------------------------------------------------------")
    print("Expected value of one dice is : 3.5")
    print(Expected_Value_x1)
    print(Expected_Value_x2)
    plot_expected_values(Expected_Value_x1, Expected_Value_x2)
    print("------------------------------------------------------------------------------------------")



main()
