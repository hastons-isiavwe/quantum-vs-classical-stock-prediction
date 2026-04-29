import random

def generate_stock_data(output_file="stock_data.txt", days=365):
    """
    Generates daily stock price percentage changes and displays them.

    Parameters:
    - output_file: Name of the output file to save the stock data.
    - days: Number of days to simulate.
    """
    # Generate random percentage changes
    percentage_changes = [
        round(random.uniform(-100.00, 100.00), 2) for _ in range(days)
    ]
    
    # Display the data
    print("Generated Stock Data (First 10 Days):")
    print("\n".join(f"Day {i + 1}: {change:+.2f}%" for i, change in enumerate(percentage_changes[:10])))
    print("\n... (Data continues, full data saved to file)\n")
    
    # Write to file
    with open(output_file, 'w') as file:
        file.writelines(f"{change:+.2f}\n" for change in percentage_changes)

    print(f"Generated stock data written to '{output_file}'.")
    return percentage_changes

# Generate the stock data
generate_stock_data()

print("program finish")