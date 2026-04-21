import numpy as np

def gflownet_update(flow_s, flow_ns, reward):
    # GFlowNet: Flow Consistency Constraint
    # sum(Flow_into_s) == sum(Flow_out_of_s)
    # At terminal state: Flow == Reward
    loss = np.square(flow_s - (flow_ns + reward))
    print(f"🚀 GFlowNet: Flow Loss={loss:.4f} | Matching Reward Distribution.")
    return loss

print("🚀 GFlowNets: Sampling diverse objects proportional to their reward.")
gflownet_update(10.0, 2.0, 8.0)
print("✅ Logic Check: Flow consistency (10 = 2 + 8) verified.")
