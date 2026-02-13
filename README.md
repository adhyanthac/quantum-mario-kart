# 🏎️ QUANTUM MARIO KART

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![React](https://img.shields.io/badge/Frontend-React-blue)](https://reactjs.org/)
[![Python](https://img.shields.io/badge/Backend-FastAPI-green)](https://fastapi.tiangolo.com/)

**Quantum Mario Kart** is a high-speed, educational racing game that gamifies the core principles of quantum mechanics. Inspired by the chaotic fun of Mario Kart and the complex reality of quantum physics, players race against time and probability itself.

---

## 🌟 THE CONCEPT

You are piloting a prototype **Quantum Kart**. Unlike normal karts, this vehicle can exist in a **superposition of states**. This means you can drive in two lanes at the same time!

The track is filled with deadly lasers. To survive for the full 60 seconds, you must master:
1.  **Classical Dodging**: Moving left/right like a normal racer.
2.  **Quantum Superposition**: Splitting your reality to "tunnel" through unavoidable obstacles with probability on your side.

---

## 🎮 GAMEPLAY MECHANICS

### 1. Classical Mode (Default)
- You control a single, solid kart.
- Use **`A`** and **`D`** to switch lanes.
- If you hit a laser, you crash. Game Over.
- Best for dodging single lasers in open lanes.

### 2. Quantum Mode (Superposition)
- Press **`H`** (Hadamard Gate) to enter Quantum Mode.
- Your kart splits into two semi-transparent "Ghost Karts" (Universe α and Universe β).
- **Entanglement**: These two ghosts are linked. Moving one affects the probability of where you *actually* are.
- **Tunneling**: If a laser is blocking one lane, you can stay in superposition. When you pass the laser, the game "measures" your position.
    - If you are lucky (based on your probability), you collapse into the safe lane and survive!
    - If you are unlucky, you collapse into the laser and crash.

### 3. Probability Management
- In Quantum Mode, you'll see percentage numbers (e.g., **L: 80% | R: 20%**).
- This is the chance that you exist in that lane.
- **Strategy**: Always try to maximize your probability in the *safe* lane before passing a laser!

### 4. Winning
- Survive for **60 seconds**.
- Watch the **Rocket Progress Bar** at the bottom of the screen to track your journey through the quantum realm.

---

## 🕹️ CONTROLS

| Key | Action | Description |
| :---: | :--- | :--- |
| **H** | **Quantum Mode** | Toggles Superposition. Uses a *Hadamard Gate* to split your wave function. |
| **A / D** | **Classic Move / Universe α** | Moves your kart (Classical) OR shifts probability for Ghost α (Quantum). |
| **← / →** | **Universe β Control** | Only works in Quantum Mode. Shifts probability for Ghost β. |
| **L** | **Swap Laser** | Teleports the incoming laser to the opposite universe. A tactical power-up! |
| **P** | **Pause** | Freezes the simulation. |

> **Pro Tip:** If a laser is coming on the Left in Universe A, but the Right is clear in Universe B... use **Standard Mode** to dodge if possible, or **Quantum Mode** to gamble with probabilities!

---

## 🖥️ USER INTERFACE GUIDE

- **Rocket Progress Bar (Bottom)**: Shows how close you are to finishing the 60-second race.
- **Floating Text (Right Side)**: stylized messages like "NICE!", "QUANTUM TUNNEL!" pop up when you successfully dodge or tunnel through obstacles.
- **Q-Bit HUD**: Displays the current probability amplitude of your kart in each lane.
- **Combo Meter**: Builds up as you chain successful dodges in Quantum Mode.

---

## ⚙️ INSTALLATION & SETUP

This game consists of two parts: a **Python Backend** (simulation) and a **React Frontend** (visuals). You must run BOTH for the game to work.

### Prerequisites
- [Node.js](https://nodejs.org/) (v14 or higher)
- [Python](https://www.python.org/) (v3.8 or higher)

### Step 1: Start the Backend 🐍
The backend runs the quantum simulation.

1.  Open a terminal/command prompt.
2.  Navigate to the `backend` folder:
    ```bash
    cd backend
    ```
3.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    .\venv\Scripts\activate   # Windows
    # source venv/bin/activate # Mac/Linux
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Start the server:
    ```bash
    uvicorn main:app --reload
    ```
    *You should see: `Uvicorn running on http://127.0.0.1:8000`*

### Step 2: Start the Frontend ⚛️
The frontend is the game window you play in.

1.  Open a **NEW** terminal window.
2.  Navigate to the `frontend` folder:
    ```bash
    cd frontend
    ```
3.  Install dependencies (first time only):
    ```bash
    npm install
    ```
4.  Launch the game:
    ```bash
    npm start
    ```
    *The game will automatically open in your browser at `http://localhost:3000`.*

---

## 🛠️ TROUBLESHOOTING

- **"WebSocket connection failed"**:
    - Make sure the backend terminal is running and says `Uvicorn running...`.
    - Check if port 8000 is already in use.
- **"Module not found" (Python)**:
    - Ensure you activated your virtual environment (`venv`) before running `uvicorn`.
    - Ensure you ran `pip install -r requirements.txt`.
- **Game runs slow**:
    - Reduce the "Game Speed" in the Settings menu (Gear icon).

---

## ⚛️ THE SCIENCE BEHIND IT

This game simulates a real **Quantum Circuit**:
- **Qubits**: Represents your car's position (0 = Left, 1 = Right).
- **H-Gate (Hadamard)**: Creates superposition (splitting the car).
- **X-Gate (Pauli-X)**: Flips the state (switching lanes).
- **Measurement**: Observing the car (hitting a laser) collapses the state to a single position based on probability amplitudes.

---
*Created for the Quantum Racing Project. Enjoy the ride!* 🚀
