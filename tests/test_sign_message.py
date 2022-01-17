import pytest

from bitcoin_client.ledger_bitcoin import Client
from bitcoin_client.ledger_bitcoin.exception.errors import DenyError

from .utils import automation


@automation("automations/sign_message_accept.json")
def test_sign_message(client: Client):
    msg = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks."
    path = "m/44'/1'/0'/0/0"
    result = client.sign_message(msg, path)

    assert result == "IE89CCEmDXX/45rXsXAPzN/iJGvBxiS2sGxF+KWRyF1IHppHF7/i0ZW4sWxvpvZJNH7An4ssLbu+NQ9kTd9XRJc="

@automation("automations/sign_message_accept.json")
def test_sign_message_accept(client: Client):
    message = "Hello world!"

    res = client.sign_message(
        message,
        "m/44'/1'/0'/0/0"
    )

    assert res == 'H1yyoNO0oKBIXcDq1eXbq5kJUs22xcNLiyidgakd3GmfeU58PLiVQA3mNfk2OMsBvUsJ4GflgkSejs8mVJ9fI+4='


@automation("automations/sign_message_accept.json")
def test_sign_message_accept_long(client: Client):
    # Test with a long message that is split in multiple leaves in the Merkle tree

    message = "The root problem with conventional currency is all the trust that's required to make it work. The central bank must be trusted not to debase the currency, but the history of fiat currencies is full of breaches of that trust. Banks must be trusted to hold our money and transfer it electronically, but they lend it out in waves of credit bubbles with barely a fraction in reserve. We have to trust them with our privacy, trust them not to let identity thieves drain our accounts. Their massive overhead costs make micropayments impossible."

    res = client.sign_message(
        message,
        "m/44'/1'/0'/0/0"
    )

    assert res == 'Hzc2vj4oA0LxFFBAhtQRwA/aUIpEWHCO51mt8oRl/hJgdd0ZN/wZe6QjBYXNJ4rYUbfl3EeSAseXy27V+Bag3lw='


@automation("automations/sign_message_reject.json")
def test_sign_message_reject(client: Client):
    with pytest.raises(DenyError):
        client.sign_message("Anything", "m/44'/1'/0'/0/0")