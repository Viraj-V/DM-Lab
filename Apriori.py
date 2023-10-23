def generate_candidates(prev_freq_itemsets, k):
    candidates = []
    
    for i in range(len(prev_freq_itemsets)):
        for j in range(i + 1, len(prev_freq_itemsets)):
            itemset1, _ = prev_freq_itemsets[i]
            itemset2, _ = prev_freq_itemsets[j]
            
            if itemset1[:-1] == itemset2[:-1]:
                new_itemset = sorted(list(set(itemset1) | set(itemset2)))
                candidates.append((new_itemset, 0))
    
    return candidates


def calculate_support(itemset, transactions):
    count = 0
    for transaction in transactions:
        if all(item in transaction for item in itemset):
            count += 1
    support = count / len(transactions)
    return support


def apriori(transactions, min_support):
    items = set()
    for transaction in transactions:
        items.update(transaction)
    
    freq_itemsets = [([item], 0) for item in items]
    final_freq_itemsets = []
    
    k = 2
    while freq_itemsets:
        candidates = generate_candidates(freq_itemsets, k)
        freq_itemsets = []
        
        for candidate, _ in candidates:
            support = calculate_support(candidate, transactions)
            if support >= min_support:
                freq_itemsets.append((candidate, support))
        
        final_freq_itemsets.extend(freq_itemsets)
        k += 1
    
    return final_freq_itemsets


# Provided transaction data
transactions = [
    ['A', 'B', 'C'],
    ['B', 'C'],
    ['C', 'D', 'E', 'F'],
    ['A', 'B', 'E'],
    ['A', 'C', 'D'],
    ['A', 'B', 'D'],
    ['E', 'C'],
    ['C', 'D', 'E', 'F'],
    ['A', 'D', 'E'],
    ['A', 'E', 'D']
]

min_support = 0.3
frequent_itemsets = apriori(transactions, min_support)

# Print frequent itemsets
print("Frequent Itemsets:")
for itemset, support in frequent_itemsets:
    print(f"{itemset}: {support:.2f}")