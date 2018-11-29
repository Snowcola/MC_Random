import datetime
from collections import OrderedDict


class Modes:
    SINGLE = 1
    DOUBLE = 2

    
class RandomSample:

    def __init__(self, lot_size=3000, sample_size=80,
                 single=True, date=None, seed=None):
        self.lot_size = lot_size
        self.sample_size = sample_size
        self.mode = self.set_mode(single)
        self.date = self.set_date(date)
        self.s_e = self.seconds_elapsed_mc(self.date)
        self.seed = self.set_seed(seed)
        self.shuffling_array = self.rng_array()
        self.start_array = self.shuffling_array[:]
        sample = self.cong_reoc()
        self.samples = sample[:2]
        self.stat_sample = sample[2]

    @staticmethod
    def set_mode(mode):
        if mode:
            return Modes.SINGLE
        else:
            return Modes.DOUBLE

    def set_seed(self, seed):
        if not seed:
            return self.automatic_seed_generation()
        return seed
    
    @staticmethod
    def set_date(date):
        if date:
            return date
        else:
            return datetime.datetime.utcnow()

    @staticmethod
    def seconds_elapsed_mc(current_date):
        m_1 = current_date.month
        y = current_date.year
        d = current_date.day

        if m_1 < 3:
            m_1 += 12
            y += -1
        d_e = int(d+((153*m_1 - 457)/5) + 365*y +
                    (y/4) - (y/100) + (y/400) - 730426)
        s_e = 86400*d_e + current_date.hour*3600 + current_date.minute*60 +  \
            current_date.second

        return int(s_e)  # time since 2000-01-01 00:00:00 in seconds

    @staticmethod
    def j_times(seconds_elapsed):
        jstr = str(seconds_elapsed)[-2:]
        j = int(jstr)+1
        return j

    def automatic_seed_generation(self):
        seed = self.s_e
        j = self.j_times(seed)
        for _ in range(j):
            seed = 40692*seed % 2147483399
        return int(seed)

    @staticmethod
    def next_x(x):
        return 40014*x % 2147483563

    @staticmethod
    def next_y(y):
        return 40692*y % 2147483399

    def rng_array(self):
        x = self.seed
        A = []
        for _ in range(40):
            x = 40014*x % 2147483563
            A.append(x)
        A = A[8:]
        A.reverse()
        return A

    def cong_reoc(self):
        k = self.shuffling_array[0]
        x = self.shuffling_array[0]
        y = self.seed
        ls = []
        ks = []
        while len(set(ls)) < self.sample_size*self.mode:
            x_i_plus_1 = self.next_x(x)
            x = x_i_plus_1

            y_i_plus_1 = self.next_y(y)
            y = y_i_plus_1

            J = int((32*k / 2147483563) + 1)

            k = self.shuffling_array[J-1] - y_i_plus_1

            self.shuffling_array[J-1] = x_i_plus_1

            if k < 1:
                k += 2147483562

            if k not in ks:
                ks.append(k)
            ls.append(int(k/2147483563*self.lot_size+1))

        sample = list(OrderedDict.fromkeys(ls))

        s_1 = sample[:self.sample_size]
        s_2 = sample[self.sample_size:]

        return s_1, s_2, ks

    @property
    def samples_sorted(self):
        """
        Returns a list of a list of samples sorted in ascending order
        """
        rv = list(map(sorted, self.samples))
        return rv
