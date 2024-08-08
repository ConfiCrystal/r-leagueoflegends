# r-leagueoflegends
This project involves the usage of sentiment analysis, a machine-learning adjacent technique in terms of data collection and usage. It is designed to determine the overall sentiment of text after training over a large amount of labelled data. I applied sentiment analysis to the entirety of the r/leagueoflegends subreddit in order to try to find any trends in the kinds of posts made over the years.

My sentiment analysis model has three potential classifications, rather than the normal two. These are positive, negative, and an added neutral since much of my data had little leaning for either sentiment. In order to accommodate this extra category, a one vs all classifier model was used.

Data was extracted and labelled manually from the r/leagueoflegends subreddit, where the model would then subsequently be used. The subreddit was extracted using [this](https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/) torrent archive, since the Reddit API does not accommodate rigorous scraping on this scale. main.py showcases this extraction, a neccessity given the immensity of having the entire subreddit archive on display.

Approximately 1500 posts were labelled manually, around 500 per category. The first labelling, sentimentV1.csv, was relatively inaccurate, and was redone with an improved labelling framework, processData.py. After brief testing using testSent.py, the model was applied to the rest of the archive in sklearnFit.py. Finally, results were organized in graph.py to produce the graph, Results.png.

Analyzing the data, there are two main points of interest. Firstly, the initial year or so of the reddit's existance had a distinct lack of negative posts. This was even more apparant while labelling the data, largely sourced from this section of time. This could be attributed to the smaller community, leading to more communication and collaboration between subreddit users and players of the game. Many small online tourneys, hosted solely for interaction in the community and entertainment, were organized on the subreddit directly back then.

Another noticable moment is in 2022, where "neutral" posts spike dramatically. While difficult to speculate over, this may be attributed to the 2022 season's far reaching changes to League of Legends gameplay. With large item, summoner spell, and map changes, including new dragons, it is possible that a great deal of neutral discussion was spent over these ideas. Another explaination could be the drought in new gamemodes and a shift in the playerbase towards TFT, stealing away interesting topics and in game events that may have been discussed on the subreddit.

Overall, it is interesting to note the lack of sentiment change around annual events or championships. Certain shortcomings of the model may be responsible for this.

These shortcomings are as follows. Firstly, the model is trained on a relatively small dataset from the very beginning of the subreddit. While many datapoints were purposefully skipped during labelling to ensure higher quality and more explicit data, having double or triple the data would be ideal. 

Additionally, the model only takes into account the title of posts to simplify issues like links and media. Such a restriction contributed to the difficulty in manual labelling, and can cloud the accuracy of the model. The final accuracy came out to about 65%, which is better than it seems given the three categories, but still not stellar.

Finally, this task may simply be an ill suited one for sentiment analysis. r/leagueoflegends is ultimately a place primarily used to ask questions, as evidenced by the majority of neutral posts in general and the need to even create a neutral category of posts. The decently above random accuracy of the model does allow for some basic speculation, but the scope of such ideation should be kept within the scope of the model's reach.

In any case, the creation of this project was wonderful fun, and included a lot of silly tinkering with the sklearn technologies.
