# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .MoneroTransactionRsigData import MoneroTransactionRsigData


class MoneroTransactionRangeSigRequest(p.MessageType):
    FIELDS = {
        1: ('rsig_data', MoneroTransactionRsigData, 0),
    }

    def __init__(
        self,
        rsig_data: MoneroTransactionRsigData = None,
    ) -> None:
        self.rsig_data = rsig_data
