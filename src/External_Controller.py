class ExternalController:
    """ Receives and acts upon messages received from the other computer. """

    def __init__(self, game):
        self.game = game
        self.repeat_connection = False

    # noinspection PyUnusedLocal
    def act_on_message_received(self, message, sender_id):
        """
        Moves this Controller's Player to the position
        that was sent by the other computer.
        Parameters:
          -- message: Must be a string that represents two non-negative
                      integers separated by one or more spaces, e.g. "100 38"
          -- sender_id: The number of the computer sending the message
                        (unused by this method)
          :type message:   str
          :type sender_id: int
        """
        decode = message.split("?")
        if decode[0] == "state":
            state = decode[1].split()
            self.game.players[int(state[0]) - 1].set_position(float(state[1]), float(state[2]), float(state[3]), float(state[4]))
        elif decode[0] == "fire":
            fire = decode[1].split()
            self.game.players[int(fire[0]) - 1].set_position(float(fire[1]), float(fire[2]), self.game.players[int(fire[0]) - 1].tank_angle, float(fire[3]))
            self.game.players[int(fire[0]) - 1].fire()
        elif decode[0] == "maprequest":
            if self.game.who_am_i == 1:
                self.game.sender.send_message("map?" + self.game.map.seed)
        elif decode[0] == "death":
            death = decode[1].split()
            self.game.players[int(death[0]) - 1].explode()
            self.game.players[int(death[0]) - 1].score -= 1
            self.game.players[int(death[1]) - 1].score += 1
        elif decode[0] == "map":
            self.game.map.generate_map(str(decode[1]))
            self.game.set_start_positions()
        elif decode[0] == "connection":
            self.game.connected_computers.append(int(decode[1]))
            if not self.repeat_connection:
                self.game.sender.send_message("connection?" + str(self.game.who_am_i))
                self.repeat_connection = True

