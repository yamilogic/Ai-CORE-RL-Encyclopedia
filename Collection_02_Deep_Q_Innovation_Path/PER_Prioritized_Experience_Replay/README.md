# PER (Prioritized Experience Replay)

🧠 **What does this do? (The Analogy)**
Think of a **Student studying for a Final Exam**. 
- They have 1,000 flashcards. 
- 900 of them are easy ("What is 1+1?"). 
- 100 of them are very hard ("Explain Quantum Entanglement"). 
If the student picks flashcards randomly, they waste 90% of their time on things they already know. **PER** is a student who puts the "Hard" flashcards at the top of the pile and reviews them 10x more often. By focusing on the "Surprising" or "Difficult" memories, the AI learns much faster.

🔍 **Step-by-Step Explanation:**
1. **TD Error**: Every time the AI learns, it calculates how "wrong" it was (Temporal Difference Error).
2. **Priority**: Experiences with a **High Error** (where the AI was very surprised) are given a high priority.
3. **Biased Sampling**: When it's time to "Replay" memories, the AI is much more likely to pick the high-priority ones.
4. **Benefit**: It solves the "Redundant Data" problem. In many games, 90% of the movement is just "walking in a straight line" (Boring). PER ensures the AI spends its time learning about the rare "Boss Battles" instead.

📊 **High-Level Design (HLD)**

```mermaid
graph TD
    A[Experience Buffer: 1,000,000 Memories] --> B[Calculate Surprise: |TD-Error|]
    B --> C[Rank Memories by Surprise]
    C --> D[Training Loop]
    D -- "Sample 32 Memories" --> E[Memory Index #42: HIGH SURPRISE]
    E -- "Update Weights" --> D
```

✅ **Why use this?**
It is one of the **Standard Components of Rainbow DQN**. It is one of the most effective "Stability and Speed" upgrades you can give to any Q-Learning agent.

🌍 **Real-World Examples:**
1. **Financial Fraud Detection**: Focusing training on the 0.01% of transactions that are actually fraud, rather than the 99.9% that are normal.
2. **Autonomous Driving Edge-Cases**: Spending more time learning from "Near-accidents" than from "Driving on a quiet highway."
