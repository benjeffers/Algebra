from itertools import combinations

class Group:
    
    def __init__(self, set, func):
        self.set = set
        self.func = func

    def is_associative(self) -> int:
        """returns 1 is group is asociative, 0 otherwise"""

        for a in self.set:
            for b in self.set:
                ab = self.func(a, b)
                for c in self.set:
                    bc = self.func(b, c)
                    a_bc = self.func(a, bc)
                    ab_c = self.func(ab, c)
                    if(a_bc != ab_c):
                        return 0
        return 1

    def is_closed(self) -> int:
        """returns 1 is group os closed, 0 otherwise"""

        for a in self.set:
            for b in self.set:
                ab = self.func(a, b)
                if(ab not in self.set):
                    return 0
        return 1

    def has_identity(self) -> int:
        """returns 1 is group has a unique identity, 0 otherwise"""

        identity_count = 0
        for a in self.set:
            is_identity = 1
            for b in self.set:
                ab = self.func(a, b)
                if(ab != b):
                    is_identity = 0
            if(is_identity == 1):
                identity_count += 1
        
        if(identity_count == 1):
            return 1
        else:
            return 0

    
    def identity(self):
        """returns the identity if group contains one, 0 otherwise"""

        for a in self.set:
            is_identity = 1
            for b in self.set:
                ab = self.func(a, b)
                if(ab != b):
                    is_identity = 0

            if(is_identity == 1):
                return a
        return 0

    
    def has_inverses(self) -> int:
        """returns 1 if group has inverses, 0 otherwise"""

        if(self.has_identity):
            identity = self.identity()

            for a in self.set:
                has_inverse = 0
                for b in self.set:
                    ab = self.func(a, b)
                    if(ab == identity):
                        has_inverse = 1
                if(has_inverse):
                    return 1
                else:
                    return 0
        return 0


    def inverse(self, elem):
        """Document this later"""
        
        if(self.has_identity()):
            identity = self.identity()
            if(elem == identity):
                return identity
            else:
                for a in self.set:
                    if(self.func(elem, a) == identity):
                        return a
            
        return False


    def is_group(self):
        """checks if the set is a group, if true returns 1, otherwise 0"""

        if(not self.is_closed()):
            print('is not closed')
            return 0
        if(not self.is_associative()):
            print('is not associative')
            return 0
        if(not self.has_identity()):
            print('no identity')
            return 0
        if(not self.has_inverses()):
            print('no inverses')
            return 0
        
        return 1

    def is_subset(self, G):
        for elem in self.set:
            if(elem not in G.set):
                return 0
        return 1

    def is_subgroup(self, G):
        if(self.is_subset(G) and self.is_group()):
            return 1
        
        return 0

    def power(self, elem, pow):
        if(pow == 0):
            return self.identity()
        elif(pow == 1):
            return elem
        else:
            power_elem = elem
            for _ in range(2, pow+1):
                power_elem = self.func(power_elem, elem)
            return power_elem
        

    def subsets(self):
        size = len(self.set)
        combs = []
        for k in range(1, size):
            combs.append(list(combinations(self.set, k)))

        flat_combs = []
        for lst in combs:
            for combination in lst:
                flat_combs.append(list(combination))
        return flat_combs

    
    def subgroups(self):
        subsets = self.subsets()
        subgroups = []
        for subset in subsets:
            H = Group(subset, self.func)
            subgroups.append(H)

        for subgroup in subgroups:
            if(not subgroup.is_associative()):
                subgroups.remove(subgroup)
                continue
            if(not subgroup.is_closed()):
                subgroups.remove(subgroup)
                continue
            if(not subgroup.has_identity()):
                subgroups.remove(subgroup)
                continue
            if(not subgroup.has_inverses()):
                subgroups.remove(subgroup)
                continue
        return subgroups
        