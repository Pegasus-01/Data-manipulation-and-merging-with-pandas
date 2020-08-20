# Merge revenue & managers on 'city' & 'branch': combined
combined = pd.merge(revenue, managers, right_on='branch',left_on='city')

# Print combined
print(combined)