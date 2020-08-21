#part1
# Merge the wards and census tables on the ward column
wards_census = wards.merge(census,on='ward')

# Print the shape of wards_census
print(wards_census.shape)


#part2
# In the ward column change '1' to '61'
wards.loc[wards['ward'] == '1', 'ward'] = '61'

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)
#just changing the value



#part3
# Change '1' to None in `ward` col
census.loc[census['ward'] == '1', 'ward'] = None

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print(wards_census.shape)
#changing value to 'none'