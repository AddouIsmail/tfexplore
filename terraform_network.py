import tfstate_classes.tfstate_input as  tfstate_input
import networkx as nx


class stages_dependencies:
    """
        Get dependencies between stages using `terraform_remote_state` key
    """
    def __init__(
            self, 
            stages_states: tfstate_input, 
        ):     
        self.stages = stages_states.tfstates
        self.dependencies = dict()
        for stage_name, state in self.stages.items():
            # WARNING: the system doen't support conflicts in filenames
            self.dependencies[stage_name] = self.__get_remote_states(state)
    
    def __get_remote_states(self, state_dict):
        # get only remote states objects
        remote_state_objects = filter(
            lambda x: x.get("mode") == "data" and x.get("type") == "terraform_remote_state",
            state_dict["resources"]
        )

        # get only dependent remote states
        remote_states_names = map(
            lambda x: x.get("name"), remote_state_objects
        )

        return list(remote_states_names)

    def get_dependencies(self):
        return self.dependencies


    def build_networkx(self):
        G = nx.Graph()
        
        for stage_name in self.stages:
            G.add_node(stage_name)

        for stage_name, stage_dependencies in self.dependencies.items():
            for s_dep in stage_dependencies:
                G.add_edge(s_dep, stage_name)
                
        return G
