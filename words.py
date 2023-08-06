import csv

# List of words related to women harassment
words = ["Abuse", "Assault", "Bullying", "Coercion", "Denial", "Discrimination", "Exploitation", "Groping", "Harassment",
         "Humiliation", "Inappropriate", "Intimidation", "Molestation", "Objectification", "Oppression", "Persecution",
         "Predation", "Rape", "Sexism", "Sexual", "Stalking", "Subjugation", "Threat", "Trauma", "Violation", "Abduction",
         "Aggression", "Assailant", "Attack", "Attacker", "Confrontation", "Controversial", "Cowardice", "Cruel",
         "Degrade", "Denigration", "Desperate", "Despicable", "Destruction", "Disgust", "Domination", "Force", "Guilt",
         "Hate", "Hurt", "Insult", "Manipulation", "Misogyny", "Pain", "Revenge", "Suffering","Abduction", "Abhorrence", "Abhorrent", "Abuse", "Abusive", "Accusation", "Accuse", "Acid", "Addict", "Addiction",
         "Aggression", "Aggressive", "Aggressor", "Alarm", "Alarming", "Allege", "Allegation", "Alleged", "Allegedly",
         "Altercation", "Ambush", "Amorous", "Annoyance", "Annoyed", "Annoying", "Annoyingly", "Anxiety", "Anxious",
         "Apology", "Appalled", "Appalling", "Arrogance", "Assailant", "Assault", "Assaulted", "Assaulting", "Attack",
         "Attacker", "Atrocious", "Atrocity", "Attractiveness", "Badger", "Badgering", "Bait", "Battered", "Battering",
         "Beaten", "Bewildered", "Bewildering", "Bewilderment", "Bitchy", "Blackmail", "Blame", "Blamed", "Blaming",
         "Bloodshed", "Bloody", "Breach", "Breaking", "Brutal", "Brutality", "Bully", "Bullying", "Catastrophic",
         "Chase", "Cheated", "Cheating", "Coercion", "Cold-hearted", "Complain", "Complaining", "Compromise",
         "Conflict", "Confrontation", "Consequence", "Contempt", "Contemptible", "Contemptuous", "Controversial",
         "Convicted", "Cowardice", "Cowering", "Cruel", "Cruelty", "Culpable", "Cursed", "Cussing", "Dangerous",
         "Darkness", "Degrade", "Demeaning", "Denigration", "Deny", "Depression", "Desire", "Desolate", "Despair",
         "Desperation", "Despicable", "Destruction", "Detain", "Detention", "Devastated", "Devastating", "Devastation",
         "Deviant", "Deviation", "Devilish", "Devotion", "Die", "Difficulty", "Dilemma", "Disappointed", "Disappointing",
         "Disappointment", "Disapproval", "Disapprove", "Disaster", "Disastrous", "Discrimination", "Disgust", "Disgusting",
         "Dishonest", "Disillusionment", "Dislike", "Dismay", "Disobey", "Disorderly", "Disparage", "Displeased",
         "Displeasing", "Disrespect", "Disrespectful", "Disruption", "Dissatisfied", "Dissatisfaction", "Distracted",
         "Distraught", "Distress", "Distressed", "Distressing", "Disturb", "Disturbance", "Disturbed", "Divert",
         "Diversion", "Divest", "Divestment", "Divorce", "Doubt", "Dread", "Dreadful", "Dreadfully", "Duplicity",
         "Embarrassed", "Embarrassing", "Embarrassment", "Enforce", "Enforcement","assault",
         "coerce",
         "catcall",
         "chauvinism",
         "cyberstalking",
         "discrimination",
         "domestic abuse",
         "exclusion",
         "fondle",
         "groping",
         "harassment",
         "hostility",
         "humiliation",
         "impropriety",
         "inappropriate",
         "intimidation",
         "lewdness",
         "molestation",
         "misogyny",
         "objectification",
         "offensive",
         "oppression",
         "peeping",
         "perpetrator",
         "predator",
         "profanity",
         "proposition",
         "rape",
         "rejection",
         "sexism",
         "sexualization",
         "slander",
         "stalking",
         "subjugation",
         "suffocation",
         "surveillance",
         "torture",
         "touching",
         "trauma",
         "trolling",
         "unwanted",
         "violation",
         "vulgarity",
         "voyeurism",
         "abuse",
         "aggression",
         "assailant",
         "belittling",
         "catcalling",
         "chauvinistic",
         "coercion",
         "contempt",
         "cruelty",
         "degradation",
         "denigration",
         "deprivation",
         "devaluing",
         "disdain",
         "disparagement",
         "distrust",
         "domination",
         "emotional abuse",
         "enmity",
         "exploitation",
         "fear",
         "fondling",
         "gaze",
         "grabbing",
         "harasser",
         "humiliating",
         "improper",
         "indecent",
         "infliction",
         "insult",
         "intentional",
         "intimidate",
         "leering",
         "lust",
         "manhandling",
         "menace",
         "molesting",
         "mortification",
         "name-calling",
         "offender",
         "objectify",
         "overpower",
         "perpetuate",
         "physical abuse",
         "predatory",
         "profane",
         "provocation",
         "psychological abuse",
         "rape culture",
         "revulsion",
         "sarcasm",
         "sexual harassment",
         "sexual misconduct",
         "sexual violence",
         "shaming",
         "smirking",
         "stigmatization",
         "subjection",
         "suppression",
         "threatening",
         "torturing",
         "toxic masculinity",
         "uninvited",
         "unwanted advances",
         "violence",
         "voyeristic"]
