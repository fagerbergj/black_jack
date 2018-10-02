from card import Card

class HandBustException(Exception):
    pass


class Hand(list):
    def sum(self):
        base_sum = 0
        aces = 0
        res = set()

        for c in self:
            if c.value != (1,11):
                base_sum += c.value
            else:
                aces += 1
                
        return self.get_sums(aces, base_sum)

    def get_sums(self, aces, base_sum):
        height_of_heap = (2**(aces + 1) - 1)
        val_heap = [0] * height_of_heap
        val_heap[0] = base_sum

        return_length = (2**(aces) - 1)
        for i in range(return_length):
            val_heap[2*i + 1] = val_heap[i] + 1
            val_heap[2*i + 2] = val_heap[i] + 11

        raw_sums = {*val_heap[return_length:]}
        sums = self.filter_out_busts(raw_sums)
        if len(sums) == 0:
            raise HandBustException
        return sums

    def filter_out_busts(self, sums):
        r = set()
        for s in sums:
            if s <= 21:
                r.add(s)
        return r
    
