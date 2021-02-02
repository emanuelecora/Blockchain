from blockchain import Block, Blockchain, User

# bchain = Blockchain()
# bchain.current_data = [1, 2, 3, 4]
# bchain.mine()

user1 = User()

print(user1.public_key.exportKey())
print(user1.private_key.exportKey())

