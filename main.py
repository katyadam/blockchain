import core
import time


def main():
    tx = core.Transaction(120, 130, 5.6, time.time())
    data = core.Data()
    data.add_tx(tx)

    blockchain = core.Blockchain()
    blockchain.create_genesis()

    blockchain.mine_new_block(data)
    blockchain.last_block.data.print_data()

    print(
        "current block hash: " + str(blockchain.last_block.hash),
        "previous block hash: " + str(blockchain.last_block.previous_hash),
    )

    tx2 = core.Transaction(130, 140, 4.6, time.time())
    data2 = core.Data()
    data2.add_tx(tx2)

    blockchain.mine_new_block(data2)
    blockchain.last_block.data.print_data()

    print(
        "current block hash: " + str(blockchain.last_block.hash),
        "previous block hash: " + str(blockchain.last_block.previous_hash),
    )


if __name__ == "__main__":
    main()
