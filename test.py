from blockchain import Block, Blockchain

bchain = Blockchain()
bchain.current_data = [1, 2, 3, 4]

bchain.mine()