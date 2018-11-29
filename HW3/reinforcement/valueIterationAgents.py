# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        # value iteration process

        # initialize the values
        for s in self.mdp.getStates():
          self.values[s] = 0

        # do the iteration
        for i in range(self.iterations):
          # copy the values in last iteration
          cur_values = self.values.copy()

          for s in self.mdp.getStates():
            # if it is the terminal state, then value is 0
            if self.mdp.isTerminal(s):
              self.values[s] = 0
            else:
              # Vopt = for all actions choose the max Q_value
              value_max = -float('inf')
              actions = self.mdp.getPossibleActions(s)
              for a in actions:
                temp = self.getQValue(s, a)
                if temp >= value_max:
                  value_max = temp
              cur_values[s] = value_max # update current values    
            # update the self.values
          self.values = cur_values

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # else compute the Q value
        res = 0 # record Q value
        next_list = self.mdp.getTransitionStatesAndProbs(state, action)
        # compute the Q value
        for temp in next_list:
          next_state = temp[0] 
          next_prob = temp[1]
          next_reward = self.mdp.getReward(state, action, next_state)
          # Q_value = for all next_state, compute sum(prob * (reward + gamma * V[next_state]))
          res += next_prob * (next_reward + self.discount * self.values[next_state])
        return res
        # util.raiseNotDefined()

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # if it is the terminal state, return None
        if self.mdp.isTerminal(state):
          return None
        # compute the best policy
        res = None
        q_max = -float('inf') # max Q_value
        actions = self.mdp.getPossibleActions(state) # all possible actions
        # choose the action which has the max Q_value
        for a in actions:
          q_value = self.getQValue(state, a)
          if q_value >= q_max:
            q_max = q_value
            res = a
        return res
       #util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
