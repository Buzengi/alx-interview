#!/usr/bin/python3
"""Prime Game Challenge"""

def isWinner(x, nos):
    """
    Fnx Checks for winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nos:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nos
    n = max(nos)
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nos for each round
    for _, n in zip(range(x), nos):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
