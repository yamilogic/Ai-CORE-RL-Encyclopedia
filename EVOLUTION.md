# The Encyclopedia of Reinforcement Learning: Evolutionary Timeline

Welcome to the definitive map of AI Intelligence. This document tracks the evolution of Reinforcement Learning from its mathematical foundations to the modern "World Models" that power autonomous civilizations.

## 🏆 Legend of Tags
- 🚀 **Breakthrough**: A paradigm shift in how AI learns.
- 🏛️ **Foundational**: The bedrock upon which all modern RL is built.
- 🏭 **Industry-Standard**: Trusted by engineers in production systems.
- 👑 **SOTA (State-of-the-Art)**: Current record-breaker in performance.
- 🛡️ **Robust-Safety**: Designed to never fail in dangerous real-world tasks.
- 🧬 **Bio-Inspired**: Mimicking the neural structures of animals and insects.
- 🌐 **Distributed-Scale**: Harnessing thousands of computers simultaneously.
- 🧠 **Meta-Learning**: AI that "Learns how to Learn" faster.
- 🔮 **Model-Based**: AI that "Dreams" and plans in its own imagination.
- 📜 **Off-Policy-Expert**: Learning from historical logs and human data.
- 🤝 **Multi-Agent-Coop**: Swarms and teams working together.
- 🎯 **Goal-Conditioned**: Mastering thousands of tasks with one brain.
- 🔍 **Unsupervised-Discovery**: Finding skills without any human rewards.
- 🔌 **Hardware-Silicon**: Designing the next generation of computer chips.
- 🏥 **Healthcare-Applied**: Saving lives through optimized medical logic.

---

## ⏳ The Evolutionary Timeline (Oldest to Newest)

| Algorithm | Year | Creator | Key Innovation | Tags | Lineage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Value Iteration** | 1957 | Richard Bellman | Dynamic Programming & Bellman Equation | 🏛️ | Bellman -> Q-Learning |
| **Q-Learning** | 1989 | Chris Watkins | Model-free learning from experience | 🏛️ 🚀 | Q-Learning -> DQN |
| **REINFORCE** | 1992 | Ronald Williams | Direct Policy Gradients | 🏛️ | REINFORCE -> PPO |
| **SARSA** | 1994 | Rummery & Niranjan | On-policy temporal difference learning | 🏛️ | SARSA -> Expected SARSA |
| **NEAT** | 2002 | Kenneth Stanley | Evolving neural network topologies | 🧬 | NEAT -> HyperNEAT |
| **DQN** | 2013 | DeepMind (Mnih) | Deep Learning + RL (Atari Master) | 🚀 🏛️ | Q-Learning -> DQN -> Rainbow |
| **TRPO** | 2015 | John Schulman | Trust Regions for stable updates | 🚀 | REINFORCE -> TRPO -> PPO |
| **DDPG** | 2015 | Google DeepMind | Continuous control for robotics | 🏛️ 🏭 | Actor-Critic -> DDPG -> TD3 |
| **A3C** | 2016 | DeepMind (Mnih) | Asynchronous parallel actors | 🌐 | DQN -> A3C -> IMPALA |
| **PPO** | 2017 | OpenAI (Schulman) | Robust, stable, easy-to-use policy gradients | 🚀 🏭 | TRPO -> PPO -> PPG |
| **Rainbow DQN** | 2017 | DeepMind (Hessel) | Combining 7 different improvements | 👑 | DQN -> Rainbow |
| **SAC** | 2018 | Berkeley (Haarnoja) | Entropy maximization for robust exploration | 🚀 👑 | DDPG -> SAC |
| **TD3** | 2018 | Scott Fujimoto | Fixing overestimation in DDPG | 🏭 | DDPG -> TD3 |
| **MuZero** | 2019 | DeepMind | Learning a world model without pixels | 🚀 🔮 | AlphaZero -> MuZero |
| **CURL** | 2020 | Laskin et al. | Contrastive learning for visual RL | 🔍 | Unsupervised -> CURL |
| **Offline RL (CQL)** | 2020 | Sergey Levine | Learning from static datasets safely | 📜 🛡️ | Q-Learning -> CQL |
| **Decision Transformer** | 2021 | Chen et al. | RL as Sequence Modeling (GPT style) | 🚀 🎯 | Transformers -> DT |
| **Dreamer V3** | 2023 | Danijar Hafner | Scaling World Models to any environment | 👑 🔮 | PlaNet -> Dreamer -> V3 |

---

## 🗺️ The Evolution Paths (Lineage)

### 1. The "Deep Q" Path (DQN Family)
`Q-Learning (1989)` ⮕ `DQN (2013)` ⮕ `Double DQN` ⮕ `Dueling DQN` ⮕ `PER` ⮕ `Rainbow (2017)` ⮕ `QR-DQN` ⮕ `IQN`

### 2. The "Policy Gradient" Path (Actor-Critic)
`REINFORCE (1992)` ⮕ `VPG` ⮕ `A2C / A3C` ⮕ `TRPO (2015)` ⮕ `PPO (2017)` ⮕ `Phasic Policy Gradient (2020)`

### 3. The "Robot Control" Path (Deterministic)
`LQR` ⮕ `DDP (1966)` ⮕ `DDPG (2015)` ⮕ `TD3 (2018)` ⮕ `SAC (2018)` ⮕ `TD-MPC (2022)`

### 4. The "Planning & Dreams" Path (World Models)
`Dyna-Q (1990)` ⮕ `Value Iteration Networks` ⮕ `PlaNet` ⮕ `Dreamer (2019)` ⮕ `MuZero (2019)` ⮕ `Dreamer V3 (2023)`

### 5. The "Imitation & Logs" Path (Expert Learning)
`Behavior Cloning` ⮕ `GAIL (2016)` ⮕ `AIRL` ⮕ `BCQ` ⮕ `CQL (2020)` ⮕ `IQL (2022)`

---

## 📁 Repository Organization

All algorithms are grouped into **Evolutionary Collections** (~20 folders each). Each collection represents a specific era or branch of AI development.

- **Collection_01_Foundations**: 1950s - 2010. Basic Q-learning, SARSA, Bellman.
- **Collection_02_Deep_Beginnings**: 2013-2015. Original DQN, DDPG, TRPO.
- **Collection_03_Scaling_Stability**: 2016-2018. PPO, A3C, Rainbow, SAC.
- **Collection_04_Modern_Frontiers**: 2019-Present. MuZero, Dreamer, Decision Transformers.
- **Collection_05_Specialized_Applied**: Applied RL for Bio, Chip Design, and Medicine.
- **Collection_40_The_Final_Frontier_2026**: The cutting edge of 2025-2026. World Models, Quantum RL, and the Singularity.

---
> [!IMPORTANT]
> This repository is designed for **Educational Purposes**. It is a library of "Core Implementations" intended to help researchers and students understand the mathematical soul of every major AI breakthrough.
