#!/usr/bin/env python
from newsletter.url import LetterUrl
from newsletter import db
from backend import backend

# pre-defined uuids are used to fill the database
ids = [
    '566ed35009584a42ae0898cb7d2c7659',
    'e79512f9051a4f8ea9d51824600afe3a',
    '2e845d6c5e8745b1925ed73f8df4b187',
    '5cb14afb31a747919fd5c5e1c477529e',
    '5f00a48e4d0a41f9812631ed523ca810',
    'eca20f254a48432c9ad6a0e326025b52',
    '4bea4ee2248a4ac0b1c4f5e7d7119299',
    '408035b32d7a4602b520cbbe2e0abcee',
    'fc2314f646fc4650bb7987fdd3c8f8dd',
    '29f098661abf4ecd97adf77eb588a694',
    'c7de9d8aef2c43f2830df173e6b3be25',
    '9be5b61ceb5746e99dca6b2e7168929c',
]
with backend.app_context():
    db.create_all()
    newsletter = LetterUrl()

    print newsletter.url(uuid=ids.pop(), email='n11u1@testdoamin.tld', url='http://ya.ru', letter_id=11)
    print newsletter.url(uuid=ids.pop(), email='n11u2@testdoamin.tld', url='http://ya.ru', letter_id=11)
    print newsletter.url(uuid=ids.pop(), email='n11u2@testdomain.tld', url='http://goo.gl', letter_id=11)
    print newsletter.url(uuid=ids.pop(), email='n11u3@testdomain.tld', url='http://goo.gl', letter_id=11)
    print newsletter.url(uuid=ids.pop(), email='n11u4@testdomain.tld', url='http://goo.gl', letter_id=11)
    print newsletter.url(uuid=ids.pop(), letter_id=11)

    print newsletter.url(uuid=ids.pop(), email='n12u1@testdomain.tld', url='http://yahoo.com', letter_id=12)
    print newsletter.url(uuid=ids.pop(), email='n12u2@testdomain.tld', url='http://yahoo.com', letter_id=12)
    print newsletter.url(uuid=ids.pop(), email='n12u1@testdomain.tld', url='http://todois.com', letter_id=12)
    print newsletter.url(uuid=ids.pop(), letter_id=12)

    print newsletter.url(uuid=ids.pop(), email='n13u1@testdomain.tld', url='http://todois.com', letter_id=13)
    print newsletter.url(uuid=ids.pop(), letter_id=13)
