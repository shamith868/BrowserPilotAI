from agent.ai_agent import AIAgent


def main():

    agent = AIAgent()

    command = input("What do you want me to do?\n\n> ")

    agent.run(command)


if __name__ == "__main__":
    main()