# ------------------------------------------
# Writtern by Subhashis Suara / QuantumBrute
# ------------------------------------------

import praw
import datetime

# --------------------------------------------------------------------------------

subreddit_names = input("Enter the subreddits with space in between (example: redditdev pics food): ")
subreddit_names_split = subreddit_names.split()
subreddit_names_join = '+'.join(subreddit_names_split)
subreddit_names_join_comma = ', '.join(subreddit_names_split)
limitno = int(input("Enter the total number of tites to get (Max: 1000): "))

#---------------------------------------------------------------------------------

print("Collecting requested data...")
print("Opening database...")
fout = open("Database.txt", "a+")

reddit = praw.Reddit(client_id= ' ',         
					 client_secret= ' ',
					 username= ' ',
					 password= ' ',
					 user_agent= 'Created by u/QuantumBrute') # Login to reddit API

def titles():
	try:
		try:
			print("Checking subreddits...")
			fout.write("\nDate & Time: {}\n".format(str(datetime.datetime.now())))
			fout.write("Subreddit: {}\n\n".format(subreddit_names_join_comma))
			for submission in reddit.subreddit(subreddit_names_join).hot(limit = limitno):
				fout.write("{}\n".format(submission.title))
			print("Adding titles to database...\n")
			print("Titles added to database succesfuly!\n")
			input("Press ENTER to exit...")
		except:
			pass
	except:
		print("One of the mentioned subreddits doesn't exist! Try again!")
		input("Press ENTER to exit...")

def main():
    titles()
    fout.close()
    
if __name__ == "__main__": 
    main()

	