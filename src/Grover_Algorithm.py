from qiskit import QuantumCircuit

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Step 1: Initialize qubits in superposition
qc.h([0, 1])  # Apply Hadamard gates to both qubits

# Step 2: Oracle (marking the state |11>)
qc.cz(0, 1)  # Apply a controlled-Z gate

# Step 3: Diffusion Operator (inversion about the mean)
qc.h([0, 1])  # Apply Hadamard gates again
qc.x([0, 1])  # Apply Pauli-X gates
qc.cz(0, 1)   # Another controlled-Z gate
qc.x([0, 1])  # Apply Pauli-X gates again
qc.h([0, 1])  # Final Hadamard gates

# Step 4: Measure all qubits
qc.measure_all()

# Print the quantum circuit
print("Grover's Algorithm Circuit:")
print(qc)
