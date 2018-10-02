from Agents.DQN_Agents.DQN_Agent_With_Fixed_Q_Targets import DQN_Agent_With_Fixed_Q_Targets

class DDQN_Agent(DQN_Agent_With_Fixed_Q_Targets):

    def __init__(self, config, hyperparameters, agent_name):

        print("Initialising DDQN Agent")
        DQN_Agent_With_Fixed_Q_Targets.__init__(self, config, hyperparameters, agent_name)

    def compute_q_values_for_next_states(self, next_states):
        max_action_indexes = self.qnetwork_local(next_states).detach().argmax(1)        
        Q_targets_next = self.qnetwork_target(next_states).gather(1, max_action_indexes.unsqueeze(1))
        return Q_targets_next 
            

