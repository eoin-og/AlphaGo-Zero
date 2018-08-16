import model
from xandos import xandos
from connect4 import Connect4
from solver import Solver


if __name__ == "__main__":

	game = xandos()
	nnet_class = model.XandosNet

	num_iters = 5
	num_sims = 25
	num_episodes = 25
	num_epoch = 10
	num_battles = 20

	solver = Solver(game=game,
					nnet_class=nnet_class,
					num_iters=num_iters,
					num_sims=num_sims,
					num_episodes=num_episodes,
					num_epoch=num_epoch,
					num_battles=num_battles)

	solver.policy_iteration()
