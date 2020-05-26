v='tetetetshdfsdgfqgsdfgsdfg'
numberBloc = 8

def decoupe(seq):
    while seq:
        yield seq[:numberBloc]
        seq = seq[numberBloc:]

print(' '.join(list(decoupe(v))))