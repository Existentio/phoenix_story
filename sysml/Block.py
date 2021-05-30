class Block:
    block_header = chr(171) + 'block' + chr(187)

    def __init__(self, block_x, block_y,
                 block_w, block_h, name,
                 blockheader=block_header):
        self.block_x = block_x
        self.block_y = block_y
        self.block_w = block_w
        self.block_h = block_h
        self.name = name
        self.header = chr(171) + 'block' + chr(187)


t = Block(0, 0, 0, 0, name='')
print(t.header)
print(t.name)
