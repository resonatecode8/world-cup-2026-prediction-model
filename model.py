import math

DC_RHO = -0.13

def expected_score(ratingA, ratingB, homeBonusA=0):
    return 1 / (1 + 10 ** ((ratingB - (ratingA + homeBonusA)) / 400))


def expected_goals(rating, opponent, homeBonus=0):
    diff = (rating + homeBonus) - opponent
    lam = 1.35 + diff / 400
    return max(0.3, min(3.5, lam))


def poisson_pmf(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)


def dc_tau(a, b, lam, mu, rho):
    if a == 0 and b == 0:
        return 1 - lam * mu * rho
    if a == 0 and b == 1:
        return 1 + lam * rho
    if a == 1 and b == 0:
        return 1 + mu * rho
    if a == 1 and b == 1:
        return 1 - rho
    return 1


def match_prob(ratingA, ratingB, homeBonusA=0):
    lam = expected_goals(ratingA, ratingB, homeBonusA)
    mu = expected_goals(ratingB, ratingA, -homeBonusA / 2)

    winA = draw = winB = 0

    for a in range(9):
        for b in range(9):
            p = poisson_pmf(a, lam) * poisson_pmf(b, mu) * dc_tau(a, b, lam, mu, DC_RHO)

            if a > b:
                winA += p
            elif a < b:
                winB += p
            else:
                draw += p

    total = winA + draw + winB

    return {
        "winA": winA / total,
        "draw": draw / total,
        "winB": winB / total,
        "expectedGoalsA": lam,
        "expectedGoalsB": mu
    }
