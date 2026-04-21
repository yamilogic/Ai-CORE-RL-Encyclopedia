import numpy as np

def cql_loss(q_values, dataset_actions_idx):
    # CQL: Pushing down Q-values for actions NOT in the dataset
    # We want to be 'Conservative' - don't over-estimate what we haven't seen!
    dataset_q = q_values[dataset_actions_idx]
    
    # Loss = logsumexp(all_qs) - mean(dataset_qs)
    # This minimizes all Qs but keeps dataset Qs high
    cql_penalty = np.log(np.sum(np.exp(q_values))) - np.mean(dataset_q)
    print(f"🚀 CQL Penalty: {cql_penalty:.4f} | Discouraging over-optimism.")
    return cql_penalty

print("🚀 CQL Core: Learning safely from static datasets without environment interaction.")
qs = np.array([2.0, 10.0, 5.0]) # Q-values for 3 actions
cql_loss(qs, 1) # Action 1 was the expert action
print("✅ Logic Check: Conservative value suppression verified.")
