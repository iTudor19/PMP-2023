import arviz as az

#modelul centrat
centered_eight = az.load_arviz_data("centered_eight")

num_chains_centered = centered_eight.posterior.chain.size
total_samples_centered = centered_eight.posterior.draw.size

print(f"numarul de lanturi pentru modelul centrat: {num_chains_centered}")
print(f"marimea totala a esantionuliu generat pentru modelul centrat: {total_samples_centered}")

az.plot_posterior(centered_eight)

#modelul necentrat
non_centered_eight = az.load_arviz_data("non_centered_eight")

num_chains_non_centered = non_centered_eight.posterior.chain.size
total_samples_non_centered = non_centered_eight.posterior.draw.size

print(f"numarul de lanturi pentru modelul necentrat: {num_chains_non_centered}")
print(f"marimea totala a esantionuliu generat pentru modelul necentrat: {total_samples_non_centered}")

az.plot_posterior(non_centered_eight)
