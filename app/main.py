from agent.browser_agent import BrowserAgent


def main():
    agent = BrowserAgent()

    agent.scrape_quotes()

    agent.close()


if __name__ == "__main__":
    main()