def get_parameter_values():
    return {
        "1 + dlnf/dlnc": 1.0,
        "Ambient temperature [K]": 294.85,
        "Anion stoichiometry": 1.0,
        "Cation stoichiometry": 1.0,
        "Cation transference number": 0.7,
        "Cell cooling surface area [m2]": 0.154,
        "Cell volume [m3]": 0.00027,
        "Current function [A]": 1.0,
        "Darken thermodynamic factor": darken_thermodynamic_factor_Chapman1968,
        "Edge heat transfer coefficient [W.m-2.K-1]": 0.3,
        "Electrode height [m]": 0.114,
        "Electrode width [m]": 0.065,
        "Electrolyte conductivity [S.m-1]": conductivity_Gu1997,
        "Electrolyte diffusivity [m2.s-1]": diffusivity_Gu1997,
        "Electrolyte viscosity [kg.m-1.s-1]": viscosity_Chapman1968,
        "Electrons in hydrogen reaction": 2.0,
        "Electrons in oxygen reaction": 4.0,
        "Hydrogen diffusivity [m2.s-1]": 4.5e-09,
        "Hydrogen reference OCP vs SHE [V]": 0.0,
        "Initial State of Charge": 1.0,
        "Initial oxygen concentration [mol.m-3]": 0.0,
        "Initial temperature [K]": 294.85,
        "Lower voltage cut-off [V]": 1.75,
        "Maximum porosity of negative electrode": 0.53,
        "Maximum porosity of positive electrode": 0.57,
        "Maximum porosity of separator": 0.92,
        "Maximum temperature [K]": 333.15,
        "Molar mass of anions [kg.mol-1]": 0.097,
        "Molar mass of cations [kg.mol-1]": 0.001,
        "Molar mass of hydrogen molecules [kg.mol-1]": 0.002,
        "Molar mass of oxygen molecules [kg.mol-1]": 0.032,
        "Molar mass of water [kg.mol-1]": 0.01801,
        "Molar volume of lead [m3.mol-1]": 1.82539682539683e-05,
        "Molar volume of lead sulfate [m3.mol-1]": 4.81717011128776e-05,
        "Molar volume of lead-dioxide [m3.mol-1]": 2.54797441364606e-05,
        "Negative current collector density [kg.m-3]": 11300.0,
        "Negative current collector specific heat capacity [J.kg-1.K-1]": 130.0,
        "Negative current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Negative current collector thermal conductivity [W.m-1.K-1]": 35.0,
        "Negative current collector thickness [m]": 0.0,
        "Negative electrode Bruggeman coefficient (electrode)": 1.5,
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Negative electrode capacity [C.m-3]": 3473000000.0,
        "Negative electrode cation signed stoichiometry": 1.0,
        "Negative electrode conductivity [S.m-1]": 4800000.0,
        "Negative electrode density [kg.m-3]": 11300.0,
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Negative electrode electrons in reaction": 2.0,
        "Negative electrode exchange-current density [A.m-2]": lead_exchange_current_density_Sulzer2019,
        "Negative electrode morphological parameter": 0.6,
        "Negative electrode open-circuit potential [V]": lead_ocp_Bode1977,
        "Negative electrode pore size [m]": 1e-07,
        "Negative electrode reference exchange-current density (hydrogen) [A.m-2]": 1.56e-11,
        "Negative electrode reference exchange-current density (oxygen) [A.m-2]": 2.5e-32,
        "Negative electrode specific heat capacity [J.kg-1.K-1]": 130.0,
        "Negative electrode surface area to volume ratio [m-1]": 2300000.0,
        "Negative electrode thermal conductivity [W.m-1.K-1]": 35.0,
        "Negative electrode thickness [m]": 0.0009,
        "Negative electrode volumetric capacity [C.m-3]": 3473000000.0,
        "Negative tab centre y-coordinate [m]": 0.06,
        "Negative tab centre z-coordinate [m]": 0.114,
        "Negative tab heat transfer coefficient [W.m-2.K-1]": 10.0,
        "Negative tab width [m]": 0.04,
        "Nominal cell capacity [A.h]": 17.0,
        "Number of cells connected in series to make a battery": 6.0,
        "Number of electrodes connected in parallel to make a cell": 8.0,
        "Oxygen diffusivity [m2.s-1]": 2.1e-09,
        "Oxygen reference OCP vs SHE [V]": 1.229,
        "Partial molar volume of anions [m3.mol-1]": 3.15e-05,
        "Partial molar volume of cations [m3.mol-1]": 1.35e-05,
        "Partial molar volume of hydrogen molecules [m3.mol-1]": 2.31e-05,
        "Partial molar volume of oxygen molecules [m3.mol-1]": 3.21e-05,
        "Partial molar volume of water [m3.mol-1]": 1.75e-05,
        "Positive current collector density [kg.m-3]": 9375.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 256.0,
        "Positive current collector surface heat transfer coefficient [W.m-2.K-1]": 0.0,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 35.0,
        "Positive current collector thickness [m]": 0.0,
        "Positive electrode Bruggeman coefficient (electrode)": 1.5,
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Positive electrode capacity [C.m-3]": 2745000000.0,
        "Positive electrode cation signed stoichiometry": 3.0,
        "Positive electrode conductivity [S.m-1]": 80000.0,
        "Positive electrode density [kg.m-3]": 9375.0,
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode electrons in reaction": 2.0,
        "Positive electrode exchange-current density [A.m-2]": lead_dioxide_exchange_current_density_Sulzer2019,
        "Positive electrode morphological parameter": 0.6,
        "Positive electrode open-circuit potential [V]": lead_dioxide_ocp_Bode1977,
        "Positive electrode oxygen exchange-current density [A.m-2]": oxygen_exchange_current_density_Sulzer2019,
        "Positive electrode pore size [m]": 1e-07,
        "Positive electrode reference exchange-current density (hydrogen) [A.m-2]": 0.0,
        "Positive electrode specific heat capacity [J.kg-1.K-1]": 256.0,
        "Positive electrode surface area to volume ratio [m-1]": 23000000.0,
        "Positive electrode thermal conductivity [W.m-1.K-1]": 35.0,
        "Positive electrode thickness [m]": 0.00125,
        "Positive electrode volumetric capacity [C.m-3]": 2745000000.0,
        "Positive tab centre y-coordinate [m]": 0.147,
        "Positive tab centre z-coordinate [m]": 0.114,
        "Positive tab heat transfer coefficient [W.m-2.K-1]": 10.0,
        "Positive tab width [m]": 0.04,
        "Reference oxygen molecule concentration [mol.m-3]": 1000.0,
        "Reference temperature [K]": 294.85,
        "Separator Bruggeman coefficient (electrolyte)": 1.5,
        "Separator density [kg.m-3]": 1680.0,
        "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
        "Separator thermal conductivity [W.m-1.K-1]": 0.04,
        "Separator thickness [m]": 0.0015,
        "Signed stoichiometry of cations (hydrogen reaction)": 2.0,
        "Signed stoichiometry of cations (oxygen reaction)": 4.0,
        "Signed stoichiometry of hydrogen (hydrogen reaction)": -1.0,
        "Signed stoichiometry of oxygen (oxygen reaction)": 1.0,
        "Signed stoichiometry of water (oxygen reaction)": -1.0,
        "Total heat transfer coefficient [W.m-2.K-1]": 10.0,
        "Typical current [A]": 1.0,
        "Typical electrolyte concentration [mol.m-3]": 5650.0,
        "Typical oxygen concentration [mol.m-3]": 1000.0,
        "Upper voltage cut-off [V]": 2.42,
        "Volume change factor": 1.0,
    }
