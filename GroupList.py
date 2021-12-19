def group_list(group, users):
    print(len(users))
    members = group + ": "
    for index, elements in enumerate(users):
        members += elements
        if index < len(users)-1:
            members += ", "

    return members


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"]))  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"