# backend/logic/splitter.py

def equal_split(amount, users):
    per_head = amount // len(users)
    return {u: per_head for u in users}


def ratio_split(amount, ratio_dict):
    total_ratio = sum(ratio_dict.values())
    split_result = {}
    for user, r in ratio_dict.items():
        split_result[user] = (amount * r) // total_ratio
    return split_result
