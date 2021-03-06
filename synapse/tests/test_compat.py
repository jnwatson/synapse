from synapse.tests.common import *

import synapse.compat as s_compat

class CompatTest(SynTest):

    def test_compat_canstor(self):
        self.true(0xf0f0)
        self.true(0xf0f0f0f0f0f0)
        self.true(s_compat.canstor('asdf'))
        self.true(s_compat.canstor(u'asdf'))

        self.false(s_compat.canstor(True))
        self.false(s_compat.canstor(('asdf',)))
        self.false(s_compat.canstor(['asdf', ]))
        self.false(s_compat.canstor({'asdf': True}))

    def test_compat_quote(self):
        self.eq(s_compat.url_quote('asdf'), 'asdf')
        self.eq(s_compat.url_quote('asdf&foo'), 'asdf%26foo')
        self.eq(s_compat.url_quote('asdf foo'), 'asdf%20foo')

    def test_compat_quote_plus(self):
        self.eq(s_compat.url_quote_plus('asdf'), 'asdf')
        self.eq(s_compat.url_quote_plus('asdf&foo'), 'asdf%26foo')
        self.eq(s_compat.url_quote_plus('asdf foo'), 'asdf+foo')