'''
# Create a new CSV file and write the words
with open("women_harassment_words.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Words"])
    for word in words:
        writer.writerow([word])




# Function to preprocess the tweets
def preprocess_tweet(tweet):
    # Remove URLs
    tweet = re.sub(r"http\S+", "", tweet)
    # Remove user mentions
    tweet = re.sub(r"@\S+", "", tweet)
    # Remove hashtags
    tweet = re.sub(r"#\S+", "", tweet)
    # Remove special characters and digits
    tweet = re.sub(r"[^a-zA-Z]", " ", tweet)
    # Convert to lowercase
    tweet = tweet.lower()
    # Tokenize the tweet
    tokens = word_tokenize(tweet)
    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    # Join the tokens back into a string
    processed_tweet = " ".join(filtered_tokens)
    return processed_tweet

# Retrieve tweets using snscrape
tweets_list = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper("women harassment lang:en").get_items()):
    tweets_list.append([tweet.date, tweet.id, tweet.rawContent])
    # Break after collecting 50 tweets
    if i == 50000 and i%1000==0:
        print(f"{i} tweets scraped.")
        break'''

'''search_terms = "women harassment:en"
start_date = "2002-01-01"
end_date = "2022-01-01"

        # Define a list to hold the tweets
tweets_list = []
total_tweets=None

        # Use snscrape to search for tweets
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'{search_terms} since:{start_date} until:{end_date}').get_items()):
            tweets_list.append([tweet.date, tweet.id, tweet.rawContent])

            # Print a message every 1000 tweets scraped
            if  i > 0 and i%500==0:
                print(f"{i} tweets scraped.")
               '''
'''import scrapy
import datetime
class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    allowed_domains = ['twitter.com']
    
    def start_requests(self):
        search_terms = "women harassment:en"
        start_date = datetime.date(2002, 1, 1)
        end_date = datetime.date(2022, 1, 1)
        
        base_url = 'https://twitter.com/search?q={} since:{} until:{}&src=typed_query'
        url = base_url.format(search_terms, start_date, end_date)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        tweets = response.xpath('//article[@data-testid="tweet"]')
        for tweet in tweets:
            date = tweet.xpath('.//time/@datetime').get()
            tweet_id = tweet.xpath('.//@data-item-id').get()
            raw_content = tweet.xpath('.//div[@class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0"]/text()')
            yield {
                'date': date,
                'id': tweet_id,
                'content': raw_content.get(),
            }  '''        