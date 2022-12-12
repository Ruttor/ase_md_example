
from zntrack import Node, zn
import ase_md.simulator as asemd
import typing
import ase_md


class GetAtoms(Node):
    """Atome abholen"""
    size: int = zn.params()
    atoms = zn.outs()

    def run(self):
        self.atoms = asemd.generate_atoms(self.size)

class RunMD(Node):
    ''' Run Method '''
    atoms: GetAtoms = zn.deps()
    temperature: int = zn.params()
    timestep: float = zn.params()
    steps: int = zn.params()
    dump_interval: int = zn.params()
    
    atoms_list = zn.outs()

    def run(self):
        self.atoms_list = asemd_run simulation (
                atoms = self.atoms,
                temperature = self.temperature,
                timestep = self.timestep,
                steps = self.steps,
                dump_interval = self.dump_interval
            )

class ComputeRDF(Node):
    atoms_list: RunMD = zn.deps()
    rmax: float = zn.params()
    nbins: int = zn.params()
    elements: str = zn.params()
    
    rdf: dict = zn.outs()

    def run(self):
        self.rdf = asemd.compute_rdf(
                atoms_list = self.atoms_list.atoms_list,
                rmax = self.rmax,
                nbins = self.nbins,
                elements = self.elements
            )

x = GetAtoms(size = 2)
x.write_graph()



