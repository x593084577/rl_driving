"""
abc.method
"""

from abc import ABCMeta
from abc import abstractmethod
from scipy.integrate import odeint
import numpy as np

class Dynamics(object):
	"""
	"""
	__metaclass__ = ABCMeta
	def __init__(self, initial_state, period=0.1):
		"""
		@Parameters
		initial_state: initial state of the model
		period: sampling period
		"""
		self._initial_state = initial_state
		self._state = initial_state
		self._period = period
		self._timestamp = 0.0

	def step(self, action):
		self._timestamp += self._period
		t = np.linspace(0, self._period, 20)
		if not isinstance(action, tuple):
			action = (action,)
		sol = odeint(self.dynamics, self._state, t, args=action)
		self._state = sol[-1, :]
		return self._state

	@abstractmethod
	def dynamics(self, state, t, action):
		raise NotImplementedError

	def reset(self, state=None):
		if state is None:
			self._state = self._initial_state
		else:
			self._state - state
		self._timestamp = 0.0
	
	@property
	def state(self):
		return self._state
	
	@property
	def time(self):
		return self._timestamp
