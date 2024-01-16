import arviz as az

centered_eight = az.load_arviz_data("centered_eight")
non_centered_eight = az.load_arviz_data("non_centered_eight")

rhat_centered = az.rhat(centered_eight, var_names=['mu', 'tau'])
rhat_non_centered = az.rhat(non_centered_eight, var_names=['mu', 'tau'])

print("Statisticile Rhat pentru modelul centrat:")
print(rhat_centered)

print("\nStatisticile Rhat pentru modelul necentrat:")
print(rhat_non_centered)

autocorr_centered = az.autocorr(centered_eight, var_names=['mu', 'tau'])
autocorr_non_centered = az.autocorr(non_centered_eight, var_names=['mu', 'tau'])

az.plot_autocorr(autocorr_centered, combined=True)
az.plot_autocorr(autocorr_non_centered, combined=True)
