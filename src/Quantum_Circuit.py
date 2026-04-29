from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer
import matplotlib.pyplot as plt

# Generate Quantum Data with Advice
def generate_quantum_stock_data(num_days=365, num_qubits=9):
    """
    Generates random percentage changes using quantum principles and gives actionable advice.
    """
    circuit = QuantumCircuit(num_qubits)

    # Apply Hadamard gates for superposition
    for qubit in range(num_qubits):
        circuit.h(qubit)

    # Add entanglement using CNOT gates
    for qubit in range(num_qubits - 1):
        circuit.cx(qubit, qubit + 1)

    # Measure the circuit
    circuit.measure_all()

    # Simulate the circuit
    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)
    result = simulator.run(compiled_circuit, shots=num_days).result()
    counts = result.get_counts()

    # Convert results to percentage changes
    percentage_changes = []
    for outcome, frequency in counts.items():
        decimal_value = int(outcome, 2)
        percent_change = (decimal_value / (2**num_qubits - 1)) * 200 - 100
        percentage_changes.append(round(percent_change, 2))

    # Limit percentage changes to a realistic range (-10% to +10%)
    percentage_changes = [max(min(change, 10.0), -10.0) for change in percentage_changes]

    print("Quantum-generated stock data created. Adjust the range of -10% to +10% for realistic stock behavior.")
    return percentage_changes[:num_days]

# Predict Stock Prices with Advice
def predict_stock_price(percentage_changes, initial_price=200, budget=10_000):
    """
    Simulates stock performance using quantum-generated data and provides actionable advice.
    """
    shares_owned = 0
    results = []

    for day in range(0, len(percentage_changes), 90):
        # Calculate rolling average
        window = percentage_changes[day:day + 90]
        avg_change = sum(window) / len(window)
        predicted_price = max(initial_price * (1 + avg_change / 100), 1)

        if predicted_price <= 67:
            shares_to_buy = 0
            advice = "Price too low. Avoid buying shares."
        elif predicted_price <= 200:
            shares_to_buy = 150
            advice = "Price moderate. Consider buying shares."
        else:
            shares_to_buy = 50
            advice = "Price high. Buy cautiously."

        cost = shares_to_buy * predicted_price

        if cost > budget or shares_to_buy == 0:
            decision = f"Day {day + 90}: Not enough budget or decision to hold. Predicted Price: ${predicted_price:.2f}. {advice}"
        else:
            budget -= cost
            shares_owned += shares_to_buy
            decision = f"Day {day + 90}: Bought {shares_to_buy} shares at ${predicted_price:.2f}. Remaining budget: ${budget:.2f}. {advice}"

        print(decision)
        results.append(decision)
        initial_price = predicted_price

    final_value = shares_owned * initial_price + budget
    results.append(f"Final Portfolio Value: ${final_value:.2f}")
    print("\n".join(results))
    return final_value

# Visualize and Save Gates
def visualize_and_save_gates_with_display():
    """
    Visualizes and saves a quantum circuit with all gates and displays results.
    """
    num_qubits = 9
    circuit = QuantumCircuit(num_qubits)

    # Add gates
    circuit.h(range(num_qubits))  # Hadamard gates
    circuit.cx(0, 1)  # CNOT gate
    circuit.x(2)  # Pauli-X gate
    circuit.y(3)  # Pauli-Y gate
    circuit.z(4)  # Pauli-Z gate
    circuit.measure_all()  # Measurement gates

    # Draw and display the circuit
    print("Displaying and saving quantum circuit with all gates...")
    circuit_diagram = circuit_drawer(
        circuit,
        output="mpl",
        style={"displaycolor": {
            "h": "#FFA500", "cx": "#00BFFF", "x": "#FF4500", "y": "#8A2BE2", "z": "#32CD32", "measure": "#FFD700"
        }}
    )
    plt.title("Quantum Circuit With All Gates")
    plt.savefig("Quantum_Circuit.png")
    plt.show()

    # Simulate and plot histogram
    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)
    result = simulator.run(compiled_circuit, shots=1000).result()
    counts = result.get_counts()

    print("Displaying and saving histogram of quantum results...")
    plot_histogram(counts, color="#8A2BE2")
    plt.title("Quantum Histogram")
    plt.savefig("Quantum_Histogram.png")
    plt.show()

# Main Functionality
if __name__ == "__main__":
    # Generate quantum data
    quantum_data = generate_quantum_stock_data()

    # Predict stock prices
    final_portfolio_value = predict_stock_price(quantum_data)
    print(f"\nFinal Portfolio Value (Quantum): ${final_portfolio_value:.2f}")

    # Visualize and save quantum circuit with all gates
    visualize_and_save_gates_with_display()
