# NewsSpider and Text Clustering with K-means

Ability to scraping <link>https://globalnews.ca/toronto/</link> to collect data, and clustering news stories with K-Means model.

## Set up
Install virtual environments</br>
Install Scikit-learn, NumPy, Pandas and other dependencies from requirement.txt file

## GlobalNews Spider
1. Creating a proxy webserver
2. Using urllib opener to get the content of the main page
3. Find a news URL on the main page
4. Scrape all pages data by regular expression
5. Save each news.html files separately
6. Save news stories in a csv file

## Data Pre-processing
Creating a dataframe from Pandas series, and transform into NumPy array

## K-means clustering with TF-IDF weights
Use scikit-learn implementation of TF-IDF and K-means, build K-Means model with k = 4 for clustering strings

## Output
It returns four groups with index of the cluster [0,1,2,3]
