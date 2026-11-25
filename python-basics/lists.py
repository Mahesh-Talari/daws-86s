server_1 = "Ansible "
server_2 = "Jenkins"
servers = ["172.10.33.25", server_2, True, 10, 20.5]
print(type(servers), servers,server_1,server_2)
#pthon is zero based index
server_1 = servers[0]
print("Server 1 ip address:", server_1)

#slicing (start_Index:end_index+1:step_size) end_index is not inclusive
sample_slice = servers[0:2]
print("Sample Slice:", sample_slice)

sample_slice = servers[0:5:2]   
print("Sample Slice:", sample_slice)

sample_slice = servers[1:5:2]   #[1,1+2,3+2,5+2]
print("Sample Slice:", sample_slice)

#Negative Indexing
sample_slice = servers[-1:-4:-1]   #last two elements
print("Sample Slice:", sample_slice)
print("Length of servers list:", len(sample_slice))

# List is mutable data type, we can change the values of list
# Mutable : Once define , can cahnge at any time E.g. List, Dictionary
# Immutable : Once define , cannot be cahnge  E.g. Tuple, Sets  

print("Original servers list:", servers)
servers[3] = 1234 # Inplace operation
print("Updated servers list:", servers)

print("List of Operations:", dir(servers))
"""[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']"""