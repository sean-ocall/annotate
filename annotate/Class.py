class Compound(object):

    def __init__(self, name, mz):
        self.__name = name
        self.__mz = float(mz)
        self.__rt_list = []

    def add_rt(self, rt):
        """
        assumes minutes!!!!!!!!!!!!!
        """
        self.__rt_list.append(60*float(rt))

    def get_avg_rt(self):
        avg = reduce(lambda x, y: x + y, self.__rt_list) / len(self.__rt_list)
        return avg

    def get_min_rt(self):
        return min(self.__rt_list)

    def get_max_rt(self):
        return max(self.__rt_list)

    def get_rt_range(self):
        return max(self.__rt_list) - min(self.__rt_list)

    def get_name(self):
        return self.__name

    def get_mz(self):
        return self.__mz

        

class UnTgCompound(object):

    def __init__(self, id, mzmin, mzmax, rtmin, rtmax):
        self.__id = id
        self.__mzmin = float(mzmin)
        self.__mzmax = float(mzmax)
        self.__rtmin = float(rtmin)
        self.__rtmax = float(rtmax)

        self.__poss_matches = ""

    def get_id(self):
        return self.__id

    def check_between_mz(self, mz):
        if self.__mzmin < float(mz) and float(mz) < self.__mzmax:
            return True
        else:
            return False

    def check_between_rt(self, lib_min_rt, lib_max_rt):
        if self.__rtmin > lib_min_rt-1 and self.__rtmax < lib_max_rt+1:
            return True
        else:
            return False
        

    def check_between_rt_old(self, rt):
        if self.__rtmin-10 < float(rt) and float(rt) < self.__rtmax+10:
            return True
        else:
            return False

    def add_poss_match(self, poss_match):
        if self.__poss_matches == "":
            self.__poss_matches = poss_match
        else:
            self.__poss_matches = self.__poss_matches + ' + ' + poss_match
            
    def get_poss_matches(self):
        return self.__poss_matches
