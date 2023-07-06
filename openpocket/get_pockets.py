def get_pockets(molecular_system, probe_radius="1 angstrom"):

    pockets = {}

    with open('static/keys.txt', 'r') as fp:
        for line in fp:
            fields = [ii for ii in line.split(' ') if ii!='']
            atom_index = int(fields[1])-1
            pocket_index = int(fields[-2])-1
            if pocket_index in pockets:
                pockets[pocket_index].append(str(atom_index))
            else:
                pockets[pocket_index]=[str(atom_index)]

    return pockets


def show_pockets(molecular_system, pockets, index):

    from molsysmt import view as msm_view

    if isinstance(index, int):
        index=[index]

    fragments=[','.join(pockets[ii]) for ii in index]
    sel='@'+','.join(fragments)

    view = msm_view(molecular_system, standard=True)
    view.add_surface(sel, opacity='0.3', color='red')

    return view


