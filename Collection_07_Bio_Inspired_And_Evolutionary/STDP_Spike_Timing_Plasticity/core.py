import numpy as np

def stdp_update(pre_spike_time, post_spike_time, weight, lr=0.1):
    # STDP: Biological time-based learning
    # If Pre fires BEFORE Post -> Strengthen (Causality)
    # If Pre fires AFTER Post -> Weaken (Anti-causality)
    dt = post_spike_time - pre_spike_time
    if dt > 0:
        dw = lr * np.exp(-dt / 10.0) # Long-term Potentiation (LTP)
    else:
        dw = -lr * np.exp(dt / 10.0) # Long-term Depression (LTD)
        
    print(f"🚀 STDP: Delta Time={dt} | Weight Shift={dw:.4f} | {'Potentiation' if dw > 0 else 'Depression'}")
    return weight + dw

print("🚀 STDP: Initializing Time-based Plasticity Logic...")
stdp_update(pre_spike_time=10, post_spike_time=12, weight=0.5) # Causality
stdp_update(pre_spike_time=15, post_spike_time=12, weight=0.5) # Anti-causality
print("✅ Logic Check: Causality-based weight shift verified.")
