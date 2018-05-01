# Sentiment-analysis-using-Business-News

## PREPROCESSING
1. keyword filtering
2. html markup filtering
3. unicode filtering

## SENTIMENT EVALUATION
http://text-processing.com/demo/sentiment/
## NGRAMS
http://stackoverflow.com/questions/32441605/generating-ngrams-unigrams-bigrams-etc-from-a-large-corpus-of-txt-files-and-t
## GUIDE
https://www.quora.com/What-are-the-best-supervised-learning-algorithms-for-sentiment-analysis-in-text
## PREPROCESSING INVOLVED IN NLP
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

## HYBRID MODEL
1. IMPLEMENT
  1. MARKET ANALYTICS PREDICTION ( economic approach )
  2. NEWS SENTIMENTAL PREDICTION ( nlp approach for what investors read )
  3. TWITTER SENTIMENTAL PREDICTION ( nlp approach for how investors react )
2. COMPARE PERFORMANCE ON TECHNIQUES BASED ON ACCURACY & TREND
3. APPLY WEIGHTED APPROACH & COMBINE ALL TECHNIQUES


## WORKFLOW OF PROJECT

- livemint_spider.py >> _data.csv,_data_body.csv 
    data[title,intro, href, datetime] 
    data_body[href,body] 
- _data.csv,_data_body.csv + idgen.py >> data_o1.csv,data_o2.csv
    idgen.py : generates ID from href and assigns to each record 
    data_o1.csv [id,...]
    data_o2.csv [id,...]
- data_o2.csv + preprocessor.py >> data_o3.csv 

- data_o1.csv, data_o3.csv + merge.py >> data_joined_2.csv 

- data_joined_2.csv + normalizer.py >> normalized.csv 

- normalized.csv + sentiment.py >> labeled.csv 

- labeled.csv, company_keyword.xlsx + keyword_extraction.py >> REL.csv 

- REL.csv + pre_prediction.py >> REL_score_open.csv, REL_score_close.csv 

- REL_score_open.csv,REL_score_close.csv + merge_sentiment.py >> REL_sentiment.csv 

- REL_sentiment.csv, NSE-RELIANCE.csv + merge_quandl.py >> REL_qs.csv 







