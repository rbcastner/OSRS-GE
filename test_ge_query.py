from unittest import TestCase
from ge_query import grand_exchange_query


class TestGeQuery(TestCase):

    def test_parses_api(self):
        data = grand_exchange_query('detailed', 3002)
        self.assertTrue(data is not None)
        self.assertEqual(
            {
                'icon', 'icon_large', 'id', 'type', 'typeIcon', 'name', 'description',
                'current', 'today', 'members', 'day30', 'day90', 'day180'
            },
            set(data.keys())
        )
