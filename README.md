# 🚀 Traveling Salesman Problem Solver using Genetic Algorithm
This project implements a **Genetic Algorithm (GA) based approach** to solve the **Traveling Salesman Problem (TSP)**, which finds the shortest possible route visiting a set of cities exactly once and returning to the starting point.

## 📌 Features
- **Optimized Path Calculation** using Genetic Algorithm
- **Visualization of the Best Route** using Matplotlib
- **Configurable Parameters**: Population size, generations, mutation rate
- **Randomly Generated Cities**

## 📂 Project Structure
```
Genetic_Algorithm/
├── README.md                   # Project Documentation
├── requirements.txt             # Dependencies
│
├── tsp_ga/                      # Core Package
│   ├── genetic_algorithm.py     # GA Implementation
│   ├── visualization.py         # Route Visualization
│
├── main.py                      # Entry Point: Runs the Solver & Visualization
```

## 🏙️ Cities Dataset
- The cities are **randomly generated** in a 2D plane.
- Users specify the **number of cities** before execution.

## 🚀 Installation & Usage
### 🔹 1️⃣ Clone the Repository
```bash
git clone https://github.com/salvabehnam/Genetic_Algorithm.git
cd TSP_GA_Project
```
### 🔹 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 🔹 3️⃣ Run the Solver
```bash
python main.py
```
- The program will prompt you for the **number of cities**.
- It will compute the **best route** and **visualize it**.

## 📊 Results & Performance
- The algorithm finds an **efficient route** using **Genetic Algorithms**.
- The best route is displayed **graphically** using Matplotlib.
- **Faster and more scalable** than brute-force methods.

## ✨ Technologies Used
- **Python**
- **NumPy** (Distance Calculation)
- **Matplotlib** (Route Visualization)
- **Genetic Algorithm** (Selection, Crossover, Mutation)

