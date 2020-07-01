import unittest
from Group import Group

class TestGroup(unittest.TestCase):

    def create_group_additive(self):
        set = [0, 1, 2, 3]
        add = lambda x, y: (x+y)%4
        G = Group(set, add)
        return G

    def create_group_multiplicative(self):
        set = [1, 3, 5, 7]
        multiply = lambda x, y: (x*y)%8
        G = Group(set, multiply)
        return G

    def test_is_closed(self):
        G = self.create_group_additive()
        self.assertTrue(G.is_closed())

    def test_is_closed_false(self):
        G = Group([0, 1, 3], lambda x, y: (x+y)%4)
        self.assertFalse(G.is_closed())

    def test_is_associative(self):
        G = self.create_group_additive()
        self.assertTrue(G.is_associative())

    def test_has_identity(self):
        G = self.create_group_additive()
        self.assertTrue(G.has_identity())

    def test_has_identity_false(self):
        G = Group([1, 2, 3], lambda x, y: (x+ y)%4)
        self.assertFalse(G.has_identity())

    def test_has_inverses(self):
        G = self.create_group_additive()
        self.assertTrue(G.has_inverses())

    def test_has_inverses_false(self):
        G = Group([0, 2, 3], lambda x, y: (x+y)%4)
        self.assertFalse(G.has_inverses())

    def test_group(self):
        G = self.create_group_additive()
        self.assertTrue(G.is_group())

    def test_group_false(self):
        G = Group([0, 2, 3], lambda x, y: (x+y)%4)
        self.assertFalse(G.is_group())

    def test_is_subgroup(self):
        
        G = self.create_group_additive()
        H = Group([0, 2], lambda x, y : (x + y) % 4)
        self.assertTrue(H.is_subgroup(G))

    def test_power_nonidentity(self):
        G = self.create_group_additive()
        self.assertTrue(G.power(2, 2) == 0)
    
    def test_power_zero(self):
        G = self.create_group_additive()
        self.assertTrue(G.power(0, 3) == 0)

    def test_power_one(self):
        G = self.create_group_additive()
        self.assertTrue(G.power(1, 3)== 3)

    def test_inverse_identity(self):
        G = self.create_group_additive()
        self.assertTrue(G.inverse(0) == 0)

    def test_inverse_one(self):
        G = self.create_group_additive()
        self.assertTrue(G.inverse(1) == 3)

    def test_inverse_two(self):
        G = self.create_group_additive()
        self.assertTrue(G.inverse(2) == 2)

    def test_inverse_three(self):
        G = self.create_group_additive()
        self.assertTrue(G.inverse(3) == 1)

    def test_inverse_three_false(self):
        G = Group([0, 2, 3], lambda x, y: (x+y)%4)
        self.assertFalse(G.inverse(3) == 0)

    def test_identity_additive(self):
        G = self.create_group_additive()
        self.assertTrue(G.identity() == 0)

    def test_identity_multiplicative(self):
        G = self.create_group_multiplicative()
        self.assertTrue(G.identity() == 1)

    

    def test_subgroups(self):
        G = self.create_group_additive()
        H_1 = Group([0], lambda x, y: (x+y)%4)
        H_2 = Group([0, 2], lambda x, y: (x+y)%4)
        subgroups = [H_1, H_2]
        for g in G.subgroups():
            print(g.set)
        self.assertTrue(G.subgroups() == subgroups)

if __name__ == '__main__':
    unittest.main()