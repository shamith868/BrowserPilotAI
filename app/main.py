from scrapers.github_scraper import GitHubScraper


def main():

    keyword = input("Enter repository keyword: ")

    scraper = GitHubScraper()

    scraper.scrape(keyword)


if __name__ == "__main__":
    main()