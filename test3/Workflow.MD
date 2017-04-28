
# WORKFLOW OF PROJECT

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





