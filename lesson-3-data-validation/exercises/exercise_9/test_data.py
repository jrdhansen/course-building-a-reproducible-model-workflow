import scipy.stats


def test_kolmogorov_smirnov(data, ks_alpha):
    sample1, sample2 = data

    columns = [
        "danceability",
        "energy",
        "loudness",
        "speechiness",
        "acousticness",
        "instrumentalness",
        "liveness",
        "valence",
        "tempo",
        "duration_ms",
    ]

    # Bonferroni correction for multiple hypothesis testing
    alpha_prime = 1 - (1 - ks_alpha) ** (1 / len(columns))

    for col in columns:
        ts, p_value = scipy.stats.ks_2samp(sample1[col], sample2[col])
        assert p_value > alpha_prime
