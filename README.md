# Q-Racing: Superposition Sprint
A quantum-mechanical racing simulation where navigation is determined by state probabilities rather than classical coordinates. Players must manage their quantum state to navigate "Superposition Lanes" and survive environmental decoherence.

🕹️ Game Mechanics: The game operates on a 3-Lane System mapped to the probability amplitudes of a 2-qubit system.

The Quantum Vehicle: Your "position" is a state vector $|\psi\rangle$. Your presence in a lane is determined by the probability $P(i) = |\langle i|\psi\rangle|^2$.

Superposition Maneuver: By applying a Hadamard (H) gate, you split your vehicle across multiple lanes. This allows you to "scout" safe paths or bypass narrow obstacles. 

Environmental Measurement: Periodically, the track features "Observer Gates." These force a measurement ($M$) on your state, collapsing your vehicle into a single lane based on your current amplitudes.

Decoherence Hazards: Passing through "Noise Clouds" applies random Pauli-X (bit-flip) or Phase-flip operations, potentially knocking you into an obstacle lane.

🛠 How to Play

Initialize: Start in the $|00\rangle$ state (Center Lane).
Navigate: Use keyboard shortcuts to apply gates in real-time
:H: Enter Superposition (spread across lanes).
X: Shift lanes (Flip state).
Z: Phase shift (protects against certain interference hazards).

Observation: When you hit a Measurement Line, the screen will flash, and your "ghost" versions will collapse into one solid vehicle.

Avoid Obstacles: If your collapsed position overlaps with a "Classical Wall," you lose Fidelity (HP).🏆 
Win Conditions
Primary: Reach the finish line with Fidelity > 0.5.
Secondary: Highest "Quantum Score" — calculated by the complexity of the gates used to successfully avoid obstacles.
