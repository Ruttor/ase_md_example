'''
from zntrack import Node, zn
import ase
import ase_md.simulator as asemd
import typing
import matplotlib.pyplot as plt

class GetAtoms(Node):
    """Generate Atoms for Simulation"""

    # Inputs:
    size: int = zn.params()
    # Outputs:
    atoms: ase.Atoms = zn.outs()
    # Function:
    def run(self):
        self.atoms = asemd.generate_atoms(self.size)

if __name__ == "__main__":
    cool_atoms = GetAtoms(size=3)
    cool_atoms.write_graph()


'''
from zntrack import Node, zn
import ase_md.simulator as asemd
import typing

class GetAtoms(Node):
    """Atome abholen"""
    size: int = zn.params()
    atoms = zn.outs()

    def run(self):
        self.atoms = asemd.generate_atoms(self.size)


x = GetAtoms(size = 2)
x.write_graph()



#atoms = ase_md.simulator.generate_atoms(size=2)

#atoms_list = ase_md.simulator.run_simulation(atoms=atoms, temperature=300, timestep=1.0, dump_interval=5, steps=20)

#rdf = ase_md.simulator.compute_rdf(atoms_list=atoms_list, rmax=1.0, nbins=50, elements="Cu")

#print(rdf)


