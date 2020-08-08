#part1
# Select the individuals column
individuals = homelessness['individuals']
individuals.head

# Print the head of the result
print(individuals.head())


#part2
# Select the state and family_members columns
state_fam = homelessness[['state' , 'family_members']]

# Print the head of the result
print(state_fam.head())

#part3
# Select only the individuals and state columns, in that order
ind_state = homelessness[['individuals' , 'state']]

# Print the head of the result
print(ind_state.head())