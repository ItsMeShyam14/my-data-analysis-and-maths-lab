# States and Actions of the Recycling Robot
# Coded by Shyam Sunder S

# Globally defined probabilities
alpha = 0.80 # Finding a can while seeking
beta = 0.40 # FInding a can while waiting

states = {
        "LOW": 0,
        "HIGH": 1
}
actions = {
        "RECHARGE": 0,
        "WAIT": 1,
        "SEEK": 2
}
probabilities = { # Probability of state transition given a state and an action
        ("LOW", "RECHARGE"): [("LOW", 0.00), ("HIGH", 1.00)],
        ("LOW", "WAIT"): [("LOW", 0.90), ("HIGH", 0.10)],
        ("LOW", "SEEK"): [("LOW", 0.80), ("HIGH", 0.20)],
        ("HIGH", "WAIT"): [("LOW", 0.10), ("HIGH", 0.90)],
        ("HIGH", "SEEK"): [("LOW", 0.30), ("HIGH", 0.70)]
}

rewards = {
        ("LOW", "RECHARGE", "HIGH"): 0.00,
        ("LOW", "WAIT", "LOW"): beta,
        ("LOW", "WAIT", "HIGH"): beta - 3, # Recharging reward of -3
        ("LOW", "SEEK", "LOW"): alpha,
        ("LOW", "SEEK", "HIGH"): alpha - 3,
        ("HIGH", "WAIT", "LOW"): beta,
        ("HIGH", "WAIT", "HIGH"): beta,
        ("HIGH", "SEEK", "LOW"): alpha,
        ("HIGH", "SEEK", "HIGH"): alpha
}
