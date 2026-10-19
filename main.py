from pyscript import display, document


gr7 = {'Joachin Conde', 'Clarize Galang'}
gr8 = {'Rhoann Capili', 'Andrew Lizardo'}
gr9 = {'Shaun Cortes', 'Sofia Riofrio'}
gr10 = {'Jacob Mendoza', 'Al-Makram Arbison'}

memberset = (gr7 | gr8 | gr9 | gr10)

display(f'The members are: {memberset}', target='result')
display(f'Total number: {len(memberset)}', target='result')

def add_member(e):

    document.getElementById('result').innerHTML = " "

    gname = document.getElementById('gname').value
    sname = document.getElementById('sname').value
    name = gname + " " + sname
    nameset = {name}

    memberadd = (nameset | memberset)

    display(f'The members are: {memberadd}', target='result')
    display(f'Total number: {len(memberadd)}', target='result')
