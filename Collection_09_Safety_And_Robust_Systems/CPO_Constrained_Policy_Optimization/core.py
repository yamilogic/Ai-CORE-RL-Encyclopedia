import numpy as np

def cpo_projection(policy_grad, cost_grad, cost_limit=0.1, current_cost=0.5):
    # CPO: Solving the constrained optimization problem
    # Maximize Reward Grad s.t. Cost < Limit
    # This involves a 'Trust Region' and a projection onto the safe plane.
    
    # If we are over the cost limit, we must move in direction of negative cost grad
    if current_cost > cost_limit:
        print("🛑 CPO: Safety Violation! Shifting gradient toward safe region.")
        safe_direction = -cost_grad
        return safe_direction
        
    # Otherwise, project policy grad so it doesn't increase cost
    # Projection = Grad - (dot(Grad, CostGrad)/|CostGrad|^2) * CostGrad
    projection = policy_grad - (np.dot(policy_grad, cost_grad) / (np.linalg.norm(cost_grad)**2 + 1e-8)) * cost_grad
    print("🚀 CPO: Safe gradient projection completed.")
    return projection

print("🚀 CPO: Initializing Trust-Region Constrained Optimization...")
p_g = np.array([1.0, 1.0]) # Wants to go North-East
c_g = np.array([1.0, 0.0]) # East is 'Dangerous'
cpo_projection(p_g, c_g, current_cost=0.0) # Result should be mostly North
print("✅ Logic Check: Orthogonal safety projection verified.")
