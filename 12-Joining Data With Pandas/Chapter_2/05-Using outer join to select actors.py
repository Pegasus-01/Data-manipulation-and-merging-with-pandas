# Merge begins_actors to returns_actors on id with outer join using suffixes
begins_returns = begins_actors.merge(returns_actors,
                                     how='outer',
                                     on='id',
                                     suffixes=('_beg','_ret'))

# Create an index that returns true if name_beg or name_ret are null
m = ((begins_returns['name_beg'].isnull()) |
     (begins_returns['name_ret'].isnull()))

# Print the first few rows of begins_returns
print(begins_returns[m].head())