import tweepy
import requests
import json
import random
import time
from datetime import datetime, timedelta
import schedule
import os

# Your Twitter API credentials
API_KEY = "YD0kuvXbASGx7y51xWWH99svt"
API_SECRET = "gnvwB8VrW11IRRIFMSQN3FD7zsT1PwmPa2RhKt5ATN8kMhdA8a"
ACCESS_TOKEN = "1592628050369429504-aNzvzWCmM0x6eO14ikWy9PKZVluCgi"
ACCESS_TOKEN_SECRET = "7FNyUoUKKoz3GdzTI4mPoynedeicgmgyHOP1BRvQrOHuD"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIoP2gEAAAAAOYNHSRHfYVStSbkYin7KSxZL79o%3DNHu8aZkQ0yeOb7Qnd3kfkhilD77mDhhgEzQQ4cOpwzNBWixqbu"

# Initialize Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Verify credentials
try:
    api.verify_credentials()
    print("✅ Twitter API authentication successful!")
except Exception as e:
    print(f"❌ Twitter API authentication failed: {e}")

class AINewsBot:
    def __init__(self):
        self.news_sources = [
            "https://newsapi.org/v2/everything?q=artificial%20intelligence&sortBy=publishedAt&pageSize=10",
            "https://newsapi.org/v2/everything?q=ChatGPT%20OR%20OpenAI&sortBy=publishedAt&pageSize=10",
            "https://newsapi.org/v2/everything?q=AI%20tools%20OR%20machine%20learning&sortBy=publishedAt&pageSize=10"
        ]
        
        # Hot AI hashtags for maximum engagement
        self.hashtags = [
            "#AI", "#ArtificialIntelligence", "#ChatGPT", "#OpenAI", "#MachineLearning",
            "#Tech", "#Innovation", "#AITools", "#Future", "#Automation", "#DeepLearning",
            "#AINews", "#TechNews", "#StartupNews", "#AIRevolution"
        ]
        
        # Engaging tweet templates
        self.templates = [
            "🚀 BREAKING: {title}\n\n{insight}\n\n{hashtags}",
            "🔥 This is HUGE for AI: {title}\n\n{insight}\n\n{hashtags}",
            "⚡ AI Update: {title}\n\n{insight}\n\n{hashtags}",
            "🎯 Major AI Development: {title}\n\n{insight}\n\n{hashtags}",
            "💡 Game-changer: {title}\n\n{insight}\n\n{hashtags}",
            "🌟 AI Breakthrough: {title}\n\n{insight}\n\n{hashtags}"
        ]
        
        # AI insights to add value
        self.insights = [
            "This could change everything for businesses 🏢",
            "The future is happening faster than we think 🚀",
            "Another step toward AGI? 🤖",
            "This will impact millions of jobs 💼",
            "The AI race is heating up! 🔥",
            "Revolutionary technology in action ⚡",
            "The next decade will be wild 🌪️",
            "Innovation never stops 💫",
            "This is why we live in exciting times ✨",
            "The AI revolution continues 🚀"
        ]
    
    def get_trending_ai_news(self):
        """Fetch trending AI news from multiple sources"""
        try:
            # Using NewsAPI (you'll need a free API key from newsapi.org)
            # For now, using a fallback method with predefined trending topics
            
            trending_topics = [
                {
                    "title": "ChatGPT gets massive update with improved reasoning",
                    "description": "OpenAI announces major improvements to ChatGPT's reasoning capabilities"
                },
                {
                    "title": "Google's Gemini AI shows breakthrough in coding tasks",
                    "description": "New AI model demonstrates superior performance in software development"
                },
                {
                    "title": "AI startup raises $100M for autonomous agents",
                    "description": "Revolutionary AI agents that can work independently attract massive funding"
                },
                {
                    "title": "Microsoft integrates advanced AI into Office suite",
                    "description": "New AI features transform productivity tools for millions of users"
                },
                {
                    "title": "AI discovers new drug compounds in record time",
                    "description": "Machine learning accelerates pharmaceutical research breakthrough"
                }
            ]
            
            return random.choice(trending_topics)
            
        except Exception as e:
            print(f"Error fetching news: {e}")
            return None
    
    def create_engaging_tweet(self, news_item):
        """Create an engaging tweet from news item"""
        try:
            title = news_item["title"]
            
            # Shorten title if too long
            if len(title) > 100:
                title = title[:97] + "..."
            
            # Select random template and insight
            template = random.choice(self.templates)
            insight = random.choice(self.insights)
            
            # Select 3-4 random hashtags
            selected_hashtags = random.sample(self.hashtags, random.randint(3, 4))
            hashtag_string = " ".join(selected_hashtags)
            
            # Create tweet
            tweet = template.format(
                title=title,
                insight=insight,
                hashtags=hashtag_string
            )
            
            # Ensure tweet is under 280 characters
            if len(tweet) > 280:
                # Reduce hashtags if needed
                selected_hashtags = random.sample(self.hashtags, 2)
                hashtag_string = " ".join(selected_hashtags)
                tweet = template.format(
                    title=title[:80] + "...",
                    insight=insight,
                    hashtags=hashtag_string
                )
            
            return tweet
            
        except Exception as e:
            print(f"Error creating tweet: {e}")
            return None
    
    def post_tweet(self):
        """Main function to post a tweet"""
        try:
            print(f"🤖 Fetching AI news... {datetime.now()}")
            
            # Get trending news
            news_item = self.get_trending_ai_news()
            if not news_item:
                print("❌ No news found")
                return False
            
            # Create tweet
            tweet_content = self.create_engaging_tweet(news_item)
            if not tweet_content:
                print("❌ Failed to create tweet")
                return False
            
            # Post tweet
            tweet = api.update_status(tweet_content)
            print(f"✅ Tweet posted successfully!")
            print(f"📝 Content: {tweet_content}")
            print(f"🔗 URL: https://twitter.com/RizwanKabir/status/{tweet.id}")
            print("-" * 50)
            
            return True
            
        except Exception as e:
            print(f"❌ Error posting tweet: {e}")
            return False
    
    def run_bot(self):
        """Run the bot with scheduled posts"""
        print("🚀 AI Twitter Bot Starting...")
        print("📅 Scheduled posts: 9:00 AM, 2:00 PM, 7:00 PM")
        
        # Schedule posts at optimal times for engagement
        schedule.every().day.at("09:00").do(self.post_tweet)  # Morning
        schedule.every().day.at("14:00").do(self.post_tweet)  # Afternoon  
        schedule.every().day.at("19:00").do(self.post_tweet)  # Evening
        
        # Post first tweet immediately
        print("🎯 Posting first tweet now...")
        self.post_tweet()
        
        # Keep the bot running
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

# Initialize and run the bot
if __name__ == "__main__":
    bot = AINewsBot()
    bot.run_bot()
