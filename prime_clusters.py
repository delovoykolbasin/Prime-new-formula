from collections import defaultdict

def segment_primes_by_lz(primes, lz_clusters, tolerance=1e-4):
    """
    Segment a sorted list of primes into subsequences matching each LZ cluster based on growth ratio.

    Args:
        primes (list or np.array): Sorted sequence of primes.
        lz_clusters (list): Known cluster LZ ratios.
        tolerance (float): Allowed deviation to assign ratio to a cluster.

    Returns:
        dict: Keys are LZ cluster indices, values are lists of primes belonging to that cluster.
              Key -1 is for primes not assigned to any cluster.
    """
    segments = defaultdict(list)

    for i in range(len(primes) - 1):
        ratio = primes[i+1] / primes[i]
        assigned = False
        for idx, lz_val in enumerate(lz_clusters):
            if abs(ratio - lz_val) < tolerance:
                # Append current prime to cluster
                if not segments[idx] or segments[idx][-1] != primes[i]:
                    segments[idx].append(primes[i])
                # Append next prime to cluster as well
                if i+1 == len(primes)-1 or (segments[idx] and segments[idx][-1] != primes[i+1]):
                    segments[idx].append(primes[i+1])
                assigned = True
                break
        if not assigned:
            # Collect unassigned primes under key -1
            if not segments[-1] or segments[-1][-1] != primes[i]:
                segments[-1].append(primes[i])

    return segments

# Example usage:
LZ_clusters = [
    1.20935043,
    1.23377754,
    1.23493518,
    1.23498046,
    1.23498221
]

prime_sequence = [
    136279841, 169050797, 209039287, 258159817, 321729427,
    397749661, 491524907, 609592301, 762912671, 946768399, 1173197299
]

clusters = segment_primes_by_lz(prime_sequence, LZ_clusters)

for cluster_id, primes in clusters.items():
    label = f"Cluster {cluster_id}" if cluster_id >= 0 else "Unassigned"
    print(f"{label}: {primes}")

