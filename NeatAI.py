import neat
import os

class NAI():
    def __init__(self):
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'Examples/config-feedforward.txt')
        self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                    neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                    config_path)

    def run(self):
        # Create the population, which is the top-level object for a NEAT run.
        p = neat.Population(self.config)

        # Add a stdout reporter to show progress in the terminal.
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)

        # Run for up to 50 generations.
        winner = p.run(self.eval_genomes, 50)

        # show final stats
        print('\nBest genome:\n{!s}'.format(winner))

    def eval_genomes(self, genomes, config):
        """
        runs the simulation of the current population of
        birds and sets their fitness based on the distance they
        reach in the game.
        """

        genomes.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genomes, config)