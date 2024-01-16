import arviz as az

centered_eight = az.load_arviz_data("centered_eight")
non_centered_eight = az.load_arviz_data("non_centered_eight")

divergences_centered = centered_eight.sample_stats.diverging.sum().item()
divergences_non_centered = non_centered_eight.sample_stats.diverging.sum().item()

print("Numărul de divergențe în modelul centrat:", divergences_centered)
print("Numărul de divergențe în modelul necentrat:", divergences_non_centered)

az.plot_pair(centered_eight, var_names=['mu', 'tau'], divergences=True)
az.plot_pair(non_centered_eight, var_names=['mu', 'tau'], divergences=True)
