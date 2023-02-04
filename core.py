from typing import List, Optional


Previous_block_hash = str
Current_block_hash = str
SECRET_CODE = "This is secret code."


class Transaction:
    def __init__(
        self, id_from: int, id_to: int, amount: float, timestamp: float
    ) -> None:
        self.id_from = id_from
        self.id_to = id_to
        self.amount = amount
        self.timestamp = timestamp


class Data:
    def __init__(self) -> None:
        self.txs: List["Transaction"] = []

    def add_tx(self, tx: "Transaction") -> None:
        self.txs.append(tx)

    def print_data(self) -> None:

        print("ID_FROM\tID_TO\tAMOUNT\tTIMESTAMP")

        for tx in self.txs:
            print(f"{tx.id_from}\t{tx.id_to}\t{tx.amount}\t{tx.timestamp}")

    def get_txs_to_hash(self) -> str:
        txs_to_hash = ""
        for tx in self.txs:
            txs_to_hash += (
                str(tx.id_to) + str(tx.id_from) + str(tx.amount) + str(tx.timestamp)
            )

        return txs_to_hash


class Block:
    def __init__(self, data: "Data") -> None:
        self.previous_hash: Optional[Previous_block_hash] = None
        self.hash: Current_block_hash = None
        self.data: "Data" = data


class Blockchain:
    def __init__(self) -> None:
        self.genesis: "Block" = None
        self.last_block: "Block" = None  # pointing onto last block in blockchain

    # genesis block is a first block of blockhain
    # it contains only its hash, to be a base for other chained blocks
    def create_genesis(self) -> None:

        genesis_block = Block(None)
        genesis_block.hash = hash(SECRET_CODE)

        self.genesis = genesis_block
        self.last_block = genesis_block

    # implementing new block into blockchain
    def mine_new_block(self, data: "Data") -> None:
        block = Block(data)
        block.previous_hash = self.last_block.hash
        block.hash = hash(tuple(block.data.get_txs_to_hash()))
        self.last_block = block
