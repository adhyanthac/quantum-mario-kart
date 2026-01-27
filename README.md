Quantum Race: Superposition Sprint
A quantum-mechanical navigation game developed for the Xu Research Group. Instead of classical steering, players manipulate a wave function to navigate a field of obstacles and environmental noise.

Project Overview
You control a quantum vehicle existing in a superposition of four lanes. Your goal is to reach the finish line by managing your probability amplitudes using quantum gates, avoiding Decoherence Crashes with classical obstacles.

Detailed Game Mechanics
1. The State Vector
Your position is defined by a 4-element state vector representing your presence in each lane.

Superposition (H Gate): Splitting your vehicle into two Ghost Cars. This allows you to occupy multiple lanes but increases the risk of being measured in the wrong spot.

Bit-Flip (X Gate): Shifting your entire probability distribution across the lanes.

2. Environmental Hazards
Obstacles: Classical walls. If any part of your Ghost Car (probability > 0) hits a wall, you risk a crash.

Noise Regions: Purple zones that simulate Decoherence. Passing through these randomizes your state vector, potentially throwing you into an obstacle.

Measurement Lines: Yellow Observer gates that force your wave function to collapse into a single lane based on your current probabilities.

3. Scoring and Win Conditions
Primary Condition: Reach the finish line (Distance = 0m) without crashing.

Secondary Condition (Quantum Efficiency): A qualitative score based on how optimized your quantum moves were.

High Score: Successfully using H to dodge an obstacle and collapsing back to a stable state.

Low Score: Excessive gate use or staying in unnecessary superposition.

Instructions for Use
Requirements: Ensure pygame is installed (pip install pygame).

Controls:

X: Apply X-Gate (Shift lanes).

H: Apply Hadamard-Gate (Enter/Exit Superposition).

Space: Manual Measurement (Collapse into one lane).
Observation: When you hit a Measurement Line, the screen will flash, and your "ghost" versions will collapse into one solid vehicle.

Avoid Obstacles: If your collapsed position overlaps with a "Classical Wall," you lose Fidelity (HP).🏆 
Win Conditions
Primary: Reach the finish line with Fidelity > 0.5.
Secondary: Highest "Quantum Score" — calculated by the complexity of the gates used to successfully avoid obstacles.
