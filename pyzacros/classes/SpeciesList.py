from Species import *

class SpeciesList(list):

    def __str__( self ) -> str:
        """
        Translates the object to a string
        """

        gasSpecies = []
        adsorbedSpecies = []

        for i,specie in enumerate(self):
            if( specie.is_adsorbed() ):
                adsorbedSpecies.append(i)
            else:
                gasSpecies.append(i)

        output = "n_gas_species "+str(len(gasSpecies))+"\n"

        output += "gas_specs_names   "
        for i in gasSpecies:
            output += "%10s"%self[i].symbol
        output += "\n"

        output += "gas_energies      "
        for i in gasSpecies:
            output += "%10s"%self[i].gas_energy
        output += "\n"

        output += "gas_molec_weights "
        for i in gasSpecies:
            #output += "%10s"%self[i].mass
            output += "%10s"%"XXX" # @TODO We need a database with the molecular weights
        output += "\n"

        output += "\n"
        output += "n_surf_species "+str(len(adsorbedSpecies))+"\n"  #TODO Remove the * species

        output += "surf_specs_names  "
        for i in adsorbedSpecies:
            output += "%10s"%self[i].symbol
        output += "\n"

        output += "surf_specs_dent   "
        for i in adsorbedSpecies:
            output += "%10s"%self[i].denticity

        return output


    @staticmethod
    def test():
        """
        Tests the main methods of the object
        """
        print( "---------------------------------------------------" )
        print( ">>> Testing SpeciesList class" )
        print( "---------------------------------------------------" )

        # Adsorbed specie
        myAdsorbedSpecies1 = Species( "H2*", denticity=1 )
        myAdsorbedSpecies2 = Species( "O2*", denticity=1 )

        # Gas specie
        myGasSpecies1 = Species( "H2", gas_energy=0.0 )

        # Gas specie
        myGasSpecies2 = Species( "O2", gas_energy=0.0 )

        # Free adsorption site
        myFreeAdsorptionSite = Species( "*" )

        mySpeciesList = SpeciesList()
        mySpeciesList.append( myAdsorbedSpecies1 )
        mySpeciesList.append( myAdsorbedSpecies2 )
        mySpeciesList.append( myGasSpecies1 )
        mySpeciesList.append( myGasSpecies2 )
        mySpeciesList.append( myFreeAdsorptionSite )

        print(mySpeciesList)

        output = str(mySpeciesList)
        expectedOutput = """\
n_gas_species 2
gas_specs_names           H2        O2
gas_energies             0.0       0.0
gas_molec_weights        XXX       XXX

n_surf_species 3
surf_specs_names         H2*       O2*         *
surf_specs_dent            1         1         0\
"""
        assert( output == expectedOutput )
