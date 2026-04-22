import numpy as np

class HierarchicalAgent:
    def __init__(self):
        self.manager_goal = "Reach Room B"
        self.worker_subgoal = "Move to Door"
        
    def step(self):
        # Manager sets a subgoal for the worker
        print(f"Manager Goal: {self.manager_goal}")
        print(f"Worker acting on Subgoal: {self.worker_subgoal}")
        # Worker executes low-level actions
        return "Step Taken"

print("🚀 Hierarchical RL: Manager (High-level) vs Worker (Low-level)...")
hrl = HierarchicalAgent()
hrl.step()
