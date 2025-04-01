##
# Michael Ghattas
# COMP 4581 - Assignment 3
# Mar/8/2025
##



import pandas as pd
import numpy as np

def loadInvestments(investmentFilename):
    """
    Load investment data from the CSV file and prepare a list of investment options.
    
    Parameters:
        investmentFilename (str): The path to the CSV file containing investment data.
        
    Returns:
        list: A list of tuples (InvestmentName, InvestmentCost, EstimatedReturnOnInvestment).
    """

    # Load CSV file, skipping the first row (United States aggregate data)
    df = pd.read_csv(investmentFilename, skiprows=[1])
    
    # Standardize column names by stripping spaces
    df.columns = df.columns.str.strip()
    
    # Identify the correct '10-year return' column dynamically
    return_column = [col for col in df.columns if '10' in col.lower() and 'year' in col.lower()]
    if not return_column:
        raise KeyError("Could not find a valid '10-year return' column in CSV")
    return_column = return_column[0]  # Use detected column
    
    # Extract required columns
    investments = []
    for _, row in df.iterrows():
        investment_name = row['RegionName']  # State name
        investment_cost = row['Zhvi']  # Average home price
        estimated_return = row[return_column] * investment_cost / 100  # Convert ratio to percentage return in dollars
        
        investments.append((investment_name, int(investment_cost), int(estimated_return)))
    
    return investments


def optimizeInvestments(investments, budget):
    """
    Optimize the investment selection to maximize the total return using dynamic programming.
    
    Parameters:
        investments (list): List of tuples (InvestmentName, InvestmentCost, EstimatedReturnOnInvestment).
        budget (int): The maximum amount available for investment.
        
    Returns:
        tuple: (max_return, selected_investments)
            max_return (int): The maximum possible return.
            selected_investments (list): List of selected investment names.
    """
    
    num_investments = len(investments)
    
    # Initialize DP table
    dp = np.zeros((num_investments + 1, budget + 1), dtype=int)
    
    # Fill DP table
    for i in range(1, num_investments + 1):
        name, cost, return_on_investment = investments[i - 1]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + return_on_investment)
            else:
                dp[i][b] = dp[i - 1][b]
    
    # Traceback to find selected investments
    selected_investments = []
    b = budget
    for i in range(num_investments, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_investments.append(investments[i - 1][0])  # Add investment name
            b -= investments[i - 1][1]  # Reduce remaining budget
    
    selected_investments.reverse()  # Maintain order
    
    return dp[num_investments][budget], selected_investments

# Example usage (assuming budget = 1,000,000)
investments = loadInvestments("state_zhvi_summary_allhomes.csv")
max_return, selected = optimizeInvestments(investments, 1000000)
print("Maximum Return:", max_return)
print("Selected Investments:", selected)



##
# Note:
# Completion, debugging, and validation of the code was assisted by GenAI/LLMs.
##