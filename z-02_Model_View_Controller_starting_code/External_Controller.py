class ExternalController:
    """ Receives and acts upon messages received from the other computer. """

    def __init__(self, zombie):
        self.zombie = zombie  # type: Player

    # noinspection PyUnusedLocal
    def act_on_message_received(self, message, sender_id):
        """
        Moves this Controller's "zombie" Player to the position
        that was sent by the other computer.
        Parameters:
          -- message: Must be a string that represents two non-negative
                      integers separated by one or more spaces, e.g. "100 38"
          -- sender_id: The number of the computer sending the message
                        (unused by this method)
          :type message:   str
          :type sender_id: int
        """
        x = float(message.split()[0])
        y = float(message.split()[1])
        self.zombie.move_to(x, y)