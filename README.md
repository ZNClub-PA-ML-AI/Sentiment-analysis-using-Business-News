
# Sentiment-analysis-using-Business-News


----------
This project is dedicated to generating sentiment value from business news about companies & comparing it with the stock market steps
**This project is a part of another parent project ie **
[Research-Platform-Stock-Market](https://github.com/ZNClub-PA-ML-AI)

# Let's begin


# Research & survey based information regarding NLP
## PREPROCESSING
1. keyword filtering
2. html markup filtering
3. unicode filtering

## SENTIMENT EVALUATION
http://text-processing.com/demo/sentiment/
VADER

## GUIDE
https://www.quora.com/What-are-the-best-supervised-learning-algorithms-for-sentiment-analysis-in-text
## PREPROCESSING STEPS INVOLVED IN NLP
1. Noise Removal
2. Named Entity Recognition
3. Noun Clauses

## FEATURES
1. UNIGRAMS,BIGRAMS, TRIGRAMS
  1. with punctuation
  2. without punctuation
2. NAMED ENTITY, NOUN CLAUSES
- all above techniques weighted differently for title,intro,body


## FINAL SCHEMA
date|comp|title|intro|body|feat_1|...|feat_n|opnd| % delta |trend
- date : date time; 2 categories:a)4pm-9am:OPEN b)9am-4pm:CLOSE
- comp : company id
- title : news headline
- intro : news headline intro
- body : content of headline
- feat_n : nlp + lexical techniques applied normalized sentiment scores
- opnd : OPEN Price of Next Day
- % delta : % change between OPEN_today & OPEN_next_day
- trend : duration of positive / negative trend

## HYBRID MODEL ( Part of Parent Project) 
1. IMPLEMENT
  1. MARKET ANALYTICS PREDICTION ( economic approach )
  2. NEWS SENTIMENTAL PREDICTION ( nlp approach for what investors read )
  3. TWITTER SENTIMENTAL PREDICTION ( nlp approach for how investors react )
2. COMPARE PERFORMANCE ON TECHNIQUES BASED ON ACCURACY & TREND
3. APPLY WEIGHTED APPROACH & COMBINE ALL TECHNIQUES

# Git status 


 **The current release version 1.0 has the following features integrated :**

- ddatabase in
