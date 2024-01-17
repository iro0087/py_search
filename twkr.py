import os

def advs(input_l, spe_char=[], exclude=True):

    rtn_l = []

    if exclude == True:

        bool_l = list(map(lambda x : x not in spe_char, input_l))

    else:

        bool_l = list(map(lambda x : x in spe_char, input_l))

    for x in range(len(bool_l)):

        if bool_l[x] == True:

            rtn_l.append(input_l[x])

    return rtn_l

def advs_sub(input_l, sub_char=[], exclude=True):

    rtn_l = []

    if exclude == True:

        bool_l = list(map(lambda x : [ i not in x for i in sub_char ], input_l))

        for x in range(len(bool_l)):

            if all(bool_l[x]):

                rtn_l.append(input_l[x])

        return rtn_l

    else:

        bool_l = list(map(lambda x : [ i in x for i in sub_char ], input_l))

        for x in range(len(bool_l)):

            if True in bool_l[x]:

                rtn_l.append(input_l[x])

        return rtn_l

def file_rec(path=".", tracker_l=[os.listdir(".")], cur_depth=0, depth="max", rtn_l=[], type_rtn="file", excl=[], sub_excl=[], frst_path="."):

    if path != frst_path or len(tracker_l) != 0:

        ln = len(tracker_l[cur_depth])

        cnt = 0

        last_len = len(rtn_l)

        while cnt < ln:

            cur_f = tracker_l[cur_depth][cnt]

            rtn_l.append(cur_f)
            
            if os.path.isdir(cur_f) == True:

                if depth == "max" or cur_depth < depth:

                    path += "/{}".format(cur_f.split("/")[-1])

                    cur_depth += 1
    
                    tracker_l[-1] = advs(tracker_l[-1], rtn_l[last_len:])

                    tracker_l.append([ path + "/" + f for f in os.listdir(path) ])

                    return file_rec(path=path, tracker_l=tracker_l, cur_depth=cur_depth, depth=depth, rtn_l=rtn_l, excl=excl, sub_excl=sub_excl, frst_path=frst_path)

            cnt += 1

        if path != frst_path:

            path = "/".join(path.split("/")[:-1])

            cur_depth -= 1

        tracker_l[-1] = []

        tracker_l.pop()

        while len(tracker_l) > 1 and len(tracker_l[-1]) == 0:

            path = "/".join(path.split("/")[:-1])

            tracker_l.pop()

            cur_depth -= 1

        return file_rec(path=path, tracker_l=tracker_l, depth=depth, rtn_l=rtn_l, cur_depth=cur_depth, excl=excl, sub_excl=sub_excl, frst_path=frst_path)

    else:

        if type_rtn == "file":

            rtn_l2 = []
    
            for f in rtn_l:

                if os.path.isdir(f) == False and "__pycache__" not in f and f not in excl:

                    rtn_l2.append(f)

        elif type_rtn == "folder":

            rtn_l2 = []
    
            for f in rtn_l:

                if os.path.isdir(f) == True and "__pycache__" not in f and f not in excl:

                    rtn_l2.append(f)

        if len(sub_excl) > 0:

            print(sub_excl)

            rtn_l2 = advs_sub(rtn_l2, sub_excl)   

        return rtn_l2

x = advs_sub(["ouiii", "non"], ["ui", "ee", "ii"])

print(x)


