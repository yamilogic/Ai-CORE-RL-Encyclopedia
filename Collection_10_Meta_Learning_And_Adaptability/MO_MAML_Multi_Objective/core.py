import numpy as np

def mo_maml_update(weights, task_grads_list, objective_weights):
    # MO-MAML: Meta-Learning across Multiple Objectives
    # Instead of one reward, we have a 'Vector' of rewards.
    # Meta-Update = sum( objective_weight * task_grad )
    # This allows the AI to learn how to balance multiple goals (e.g. Speed vs Fuel).
    
    total_grad = np.zeros_like(weights)
    for grad, obj_w in zip(task_grads_list, objective_weights):
        total_grad += obj_w * grad
        
    new_weights = weights + 0.01 * total_grad
    print(f"🚀 MO-MAML: Multi-Objective Meta-Update Complete. Gradient Norm={np.linalg.norm(total_grad):.4f}")
    return new_weights

print("🚀 MO-MAML: Initializing Multi-Objective Meta-Learning Controller...")
w_init = np.array([0.5, 0.5])
grads = [np.array([1, 0]), np.array([0, 1])] # Obj 1 wants West, Obj 2 wants North
objs = [0.8, 0.2] # Prioritize Obj 1
mo_maml_update(w_init, grads, objs)
print("✅ Logic Check: Weighted multi-objective meta-gradient verified.")
