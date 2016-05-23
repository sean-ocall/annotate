from Class import Compound, UnTgCompound

fp = open('MZ_for Sean.csv', 'r')

lines = fp.readlines()

compounds = []

for line in lines[2:]:
    parts = line.split(',')
    name = parts[0]
    mz = parts[1]

    new_cpd = Compound(name, mz)

    for part in parts[2:]:
        if len(part) > 1:
            if float(part) <60:
                new_cpd.add_rt(part)

    compounds.append(new_cpd)

for compound in compounds[0:10]:
    name = compound.get_name()
    mz = compound.get_mz()
    avg_rt = compound.get_avg_rt()

    print name, ":", mz, ":", avg_rt


fp_2 = open("Pks_An_mod.tsv", 'r')

lines = fp_2.readlines()

untg_compounds = []


for line in lines[1:]:
    parts = line.split('\t')

    id = parts[0]


    mzmin = parts[2]
    mzmax = parts[3]

    rtmin = parts[5]
    rtmax = parts[6]

    new_cpd = UnTgCompound(id, mzmin, mzmax, rtmin, rtmax)

    untg_compounds.append(new_cpd)


for untg in untg_compounds:
    for compound in compounds:
        if untg.check_between_mz(compound.get_mz()) and untg.check_between_rt(compound.get_avg_rt()):
            untg.add_poss_match(compound.get_name())

            
op = open("Pks_An_id.tsv","w")

op.write("id\t"+lines[0])

for i,line in enumerate(lines[1:]):
    op.write(untg_compounds[i].get_poss_matches() + "\t" + line)

op.close()
    

    
