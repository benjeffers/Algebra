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
        subgroups = [H_1.set, H_2.set]
        G_subgroup_sets = []
        for group in G.subgroups():
            G_subgroup_sets.append(group.set)
        self.assertTrue(G_subgroup_sets == subgroups)


    def test_left_coset(self):
        G = self.create_group_additive()
        H = Group([0, 2],  G.func)
        coset = G.left_coset(H, 1)
        self.assertTrue(coset == Group([1, 3], G.func))

    def test_right_coset(self):
        G = self.create_group_additive()
        H = Group([0, 2],  G.func)
        coset = G.right_coset(H, 1)
        self.assertTrue(coset == Group([1, 3], G.func))


    def test_equality(self):
        G = Group([1, 2, 3, 4, 5], lambda x, y: (x + y)%5)
        H = Group([1, 2, 3, 4, 5], lambda x, y: (x + y)%5)
        self.assertTrue(G == H)

    def test_equality_false(self):
        G = self.create_group_additive()
        H = self.create_group_multiplicative()
        self.assertFalse(G == H)

    def test_inequality(self):
        G = Group([1, 2, 3, 4, 5], lambda x, y: (x + y)%5)
        H = Group([1, 2, 3, 4], lambda x, y: (x + y)%4)
        self.assertTrue(G != H)

    def test_inequality_false(self):
        G = Group([1, 2, 3, 4, 5], lambda x, y: (x + y)%5)
        H = Group([1, 2, 3, 4, 5], lambda x, y: (x + y)%5)
        self.assertFalse(G != H)

    def test_is_abelian(self):
        G = self.create_group_additive()
        self.assertTrue(G.is_abelian())

    def test_normal(self):
        G = self.create_group_additive()
        H = Group([0, 2], G.func)
        self.assertTrue(G.is_normal(H))

    def test_order_identity(self):
        G = self.create_group_additive()
        self.assertTrue(G.order(0) == 1)

    def test_order_one(self):
        G = self.create_group_additive()
        self.assertTrue(G.order(1) == 4)

    def test_order_two(self):
        G = self.create_group_additive()
        self.assertTrue(G.order(2) == 2)

    def test_order_three(self):
        G = self.create_group_additive()
        self.assertTrue(G.order(3) == 4)
    
    def test_group_generated_by(self):
        G = self.create_group_additive()
        H = Group([0, 2], G.func)
        self.assertTrue(G.group_generated_by(2) == H)

    def test_group_generated_by_cyclic(self):
        G = self.create_group_additive()
        self.assertTrue(G.group_generated_by(3) == G)

    def test_is_cylic(self):
        G = self.create_group_additive()
        self.assertTrue(G.is_cylic())

    def test_is_cylic_false(self):
        G = self.create_group_multiplicative()
        self.assertFalse(G.is_cylic())

    def test_direct_product(self):
        G = Group([0, 1], lambda x, y: (x + y)%2)
        H = Group([0, 1], lambda x, y: (x + y)%2)
        GH = Group([(0, 0), (0, 1), (1, 0), (1, 1)], lambda x, y: ((x[0] + y[0])%2, (x[1] + y[1])%2))
        self.assertTrue(G.external_direct_product(H) == GH)

    def test_generators(self):
        G = self.create_group_additive()
        gens = [1, 3]
        self.assertTrue(G.get_generators() == gens)
        

if __name__ == '__main__':
    unittest.main()