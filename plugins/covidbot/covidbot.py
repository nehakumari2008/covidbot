from errbot import BotPlugin, botcmd, arg_botcmd
import get_stats


class CovidBot(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def tryme(self, msg, args):  # a command callable with !tryme
        """
        Execute to check if Errbot responds to command.
        Feel free to tweak me to experiment with Errbot.
        You can find me in your init directory in the subdirectory plugins.
        """
        return 'It *works* !'  # This string format is markdown.

    @botcmd
    def covid(self, msg, args):
        stats = get_stats.get_numbers(args)
        if stats:
            return "Cases for " + args + " is, Active: " + str(
                stats[0]) + " New: " + str(stats[1]) + " Recovered: " + str(stats[2])
        else:
            state = get_stats.get_state_wise_data(args)
            if state:
                response = "Cases for " + args + " is, Active: " + str(state[0]) + " Confirmed: " + str(state[1]) + " Recovered: " + str(state[2])
                return response
            else:
                data = get_stats.get_city_wise_data(args)
                if data:
                    response = "Cases for " + args + ",Active: " + str(data['active']) + ", Confirmed: " + str(data['confirmed']) \
                               + "(" + str(data['delta']['confirmed']) + ")" + ", Recovered: " + str(data['recovered']) \
                               + "(" + str(data['delta']['recovered']) + ")"
                    return response
                else:
                    return "Not able to locate your Country or State or City. Please try again."
