1. Please run the Python code: "preprocessing.py" first, this program will generate 2 csv files, which are unique songIds and userIds in int type for songs and users in 1M dataset. (Please set the working directory)

2. 2 csv files will be used in Spark, songId and userId in int type and joined with our original 1M user dataset, so that we can use ALS.

3. All outputs are formed by userId of the original type, and songId with generated int type.