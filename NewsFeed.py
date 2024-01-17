import re
import os
import requests
from dotenv import load_dotenv
from datetime import date
import webbrowser
import requests
from datetime import date

load_dotenv()
api = os.environ.get('api')

class NewsFetcher:
    def __init__(self):
        self.default_country = "in"
        self.default_category = "general"
        self.default_num = 2
        self.Specific_news_area = "in"

    def fetch_news(self, category, country, num):
        url = f"https://newsapi.org/v2/top-headlines?from={date.today()}&country={country}&category={category}&language=en&apiKey=02dc2dc240504ddd909c8fa5233ce53b"
        response = requests.get(url)

        try:
            response.raise_for_status()  # Check for HTTP errors
            data = response.json()
            articles = data.get('articles')

            if articles:
                news_list = [f"{category} news, {country}"] + [title['title'] for title in articles[:num]]
            else:
                news_list = [f"No articles found for {category} news in {country}"]

            return news_list

        except requests.exceptions.HTTPError as errh:
            return [f"HTTP Error: {errh}"]
        except requests.exceptions.ConnectionError as errc:
            return [f"Error Connecting: {errc}"]
        except requests.exceptions.Timeout as errt:
            return [f"Timeout Error: {errt}"]
        except requests.exceptions.RequestException as err:
            return [f"Something went wrong: {err}"]

    def parse_command(self, command):
        command = command.lower()
        country_match = re.search(r'in|us|america', command)
        category_match = re.search(r'tech|technology|science|general', command)
        num_match = re.search(r'\b\d+\b', command)

        country = country_match.group() if country_match else self.default_country
        category = category_match.group() if category_match else self.default_category

        # Set default number to 10 if the country is the US
        num = int(num_match.group()) if num_match else self.default_num
        if country == "us" and not num_match:
            num = 10

        # Handle variations of country names
        if "america" in command:
            country = "us"

        # Additional logic to set category based on user input
        if "tech" in command:
            category = "technology"
        elif "science" in command:
            category = "science"

        self.Specific_news_area = country

        # Check if no specific data is provided in the command
        if not category_match and not country_match and not num_match:
            # Fetch 2 news from each case if no specific data is provided
            news_list = []
            news_list += self.fetch_news("technology", "us", 2)
            news_list += self.fetch_news("technology", "in", 2)
            news_list += self.fetch_news("general", "us", 2)
            news_list += self.fetch_news("science", "in", 2)
            news_list += self.fetch_news("science", "us", 2)
            return news_list

        return self.fetch_news(category, country, num)

    def execute_command(self, command):
        result = self.parse_command(command)
        return result

    def Specific_news(self,command):
        num = command.find("of")
        query = command[num + 3:]
        url = f"https://newsapi.org/v2/top-headlines?everything?q={query}&country={self.Specific_news_area}&from={date.today()}&language=en&apiKey=02dc2dc240504ddd909c8fa5233ce53b"
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        articles = data.get('articles')
        for i in articles:
            link = i["urlToImage"]
            content = str(i["content"])
            url = i['url']
            content = content.lower()
            query = query.lower()
            if query in content:
                webbrowser.open(link)
                return i["content"] + f" , if you wanna know about this article click this link boss {url}"


if __name__ == "__main__":
    # Test Case 1: Fetch Top 10 News in India
    news_fetcher = NewsFetcher()
    print(news_fetcher.fetch_news("in",5))
    print(news_fetcher.Specific_news('tell me more about the news of'))


    #news_result = news_fetcher.execute_command("news india 10 science")
    #for item in news_result:
     #   print(item)


    # Test Case 2: Fetch Top 5 Tech News in the US
    # news_result = news_fetcher.execute_command("fetch top 5 tech news in us")
    # for item in news_result:
    #     print(item)

    # Test Case 3: Fetch Top 7 News in America
    # news_result = news_fetcher.execute_command("fetch top 7 news in america")
    # for item in news_result:
    #     print(item)

    # Add more test cases if needed
#53ede28ddb4848d2a7e2ef72fccbf097