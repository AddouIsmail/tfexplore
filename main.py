import sys
import tfstate_classes.s3 as s3
import tfstate_classes.local as local

from terraform_network import stages_dependencies
from pyvis.network import Network


if __name__ == "__main__":
    args = sys.argv
    tfstate_type = args[1]
    tfstate_location = args[2]

    if tfstate_type == "s3":
        states = s3.terraform_states(tfstate_location)
    elif tfstate_type == "local":
        states = local.terraform_states(tfstate_location)
    else:
        raise NotImplementedError()
    
    deps = stages_dependencies(states)
    graph = deps.build_networkx()
    nt = Network('700px', '1000px')
    nt.from_nx(graph)
    nt.show("index.html")
