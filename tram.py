import random
import copy

class TramMDP:
    def __init__(self, fail_prob=0.5, length=10, init_state=1, gamma=1):
        self.length = length
        self.states = set(range(1, self.length+1))
        self.gamma = gamma
        assert self.length > 1, "length should be greater than 1"
        self.fail_prob = fail_prob
        self.state = init_state
        self.actions = ("walk", "tram")
        self.utility = 0
    
    def get_actions(self):
        return self.actions
    
    def get_states(self):
        return self.states

    def get_state(self):
        return self.state
    
    def get_info(self, state, action):
        if action == "walk":
            return [(min(state+1, self.length), 1)]
        elif action == "tram":
            return [(min(2*state, self.length), 1 - self.fail_prob), (state, self.fail_prob)]

    def is_terminal(self, state):
        return state == self.length
     
    def step(self, action):
        if action == "walk":
            self.state += 1
        elif action == "tram":
            random_num = random.random()
            if random_num >= self.fail_prob:
                self.state = min(2 * self.state, self.length)
        else:
            raise ValueError("Action must be 'walk' or 'tram'")
        reward = -1
        self.utility = reward + self.gamma * self.utility
        return self.state, reward
    
    def reset(self):
        self.utility = 0
        self.state = 1

class SimplestPolicy():
    def __init__(self, action):
        self.action = action
    
    def act(self, state):
        return self.action

class PolicyEvaluation:
    def __init__(self, mdp, policy):
        self.mdp = mdp
        self.policy = policy
        self.values = {key: 0 for key in self.mdp.get_states()}
    
    def play_game(self):
        #<YOUR CODE>
        pass
    
    def evaluate(self, num_iter):
        #<YOUR CODE>
        pass
    
    def reset(self):
        self.values = {key: 0 for key in self.mdp.get_states()}

class DeterministicPolicy:
    def __init__(self, actions=dict()):
        self.actions = actions
    
    def act(self, state):
        return self.actions[state]

class PolicyIteration:
    def __init__(self, mdp, policy):
        self.mdp = mdp
        self.policy = policy
    
    def step(self):
        # <YOUR CODE>
        pass

    def run(self, num_iter):
        for _ in range(num_iter):
            self.step()
        return self.policy

class ValueIteration:
    def __init__(self, mdp):
        self.mdp = mdp
        self.values = {key: 0 for key in self.mdp.get_states()}

    def step(self):
        # <YOUR CODE>
        pass
    
    def run(self, num_iter):
        for _ in range(num_iter):
            self.step()
    
    def get_policy(self):
        policy = DeterministicPolicy()
        # <YOUR CODE>
        return policy

                        


def play_game(mdp:TramMDP, policy):
    print(f"State = {mdp.get_state()}")
    while not mdp.is_terminal(mdp.get_state()):
        action = policy.act(mdp.get_state())
        print(action)
        state, _ = mdp.step(action)
        print(f"State = {mdp.get_state()}")
    print(f"Terminal state. Utility = {mdp.utility}")

def main(args=None):
    mdp = TramMDP(fail_prob=0.15, gamma=0.9)
    # policy = SimplestPolicy("walk")
    actions = dict()
    for i in range(1, 11):
        if i == 1:
            actions[i] = "tram"
        else:
            actions[i] = "tram"
    policy = DeterministicPolicy(actions)
    play_game(mdp, policy)
    # evaluator = PolicyEvaluation(mdp, policy)
    # print(evaluator.evaluate(1000))
    # policy_iter = PolicyIteration(mdp, policy)
    # final_policy = policy_iter.run(100)
    # print(final_policy.actions)
    # value_iter = ValueIteration(mdp)
    # value_iter.run(1000)
    # vpolicy = value_iter.get_policy()
    # print(vpolicy.actions)
    
if __name__ == '__main__':
    main()
    

