from .Species import *
from .SpeciesList import *

class Cluster:

    ###
    # @brief Initialize the :class:`Cluster`
    ##
    def __init__( self, site_types: list, neighboring: list, species: SpeciesList,
                    gas_species: SpeciesList=SpeciesList(), multiplicity: int=0, cluster_energy: float=0.000 ):
        """
        Creates a new Cluster object

        :parm site_types: tuple
        :parm neighboring: list
        :parm species: tuple
        :parm multiplicity: int
        :parm cluster_energy: float
        """
        self.site_types = site_types                  # e.g. ( "f", "f" )
        self.neighboring = neighboring                # e.g. [ (1,2) ]
        self.species = species                        # e.g. ( Species("H*",1), Species("H*",1) )
        self.gas_species = gas_species                # e.g. ( Species("H2") )
        self.multiplicity = multiplicity              # e.g. 2
        self.cluster_energy = cluster_energy                          # Units eV

        self.sites = len(site_types)

        if( len(species) != self.sites ):
            msg  = "### ERROR ### Cluster.__init__.\n"
            msg += "Inconsistent dimensions for species or site_types\n"
            raise NameError(msg)

        self.__label = None
        self.__updateLabel()

        self.__mass = 0.0

        for item in species:
            self.__mass += item.mass()

        for item in gas_species:
            self.__mass += item.mass()


    def __len__( self ) -> int:
        """
        Returns the number of species inside the cluster
        """
        return len(self.species)


    def __eq__( self, other ):
        """
        Returns True if both objects have the same label. Otherwise returns False
        """
        if( self.__label == other.__label ):
            return True
        else:
            return False


    def __hash__(self):
        """
        Returns a hash based on the label
        """
        return hash(self.__label)


    def __updateLabel( self ):
        """
        Updates the attribute 'label'
        """
        self.__label = ""
        for i in range(len(self.species)):
            self.__label += self.species[i].symbol+"-"+self.site_types[i]
            if( i != len(self.species)-1 ):
                self.__label += ","

        if( len(self.gas_species) > 0 ):
            self.__label += ":"

        for i in range(len(self.gas_species)):
            self.__label += self.gas_species[i].symbol
            if( i != len(self.gas_species)-1 ):
                self.__label += ","

        if( len(self.neighboring) > 0 ):
            self.__label += ":"

        for i in range(len(self.neighboring)):
            self.__label += str(self.neighboring[i]).replace(" ", "")
            if( i != len(self.neighboring)-1 ):
                self.__label += ","


    def label( self ) -> str:
        """
        Returns the label of the cluster
        """
        if( self.label is None ):
            self.__updateLabel()

        return self.__label


    def __str__( self ) -> str:
        """
        Translates the object to a string
        """
        output  = "cluster " + self.__label +"\n"

        if( len(self.gas_species) != 0 ):
            output += "  # gas_species "
            for i in range(len(self.gas_species)):
                output += self.gas_species[i].symbol
                if( i != len(self.gas_species)-1 ):
                    output += " "
            output += "\n"

        if( self.sites != 0 ):
            output += "  sites " + str(self.sites)+"\n"

            output += "  neighboring "
            for i in range(len(self.neighboring)):
                output += str(self.neighboring[i][0])+"-"+str(self.neighboring[i][1])
                if( i != len(self.neighboring)-1 ):
                    output += " "
            output += "\n"

            output += "  lattice_state"+"\n"
            for i in range(len(self.species)):
                output += "    "+str(i+1)+" "+self.species[i].symbol+" "+str(self.species[i].denticity)+"\n"

            output += "  site_types "
            for i in range(len(self.site_types)):
                output += str(self.site_types[i])
                if( i != len(self.site_types)-1 ):
                    output += " "
            output += "\n"

            output += "  graph_multiplicity "+str(self.multiplicity)+"\n"

        output += "  cluster_eng "+str(self.cluster_energy)+"\n"
        output += "end_cluster"

        return output


    def mass( self ) -> float:
        """
        Returns the mass of the cluster in Da
        """
        return self.__mass
