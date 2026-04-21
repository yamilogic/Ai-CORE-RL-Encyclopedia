# TarMAC (Targeted Multi-Agent Communication)

🧠 **What does this do? (The Analogy)**
Think of a **Person shouting 'Is there a doctor in the house?'**. 
- 100 people hear the shout. 
- 99 people (The Non-Doctors) ignore it because it's not "targeted" to them. 
- 1 person (The Doctor) "Attends" to the message and rushes to help. 
- **TarMAC** is an AI communication protocol where agents don't just "talk"—they "tag" their messages. 
- Only the agents who have a "matching tag" (interest) will listen and react. This prevents a large team of robots from being "distracted" by messages that don't concern them.

🔍 **Step-by-Step Explanation:**
1. **Signature Generation**: The sender creates a "Signature" (a small vector) along with their message.
2. **Relevance Filtering**: The receiver compares the signature to its own "Need" or "State."
3. **Information Routing**: Only messages with high "Similarity" (Dot Product) are used to update the receiver's brain.
4. **Benefit**: It allows for **Private Conversations** and **Sub-Team Coordination** without a central controller.

📊 **High-Level Design (HLD)**

```mermaid
graph TD
    A[Agent 1: 'Need Backup at (X,Y)'] -- "Signature: SOS-Combat" --> B[Network]
    B -- "Relevance Check" --> C[Agent 2: 'Combat Bot']
    B -- "Relevance Check" --> D[Agent 3: 'Medic Bot']
    C -- "High Relevance: Listen" --> E[Coordinate Backup]
    D -- "Low Relevance: Ignore" --> F[Continue Search]
```

✅ **Why use this?**
It is the best choice for **Heterogeneous Teams** (teams with different types of robots). If you have drones, tanks, and infantry, TarMAC ensures the drones only "talk" to the infantry when there is something the infantry needs to see.

🌍 **Real-World Examples:**
1. **Smart City Sensors**: A "Smoke Detector" only sending an urgent message to the nearest "Fire Truck" and "Water Sprinkler," while the "Street Lights" ignore the data.
2. **Autonomous Taxi Fleet**: One taxi informing only the taxis "on the same street" about a traffic jam, rather than telling the whole city.
