#part1
# Merge the crews table to itself
crews_self_merged = crews.merge(crews,on='id',suffixes=('_dir','_crew'))


#part2
# Merge the crews table to itself
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))

# Create a Boolean index to select the appropriate rows
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') &
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]


#part3
# Print the first few rows of direct_crews
print(direct_crews.head())