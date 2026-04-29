def simulate_stock_performance(input_file="stock_data.txt", initial_price=200, budget=10_000):
    """
    Simulates stock performance, calculates portfolio value, and provides advice on whether to buy shares.

    Parameters:
    - input_file: File containing the daily percentage changes.
    - initial_price: Starting price of the stock.
    - budget: Initial budget for buying shares.
    """
    # Read data
    with open(input_file, 'r') as file:
        percentage_changes = [float(line.strip()) for line in file.readlines()]
    
    shares_owned = 0
    results = []

    # Simulate using 90-day rolling window
    for day in range(0, len(percentage_changes), 90):
        # Calculate average percentage change over the window
        window = percentage_changes[day:day + 90]
        avg_change = sum(window) / len(window)
        predicted_price = initial_price * (1 + avg_change / 100)

        # Decision logic
        if predicted_price <= 67:
            shares_to_buy = 0
            advice = "Predicted price is too low. Avoid buying shares."
        elif predicted_price <= 200:
            shares_to_buy = 150
            advice = "Predicted price is moderate. Consider buying shares."
        else:
            shares_to_buy = 50
            advice = "Predicted price is high. Buy cautiously."

        cost = shares_to_buy * predicted_price

        # Update portfolio based on budget
        if cost > budget:
            affordable_shares = int(budget // predicted_price)
            shares_to_buy = min(shares_to_buy, affordable_shares)
            cost = shares_to_buy * predicted_price

        if shares_to_buy > 0:
            budget -= cost
            shares_owned += shares_to_buy
            results.append(
                f"Day {day + 90}: Bought {shares_to_buy} shares at ${predicted_price:.2f}. Remaining budget: ${budget:.2f}. {advice}"
            )
        else:
            results.append(
                f"Day {day + 90}: Not enough budget to buy shares. Predicted Price: ${predicted_price:.2f}. {advice}"
            )

        initial_price = predicted_price

    # Final portfolio value
    final_value = shares_owned * initial_price + budget
    results.append(f"Final Portfolio Value: ${final_value:.2f}")
    print("\n".join(results))
    return final_value

# Simulate stock performance
simulate_stock_performance()
