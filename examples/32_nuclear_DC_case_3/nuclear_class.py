import sys

sys.path.insert(0, "/Users/svijaysh/NPP+DCfork/H2Integrate")
from h2integrate.core.h2integrate_model import H2IntegrateModel


DC_DEMAND = 2e6  # 2 GW


class NuclearDC:
    def __init__(self, config):
        self.config = config
        self.h2i = H2IntegrateModel(config)
        self.h2i.setup()

    def print_init_sizes(self):
        print(
            "Nuclear plant initial size (kW):",
            self.h2i.prob.get_val("nuclear.system_capacity"),
        )
        print(
            "Electrcial demand plant initial size (kW):",
            self.h2i.prob.get_val("electrical_load_demand.electricity_demand"),
        )
        print(
            "Electrcial demand plant initial size (kW):",
            self.h2i.prob.get_val("electrical_load_demand.electricity_in"),
        )

    def sweep_nuclear_sizes(self, nuclear_sizes):
        results = []
        for size in nuclear_sizes:
            result = self.run_nuclear_case(size)
            results.append(result)
        return results

    def set_relevant_values(self, nuclear_kw, icx_kw_val):
        self.h2i.prob.set_val("nuclear.system_capacity", nuclear_kw, units="kW")
        self.h2i.prob.set_val(
            "nuclear.electricity_demand", nuclear_kw, units="kW"
        )  # nuclear runs at full capacity
        self.h2i.prob.set_val("grid.interconnection_size", icx_kw_val, units="kW")

    def run_nuclear_case(self, size):
        pass


ndc = NuclearDC("nuclear_datacenter_config_case.yaml")
ndc.print_init_sizes()
ndc.set_relevant_values(nuclear_kw=DC_DEMAND, icx_kw_val=DC_DEMAND)